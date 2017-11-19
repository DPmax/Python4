# -*- coding: utf-8 -*-
"""

@author: LONGCHENG
"""

"381-LAB 4"
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.stats import expon

def CentrlLimitTheorem(N,n):
    mu_w = 2
    sigma_w = 0.57
    sigma_sn = sigma_w*math.sqrt(n)
    var = sigma_sn*sigma_sn
    mu_sn = n*mu_w
    nbins = 30      #number of bins
    edgecolor = 'w' #color separating bars in the bargraph
    x = np.zeros(N)
#calculations for X
    for k in range(N):
        # x is the array with the values
        # of the RV to be plotted
        # the min bookwidth = 1,
        # the max bookwidth = 3
        for l in range(n):
            x[k] += np.random.uniform(n*1,n*3)
        x[k] *= 1/n
#probability histogram of the RV S
    #create bins and histogram
    fig1 = plt.figure(n+1)
    bins = [float(x) for x in np.linspace(n*1, n*3, nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)
    #define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 =  (be1+be2) / 2
    barwidth = b1[1] - b1[0] #width of bars in the bargraph
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
#Gaussian function
    x0 = np.linspace(n*1,n*3)
    fact = 1/(np.sqrt(2*np.pi*var))
    y = fact*np.exp(-(x0-mu_sn)**2/(2*var))
#plotting of the Gaussian function
    plt.plot(x0,y, color='#A60628')
    plt.title('PDF of book stack height and comparison with Gaussian')
    plt.xlabel('Book stack height for n='+str(n)+' books')
    plt.ylabel('PDF')
    fig1.show()


def ExponentiallyDistributedRandomVariables(N):
    beta = 0.5
    #t is a exponential continuous random variable.
    t = expon.rvs(scale = beta, size = N)
#probability histogram of the RV T
    fig1 = plt.figure(1)
    plt.hist(t,bins = 31, normed = True, edgecolor='w')
    plt.xlim(0,4)
    
#Gaussian function
    x = np.linspace(0,4)
    y = 2*np.exp(-2*x)
    plt.plot(x,y, color='#A60628')
    plt.title('PDF of the RV T and comparison with g(x) plot')
    plt.ylabel('PDF')
    fig1.show()
    
def DistributionoftheSum(N,n):
    beta = 45
    mu_c = n* beta
    sigma_c = beta * np.sqrt(n)
    var = sigma_c * sigma_c
    nbins = 30
    edgecolor = 'w'
    x = np.zeros((N))
#calculations for X
    for k in range(N):
        # x is the array with the values
        # of the RV to be plotted
        for l in range(n):
            x[k] += np.random.exponential(beta)
#probability histogram of the RV T
    #create bins and histogram
    fig1 = plt.figure(3)
    bins = [float(x) for x in np.linspace(350,2100, nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)
    #define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 =  (be1+be2) / 2
    barwidth = b1[1] - b1[0] #width of bars in the bargraph
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
#plot the graph of normal distribution
    x0 = np.linspace(350,2100)
    fact = 1/(np.sqrt(2*np.pi*var))
    y = fact*np.exp(-(x0-mu_c)**2/(2*var))
    plt.plot(x0,y,color='#A60628')
    plt.title('PDF of the RV T and comparison with noraml distribution')
    plt.ylabel('PDF')
    fig1.show()
    
    
#plot of CDF
    fig2 = plt.figure(4)
    H1 = np.cumsum(h1)*barwidth
    plt.bar(b1,H1,width=barwidth,edgecolor=edgecolor)
    plt.title('CDF of the lifetime of a carton')
    plt.ylabel('CDF')
    fig2.show()
    

    




CentrlLimitTheorem(10000,1)
CentrlLimitTheorem(10000,5)
CentrlLimitTheorem(10000,10)
CentrlLimitTheorem(10000,15)
#ExponentiallyDistributedRandomVariables(10000)
#DistributionoftheSum(10000,24)