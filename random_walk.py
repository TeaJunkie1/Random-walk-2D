import numpy
import pylab
import random

n = 10000



#kolik bude stepů
#vytvoření 2 arrayu kde budou x a y koordinanty
#velikostí rovných číslu velikosti a vyplnit 0
x = numpy.zeros(n)
y = numpy.zeros(n)

#plnění koordinantů s náhodnými hodnotami
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

#grafovani
pylab.title("Nahodna prochazka  " + str(n) + " kroku" )
pylab.plot(x, y)
pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
pylab.show()