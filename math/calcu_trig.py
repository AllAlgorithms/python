from math import sqrt

sign = ["",
        "","",'-','-', #sin
        "",'-',"-",'', #cos
        "",'-','',"-"] #tan

def trig_func(name,value,quad=1):
    if name == 'tan':
        cos = sqrt(1 / (value ** 2 + 1))
        sin = abs(value * cos)
        print("sin={}{},cos={}{},tan={}".format(sign[quad],
                                                sin,sign[quad+4],
                                                cos,value))

    elif name == 'sin':
        cos = sqrt(1 - value ** 2)
        tan = abs(value / cos)
        print("sin={},cos={}{},tan={}{}".format(value,
                                                sign[quad+4],cos,
                                                sign[quad+8],tan))

    elif name == 'cos':
        sin = sqrt(1 - value ** 2)
        tan = abs(sin / value)
        print("sin={}{},cos={},tan={}{}".format(sign[quad],sin,
                                                value,
                                                sign[quad+8],tan))

    else:
        print('not sin,cos,tan')
