# -*- coding: utf-8 -*-
"""Chapter7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i6D6Syhy-arzX49bxXZCD_pT82Ukb8oe
"""

from typing import List 
from typing import Tuple 
import math

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
  #returns mu and sigma correpsonting to a binomial(n, p)
  mu = p * n 
  sigma = math.sqrt(p * (1-p) * n)
  return mu,sigma

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
  return (1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

normal_probablity_below = normal_cdf

def normal_probability_above(lo: float, 
                             mu: float = 0, 
                             sigma: float = 1) -> float:
      #the probability that an N(mu, sigma) is greater than lo. 
        return 1 - normal_cdf(lo, mu, sigma)

      #its between if its less than hi but not less than lo 
def normal_probabilty_between(lo: float, 
                                    hi: float, 
                                    mu: float = 0, 
                                    sigma: float = 1) -> float:
    #the probability that an N(mu, sigma) is between lo and hu 
        return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

        #its outside if its not between 
def normal_probability_outside(lo: float, 
                               hi: float, 
                               mu: float = 0, 
                               sigma: float = 1) -> float:
        return 1 - normal_probabilty_between(lo, hi, mu, sigma)
def inverse_normal_cdf(p: float, 
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
  # find approximate inverse using binary search 
  #if not standard, compute standard and rescale

  if mu != 0 or sigma != 1:
    return mu +sigma * inverse_normal_cdf(p, tolerance=tolerance)

  low_z = -10.0     #normal_cdf(-10) is (very close to) 0
  hi_z = 10.0       #normal_cdf(10) is (Very close to) 1 

  while hi_z - low_z > tolerance:
    mid_z = (low_z +hi_z) / 2 #consider the midpoint 
    mid_p = normal_cdf(mid_z) # and the cdfs values there
    if mid_p < p:
     low_z = mid_z #midpoint is too low, search above it
    else: 
      hi_z = mid_z #midpoint too high, seach bellow it 
  return mid_z

def normal_upper_bound(probability: float, 
                       mu: float = 0, 
                       sigma: float = 1) -> float:
                       #returns the z for which P(Z <=z) = probability 
      return inverse_normal_cdf(probability, mu, sigma)
    
def normal_lower_bound(probability: float, 
                       mu: float = 0, 
                       sigma: float = 1) -> float: 
                      #returns the z for which P(Z >= z) = probability 
      return inverse_normal_cdf(1-probability, mu, sigma)

def normal_two_sided_bounds(probability: float, 
                            mu: float = 0, 
                            sigma: float = 1) -> Tuple[float, float]:
                  #returns the symmetric (about the mean) bounds that contain the specified probability 
    tail_probability = (1-probability) /2

#upprt bound should have tail_probability above it 
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
  #upprt bound should have tail_probability below it 
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
  if x>= mu:
  #x is greater than the mean so the tail is everything greater than x
    return 2 * normal_probability_above(x, mu, sigma)
  else: 
    #x is less than the mean, so the tail is everything less than x 
    return 2 * normal_probablity_below(x, mu, sigma)
  
  upper_p_value = normal_probability_above 
  lower_p_value = normal_probabiity_below

two_sided_p_value(529.5, mu_0, sigma_0)

#p-Hacking 

from typing import List 

def run_experiment() -> List[bool]:
  #flips a fair coin 1k times, true = heads, false = tails 
  return[random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment: List[bool]) -> bool:
  #using the 5% significance levels 
  num_heads = len([flip for flip in experiment if flip])
  return num_heads < 469 or num_heads > 531

  random.seed(0)
  experiements = [run_experiement() for _ in range(1000)]
  num_rejections = len([experiment for experiment in experiments if reject_fairness(experiment)])

  assert num_rejections == 46


def estimated_parameters(N: int, n:int) -> Tuple[float, float]:
  p = n/ N
  sigma = math.sqrt(p * (1- p) / N)
  return p, sigma 


def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
  p_A, sigma_A = estimated_parameters(N_A, n_A)
  p_B, sigma_B = estimated_parameters(N_B, n_B)
  return(p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B **2)