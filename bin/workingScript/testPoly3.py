#%load_ext autoreload
#%autoreload 2
### now we test on a standard rectangle case
from pygotools.direct import direct, directOptim
from pygotools.optutils import optimTestFun, consMani
import pygotools.direct
import numpy
import scipy.spatial
import matplotlib.pyplot as plt

boundSize = 2
lb = -numpy.ones(2) * boundSize
ub = numpy.ones(2) * boundSize

func = optimTestFun.rosen

rectListOptim,output = directOptim(func,lb,ub,
                                                 iteration=50,
                                                 numBox=1000,
                                                 targetMin=0,
                                                 scaleOutput=False,
                                                 full_output=True)

pygotools.direct.plotDirectBox(rectListOptim,lb,ub,scaleOutput=False)

# class object 
directObj = direct(func,lb,ub)
rectListOptim,output = directObj.divide(50,numBox=10000,full_output=True)

potentialIndex = pygotools.direct.identifyPotentialOptimalObjectPareto(rectListOptim)
pygotools.direct.plotParetoFrontRect(rectListOptim,potentialIndex)

pygotools.direct.plotDirectBox(rectListOptim,lb,ub,scaleOutput=False)

# in terms of inequalities 
A = numpy.array([[-1.,-1.],[1.,-1]])
b = numpy.array([0,1])
A,b = consMani.addBoxToInequalityLBUB(lb,ub,A,b)

directObj = direct(func,lb,ub,A,b)
polyListOptim,output = directObj.divide(15,numBox=2000,full_output=True)

potentialIndex = pygotools.direct.identifyPotentialOptimalPolygonPareto(polyListOptim)

pygotools.direct.plotDirectPolygon(polyListOptim,potentialIndex)

pygotools.direct.directUtil.plotParetoFrontPoly(polyListOptim,potentialIndex)

index = directUtil.findLowestObjIndex(polyListOptim)
polyListOptim[index].getFx()
polyListOptim[index].getLocation()


for i in range(0,len(polyListOptim)):
    print "poly " +str(i)
    print "location"
    print polyListOptim[i].getLocation()
    print "gradient"
    print polyListOptim[i].getGrad()
    #print polyListOptim[i].getVertices()

# in 3 dimension
lb = numpy.array([-2.,-2.,-2],float)
ub = numpy.array([2.,2.,2],float)

func = optimTestFun.rosen

rectListOptim,output = directAlg.directOptim(func,lb,ub,
                                             iteration=50,
                                             numBox=1000,
                                             targetMin=0,
                                             scaleOutput=False,
                                             full_output=True)

pyOptimUtil.direct.plotDirectBox(rectListOptim,lb,ub,scaleOutput=False)

# class object 
directObj = directAlg.direct(func,lb,ub)
rectListOptim,output = directObj.divide(50,numBox=10000,full_output=True)

potentialIndex = directUtil.identifyPotentialOptimalObjectPareto(rectListOptim)
pyOptimUtil.direct.directUtil.plotParetoFrontRect(rectListOptim,potentialIndex)

pyOptimUtil.direct.plotDirectBox(rectListOptim,lb,ub,scaleOutput=False)

# in terms of inequalities 
A,b = polyOperation.addBoxToInequalityLBUB(lb,ub)

directObj = directAlg.direct(func,lb,ub,A,b)
polyListOptim,output = directObj.divide(10,numBox=2000,full_output=True)

potentialIndex = polyOperation.identifyPotentialOptimalPolygonPareto(polyListOptim)

pyOptimUtil.direct.directUtil.plotParetoFrontPoly(polyListOptim,potentialIndex)

pyOptimUtil.direct.plotDirectPolygon(polyListOptim,potentialIndex)

index = directUtil.findLowestObjIndex(polyListOptim)
polyListOptim[index].getFx()
polyListOptim[index].getLocation()



#

from pyGenericOdeModel import operateOdeModel,modelDef,odeLossFunc
import numpy
import scipy.integrate
import math,time,copy
import matplotlib.pyplot 
from openopt import NLP,GLP

from numpy import cos, arange, ones, asarray, abs, zeros, sqrt, asscalar
from pylab import legend, show, plot, subplot, xlabel, subplots_adjust
from string import rjust, ljust, expandtabs


ode = modelDef.LegrandEbola()

yDeath = [29.0, 59.0, 60.0, 62.0, 66.0, 70.0, 70.0, 80.0, 83.0, 86.0, 95.0, 101.0, 106.0, 108.0, 122.0, 129.0, 136.0, 141.0, 143.0, 149.0, 155.0, 157.0, 158.0, 157.0, 171.0, 174.0, 186.0, 193.0, 208.0, 215.0, 226.0, 264.0, 267.0, 270.0, 303.0, 305.0, 307.0, 309.0, 304.0, 310.0, 310.0, 314.0, 319.0, 339.0, 346.0, 358.0, 363.0, 367.0, 373.0, 377.0, 380.0, 394.0, 396.0, 406.0, 430.0, 494.0, 517.0, 557.0, 568.0, 595.0, 601.0, 632.0, 635.0, 648.0, 710.0, 739.0, 768.0, 778.0, 843.0, 862.0, 904.0, 926.0, 997.0]

