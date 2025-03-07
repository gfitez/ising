
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import json, hashlib



"""General Functions"""
"""
from ising import run_multi_core, set_input
from glob import glob

def run(params = {}):
    inp = set_input("")
    for key,value in params.items():
        inp[key]=value

    run_multi_core(inp)

Tc=2.269


for i in range(100):
    print(i)
    run({"t_step":0.01/3, "B":0.01, "flip_perc":0.1, "N":100, "t_min":1.2, "t_max":3.2, "n_burnin":60000, "n_steps":100000, "t_top":4, "B_top":1, "use_gaussian":False})
"""
from isingDELTARUN import run_multi_core, set_input
from glob import glob

def run(params = {}):
    inp = set_input("")
    for key,value in params.items():
        inp[key]=value

    run_multi_core(inp)

Tc=2.269


for i in range(100):
    print(i)
    run({"t_step":0.001, "B":0.0, "flip_perc":0.1, "N":100, "t_min":0, "t_max":0.5, "n_burnin":60000, "n_steps":100000, "t_top":4, "B_top":1, "use_gaussian":False})