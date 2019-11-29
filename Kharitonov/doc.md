# Kharitonov


## 実数の場合
単多項式に対するHermite-Biehler Interlacing定理がどう構築されるか

$$
\Delta := \{\delta:\delta\in\mathbb{R}^{n+1}
x_i \leq \delta_i \leq y_i , i=0,...,n
\}
$$
に対して,いかなる多項式も最高次の係数は0にならないとする.  
この多項式群を$\bold{L}(s)$で定義する.

___
## 補題 5.1
以下のように表される二つの安定な多項式
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

## Kharitonov's Theorem
全ての多項式族は以下の四つの多項式がHurwitzとなるとき、そのときに限ってHurwitzである。
- $K^1(s)=x_0+x_1 s+y_2 s^2+y_3s^3+x_4s^4+x_5s^5+y_6s^6+...+$
- $K^2(s)=x_0+y_1s+y_2s^2+x_3s^3+x_4s^4 + y_5s^5+y_6s^6+...+$
- $K^3(s)=y_0+x_1s+x_2s^2+y_3s^3+y_4s^4+x_5s^5+x_6s^6+...+$
- $K^4(s)=y_0+y_1s+x_2s^2+x_3s^3+y_4s^4+y_5s^5+x_6s^6+...+$
____
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
と表せる.  

$$
\delta(s)=\delta_0+\delta_1s^1+\delta_2s^2+\delta_3s^3+...+\delta_ns^n+...
$$
とする.  
このとき,


$$
K^{o}_{max}(s)=y_1-x_3s^2+y_5y^4-x_7s^6+...+
$$

$$
\delta^o(\omega)=\delta_1-\delta_3\omega^2+\delta_5\omega^4+...+...

$$

$$
K^{o}_{min}(s)=x_1-y_3s^2+x_5y^4-y_7s^6+...+
$$

$$
K_{max}^{e}(s)=y_0-x_2s^2+y_4s^4-x_6s^6+...+
$$
$$
\delta^e(\omega)=\delta_0-\delta_2\omega^2+\delta_4\omega^4-\delta_6\omega^6+...+
$$
$$
K_{min}^{e}(s)=x_0-y_2s^2+x_4s^4-y_6y^6+...+
$$

となる。  

このとき,

$$
K_{max}^e(\omega)-\delta^e(\omega)=(y_0-\delta_0)+(\delta_2-x_2)\omega^2+(y_4-\delta_4)\omega^4+...+
$$
さらに,
$$
\delta^e(\omega)-K_{min}^e(\omega)=(\delta_0-x_0)+(y_2-\delta_2)\omega^2+(\delta_4-x_4)\omega^4+...+
$$
よって
$$
K_{min}^e(\omega)\leq\delta^e(\omega)\leq K^e_{max}(\omega)\ \ ,\forall\omega\in[0,\infty]
$$
同様に
$$
K_{min}^o(\omega)\leq\delta^o(\omega)\leq K^o_{max}(\omega)  ,\forall\omega\in[0,\infty]
$$

補題5.1を$K_3,K_4$に適用することで、
$$
K_{max}^{even}(s)+\delta^{odd}(s) ･･･(1)
$$ 
が安定であることがわかる。  
同様に,補題5.2を$K_1,K_2$に適用することで、
$$
K_{min}^{odd}(s)+\delta^{odd}(s) ･･･(2)
$$

が安定であることがわかる。  
(1),(2)に補題5.2に適用することで、
$$
\delta^{even}(s)+\delta^{odd}(s)=\delta(s)
$$
は安定であることがわかる.

# Algorithm

1. $\Delta := \{\delta:\delta\in\mathbb{R}^{n+1}
x_i \leq \delta_i \leq y_i , i=0,...,n
\}$における$x_i,y_i,i=0,...n$を入力  

2. $x_i,y_i,i=0,...n$を元に,4つの多項式$K_1,K_2,K_3,K_4$を作る

3. $K_1,K_2,K_3,K_4$に対して,フルビッツ判定を行って,全て安定なら,この多項式族は安定


___

$$
\delta(j\omega)=\delta_0+\delta_1j\omega-\delta_2\omega^2-\delta_3j\omega^3+...+\delta_ns^n+...
$$

$$
\delta^{even}(i\omega)=\delta^e(\omega)=\delta_0-\delta_2\omega^2+\delta_4\omega^4+...+
$$
$$
\delta^{odd}(j\omega)=j\omega(\delta_1-\delta_3\omega^2+\delta_5\omega^4+...+...)

$$

$$
\delta^o(\omega)=\delta_1-\delta_3\omega^2+\delta_5\omega^4+...+...
$$

$$
P^e(\omega)=P^{even}(j\omega)
$$
$$
P^o(\omega)=\dfrac{P^{odd}(j\omega)}{j\omega}
$$
___