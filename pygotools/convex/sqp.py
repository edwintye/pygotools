
__all__ = [
    'sqp'
    ]

from pygotools.optutils.optCondition import exactLineSearch, sufficientNewtonDecrement
from pygotools.optutils.consMani import addLBUBToInequality
from pygotools.optutils.checkUtil import checkArrayType
from pygotools.optutils.disp import Disp
from pygotools.gradient.finiteDifference import forwardGradCallHessian

import numpy

from cvxopt.solvers import coneqp
from cvxopt import matrix

EPSILON = 1e-6
maxiter = 100

def sqp(func, grad, hessian=None, x0=None,
        lb=None, ub=None,
        G=None, h=None,
        A=None, b=None,
        disp=0, full_output=False):

    x = checkArrayType(x0)
    G, h = addLBUBToInequality(lb,ub,G,h)
    G = matrix(G)
    h = matrix(h)
    
    if A is not None:
        A = matrix(A)
    if b is not None:
        b = matrix(b)

    oldFx = numpy.inf
    fx = func(x)

    dispObj = Disp(disp)
    i = 0

    while abs(fx-oldFx)>=EPSILON:

        if hessian is None:
            H = forwardGradCallHessian(grad, x)
        else:
            H = hessian(x)

        g = grad(x)
        # readjust the bounds
        if G is not None:
            hTemp = h - G*matrix(x)
            dims = {'l': G.size[0], 'q': [], 's':  []}
        else:
            hTemp = None
            dims = []

        if A is not None:
            bTemp = b - A*matrix(x)
        else:
            bTemp = None

        # solving the QP to get the descent direction
        qpOut = coneqp(matrix(H), matrix(g), G, hTemp, dims, A, bTemp)
        # exact the descent diretion and do a line search
        deltaX = numpy.array(qpOut['x']).ravel()
        oldFx = fx
        t, fx = exactLineSearch(1, x, deltaX, func)
        
        #print qpOut

        x += t * deltaX
        i += 1
        dispObj.d(i, numpy.array(qpOut['z']).ravel(), fx, deltaX, g)
        
        if sufficientNewtonDecrement(deltaX,g):
            break
        
        if i >= maxiter:
            break

    # TODO: full_output- dual variables
    if full_output:
        return x, qpOut
    else:
        return x

