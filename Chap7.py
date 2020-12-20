#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:24:13 2020

@author: sijokuriakose
"""



import sys

from typing import Tuple
import math


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Returns mu and sigma corresponding to a Binomial (n, p)"""
    
    mu = p * n 
    sigma = math.sqrt(p*(1-p)*n)
    return mu, sigma


from scratch.probability import normal_cdf