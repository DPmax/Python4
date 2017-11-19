# Python4

Laboratory Project 4
Central Limit Theorem Simulate RVs with Exponential Distribution

1.	The Central Limit Theorem
Introduction: If x1,x2…xn are independent random variables having te same probability distribution with mean mu and standard deviation sigma, consider the sum Sn = x1+x2…+xn. This sum Sn is a random variable with mean mu_sn = n*sigma and standard deviation sigma_sn = sigma*sqrt(n). The PDF of the normally distributed RV. Sn is given by f(Sn) = 1/sigma_sn * sqrt(2*pi) * exp(-(x-mu_Sn)^2/2*sigma_Sn^2). 
Methodology: The methodology I used is generate n numbers of random number for x array. The number n could be 1, 5, 10, 15. Make n = 1 and run experiments 10000 times to simulate the RV S = W1. After the N experiments are completed, create and plot a probability histogram of the RV S and compare with normal distribution probability function plot of f(x).
Result: the plot of PDF of book stack height and comparison with Gaussian
  

2.	Exponentially Distributed Random Variables

Introduction: Simulate a R.V. with exponential probability distribution. As the PDF of a random variable exponentially distributed is defined as f(t) = 1/beta exp(-1/beta * t) when t >= 0. 
Methodology: Give by the following PDF f(t) = 2exp(-2t) when t>=0, generate the probability histogram of the random variable t using numpy.random.exponential() and do this experiment 10000 times. Last, compare with plot of function g(x) = 2exp(-2x)

Conclusion: the plot of PDF of R.V. T and comparison with normal distribution g(x)
Result:	
 












3.	Distribution of the Sum of RVs

Introduction: The lifetime(T) of the battery is a random variable with an exponentially distributed lifetime. A battery lasts an average of 45 days. The PDF of the battery life time is given by f(t) = 1/beta * exp * (-1/beta * t) when t >= 0 where beta = 45. The batteries are purchased in a carton of 24.
Methodology: To simulate the RV representing the lifetime of a carton of 24 batteries, use the numpy.random.exponential() to generate 24 numbers of x. Then, sum the numbers in x array to representing the life of the carton. Repeat this experiment for a total 10000times for N carton and create the experimental PDF of the lifetime of a carton. Last, compare with plot of the graph of a normal distribution and plot the CDF of the lifetime of a carton.
Result:  Compare the graph and based on the graph answer the question.
   

QUESTION	ANS.
1.	Probability that the carton will last longer than three years 1-F(1095) = 	0.42
2.	Probability that the carton will last between 2.0 and 2.5 years F(912) – F(730) =	0.24
