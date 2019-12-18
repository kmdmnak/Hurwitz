from flask import Flask, request
try:
    from .Hurwitz.hurwitzTest2 import HurwitzStabililtyTestForRealPolymonials
    from .Hurwitz.equation import solve_root
    app = Flask(__name__, static_url_path="/sources")
except Exception:
    # start in dev
    from Hurwitz.hurwitzTest2 import HurwitzStabililtyTestForRealPolymonials
    from Hurwitz.equation import solve_root
    app = Flask(__name__, static_url_path="/sources")
"""
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("key/hurwitz-key.json")
firebase_admin.initialize_app(cred)
"""
PORT_NUMBER = 3360


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    text = """
    <div id="app"></div>
    <div id="app1"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML"></script>
    <script src="./sources/main.js"></script>
    """
    return text


@app.route('/hurwitz', methods=["POST"])
def hurwitz():
    form_datas = request.get_json(force=True)
    coefficients = form_datas.get("coefficients", None)
    print(coefficients)
    H = HurwitzStabililtyTestForRealPolymonials(coefficients)
    result = H.execute()
    if result:
        print("this is hurwitz")
    else:
        print("this is not hurwitz")
    result_solve = None
    if len(coefficients) != 1:
        result_solve, roots = solve_root(coefficients, True)
    else:
        pass
    # to list
    roots = list(map(lambda x: {"x": float(x.real),
                                "y": float(x.imag)}, roots))
    print(roots)
    return {"roots": roots, "hurwitz_test": result}


if __name__ == "__main__":
    import socket
    app.run(
        host=socket.gethostbyname(socket.gethostname()),
        port=PORT_NUMBER,
        debug=True)


"""
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="/__/firebase/7.5.2/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="/__/firebase/7.5.2/firebase-analytics.js"></script>

<!-- Initialize Firebase -->
<script src="/__/firebase/init.js"></script>
"""
