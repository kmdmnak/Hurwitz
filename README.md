# algorithm 1.3
P58-P62にあるアルゴリズムの実装

# Install
Python,pipはインストール済みとする.  

``` cmd
pip install git+https://github.com/KMDMNAK/Hurwitz.git
```
# Usage

``` python
from Hurwitz.hurwitzTest import HurwitzStabililtyTestForRealPolymonials
# test for x^3 + 2x^2 +3x + 4
hst=HurwitzStabililtyTestForRealPolymonials([1,2,3,4])

isHurwitz=hst.execute()
hst.P_array
```

# References
## class

### HurwitzStabililtyTestForRealPolymonials
#### property
- P_array  
#### methods
- execute
### HurwitzStabililtyTestForComplexPolymonials
  
### Class
- 
## checkpoints
- 係数の入力が分数だった場合.
  - 小数が入力された場合,分数に変換する?

# Content

## Hurwitz Stability

### Hurwitz Polynomial
実数nの多項式$P(z)$の全ての根が,複素平面における左半平面(開集合)上に存在するとき,多項式$P(z)$を,Hurwitz多項式であるという.  


## 反例
Hurwitzではない
[1,1,4,30]

