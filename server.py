from flask import Flask, request
import socket
from Hurwitz.hurwitzTest2 import HurwitzStabililtyTestForRealPolymonials
from Hurwitz.equation import solve_root

PORT_NUMBER = 3360

app = Flask(__name__, static_url_path="/source")


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    text = """
    <div id="app"></div>
    <div id="app1"></div>
    <script src="./source/main.js"></script>
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
    return {"roots": roots}


if __name__ == "__main__":
    app.run(
        host=socket.gethostbyname(socket.gethostname()),
        port=PORT_NUMBER,
        debug=True)
