import math
import numpy as np
from dateutil import parser


if __name__ == '__main__':
    X = ['2016.03.26', '2016.05.16', '', '2016.05.21', '2016.05', '2016.05.21', '2016.05.21', '2016.12.09', '2016.12.25']
    Y = [51691, 50602, 0, '', -1, 0, 53202, 77288, 71403]
    for index, x in enumerate(X):
        while (not X[index]) or len(X[index]) != 10 or (not Y[index]) or Y[index] <= 0:
            X.pop(index)
            Y.pop(index)

    for index, x in enumerate(X):
        X[index] = (parser.parse(x) - parser.parse('2000.01.01')).days

    print X
    print Y

    z1 = np.polyfit(X, Y, 1)
    p1 = np.poly1d(z1)
    print z1
    print p1
    dm = "{:.0f}".format(z1[0] * 30)
    print dm