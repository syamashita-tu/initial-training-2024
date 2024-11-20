"""
x=-3,-2,-1,0,1,2,3 に対して数値微分の関数 dfdx_approx を呼び出し、その結果得られた値と正確な微分の値(exp′(−3), ... ,exp′(3))とを比較して下さい。
対数関数 log(x) についても同様の実験を行い、x=0.25,0.5,1,2,4,8 に対して比較して下さい。Python から対数関数を呼び出す場合、math.log を使用しましょう。
"""


import math  # exp を呼び出すために math モジュールをインポート

def f(x):
    return math.exp(x)

def g(x):
    return math.log(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

for x in range(-3, 4):
    ans_f = dfdx_approx(x)
    print(f"x={x}のとき，df(x)/dx={ans_f}")

print()

for i in range(-2, 4):
    x = 2 ** i
    ans_g = dgdx_approx(x)
    print(f"x={x}のとき，dg(x)/dx={ans_g}")
