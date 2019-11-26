# Kharitonov

- Robust Schurとの関係

## 実数の場合
単多項式に対するHermite-Biehler Interlacing定理がどう構築されるか

$$
\Delta := \{\delta:\delta\in\mathbb{R}^{n+1}
x_i \leq \delta_i \leq y_i , i=0,...,n
\}
$$
に対して,いかなる多項式も最高次の係数は0にならないとする.  
この多項式群を$\bold{L}(s)$で定義する.

## Kharitonov's Theorem
全ての多項式は以下の四つの多項式がHurwitzとなるとき、そのときに限ってHurwitzである。
- $K^1(s)=x_0+x_1 s+y_2 s^2+y_3s^3+x_4s^4+x_5s^5+y_6s^6$
- $K^2(s)=x_0+y_1s+y_2s^2+x_3s^3+x_4s^4 + y_5s^5+y_6s^6$
- $K^3(s)=y_0+x_1s+x_2s^2+y_3s^3+y_4s^4+x_5s^5+x_6s^6$
- $K^4(s)=y_0+y_1s+x_2s^2+x_3s^3+y_4s^4+y_5s^5+x_6s^6$

※これらの多項式は,heyperrectagleにおける対角に位置する頂点に値する.  
### 証明
$$
K_{max}^{even}(s):=y_0+x_2s^2+y_4s^4+x_6s^6+...+
$$
$$
K_{min}^{even}(s):=x_0+y_2s^2+x_4s^4+y_6y^6+...+
$$
$$
K^{odd}_{max}(s):=y_1s+x_3s^3+y_5y^5+x_7s^7+...+
$$
$$
K^{odd}_{min}(s):=x_1s+y_3s^3+x_5y^5+y_7s^7+...+
$$
と定義する.  
このとき、
$$
K^1(s)=K_{min}^{even}(s)+K^{odd}_{min}(s)
$$
$$
K^2(s)=K_{min}^{even}(s)+K^{odd}_{max}(s)
$$
$$
K^3(s)=K_{max}^{even}(s)+K^{odd}_{min}(s)
$$
$$
K^4(s)=K_{max}^{even}(s)+K^{odd}_{max}(s)
$$

___
## 補題 5.1
以下のように表される二つの多項式
$$
P_1(s)=P^{even}(s)+P_1^{odd}(s)
$$
$$
P_2(s)=P^{even}(s)+P_2^{odd}(s)
$$
が、等しい次数を持ち、任意の$\omega\in[0,\infin]$について
$$
P_1^o(\omega)\leq P_2^o(\omega)
$$

が成り立つとき、$P^{odd}(s)$が、任意の$\omega\in[0,\infin]$について

$$
P_1^o(\omega)\leq P^o(\omega) \leq P_2^o(\omega)
$$
を満たす全ての多項式$P(s)=P^{even}(s)+P^{odd}(s)$は安定となる。
___