yCase = [49.0, 86.0, 86.0, 86.0, 103.0, 112.0, 112.0,  122.0,  127.0,  143.0,  151.0,  158.0,  159.0,  168.0,  197.0, 203.0,  208.0,  218.0,  224.0,  226.0,  231.0,  235.0,  236.0,  233.0,  248.0,  258.0,  281.0,  291.0,  328.0,  344.0, 351.0,  398.0,  390.0,  390.0,  413.0,  412.0,  408.0,  409.0,  406.0,  411.0,  410.0,  415.0,  427.0,  460.0,  472.0, 485.0, 495.0, 495.0, 506.0, 510.0, 519.0,  543.0,  579.0, 607.0,  648.0,  771.0,  812.0,  861.0,  899.0,  936.0, 942.0, 1008.0, 1022.0, 1074.0, 1157.0, 1199.0, 1298.0, 1350.0, 1472.0, 1519.0, 1540.0, 1553.0, 1906.0]


# the corresponding
t = [0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 10.0, 13.0, 16.0, 18.0, 20.0, 23.0, 25.0, 26.0, 29.0, 32.0, 35.0, 40.0, 42.0, 44.0, 46.0, 49.0, 51.0, 62.0, 66.0, 67.0, 71.0, 73.0, 80.0, 86.0, 88.0, 90.0, 100.0, 102.0, 106.0, 108.0, 112.0, 114.0, 117.0, 120.0, 123.0, 126.0, 129.0, 132.0, 135.0, 137.0, 140.0, 142.0, 144.0, 147.0, 149.0, 151.0, 157.0, 162.0, 167.0, 169.0, 172.0, 175.0, 176.0, 181.0, 183.0, 185.0, 190.0, 193.0, 197.0, 199.0, 204.0, 206.0, 211.0, 213.0, 218.0]

# initial guess
theta = numpy.array([0.5,0.5,0.5,### the beta
                     2.0,1.5,1.0,3.0,      ### the omega
                     0.5,0.5,0.5, ### alpha, delta, theta
                     10,10])  ### kappa,intervention time

theta = numpy.array([0.588,0.794,1.653, ### the beta
                     10.0/7.0,9.6/7.0,5.0/7.0,2.0/7.0, ### the omega
                     7.0/7.0,0.81,0.80, ### alpha, delta, theta
                     300,12.0])  ### kappa,intervention time


# starting value
y = numpy.reshape(numpy.append(numpy.array(yCase),numpy.array(yDeath)),(len(yCase),2),'F') / 1175e4 
x0 = [1, 49.0/1175e4, 0.0, 0.0, 0.0, 29.0/1175e4]
t0 = 0

objLegrand = odeLossFunc.squareLoss(theta,ode,x0,t0,t[1::],y[1::,:],['I','R'],[1175e4,1175e4])


boxBounds = [
          (0.0,2.0),
          (0.0,2.0),
          (0.0,2.0),
          (0.0,100.0),
          (0.0,100.0),
          (0.0,100.0),
          (0.0,100.0),
          (0.0,100.0),
          (0.0,1.0),
          (0.0,1.0),
          (0.0,1000.0),
          (0.0,218.0)
           ]

cons = ({'type': 'ineq',
          'fun' : lambda x: numpy.array([x[3]-x[5],x[4]-x[5]])
          })


npBox = numpy.array(boxBounds)

lb = npBox[:,0]
ub = npBox[:,1]

# define our inequality
A = numpy.zeros((2,len(theta)))
A[0,3] = -1
A[0,5] = 1
A[1,4] = -1
A[1,5] = 1
b = numpy.zeros(2)



directObj = directAlg.direct(objLegrand.cost,lb,ub,A,b)
polyListOptim,output = directObj.divide(0,numBox=2000,full_output=True)

G,h = polyOperation.addBoxToInequalityLBUB(lb,ub,A,b)

V = polyOperation.constraintToVertices(G,h)

index = polyOperation.redundantConstraint(G,h)

index = polyOperation.bindingConstraint(G,h).tolist()

x0, sol, G1, h1 = polyOperation.findAnalyticCenter(G,h,True)

x0 = matrix(x0)

d = h1 - G1 * x0

D = mul(d[:,matrix(0,(1,len(x0)))]**-1,G1)
hull = scipy.spatial.ConvexHull(D,False)

i = 0

F = D[hull.simplices[i].tolist(),:]
y = matrix(1.0,(len(F[:,0]),1))

numpy.linalg.matrix_rank(numpy.array(F))
numpy.linalg.matrix_rank(numpy.array(D))

u,s,v = numpy.linalg.svd(numpy.array(D))

beta,e,rank,s = numpy.linalg.lstsq(numpy.array(F),numpy.array(y))

y1 = y 
lapack.gels(+F,y1)

u,s,v = numpy.linalg.svd(hull.simplices)

polyObj = polyOperation.PolygonObj(func,G,h)

A1,b1 = polyObj.getInequality()

V1 = polyObj.getVertices()

potentialIndex = polyOperation.identifyPotentialOptimalPolygonPareto(polyListOptim)

pyOptimUtil.direct.directUtil.plotParetoFrontPoly(polyListOptim,potentialIndex)

