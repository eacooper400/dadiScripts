#!/usr/bin/python
import numpy
from numpy import array
import dadi
import sys
sys.path.append("/home/ecoope4/dadiMonarcha/")
import Liz_Monarcha_dadimodels_FIX


"""
File: Liz_Monarcha_dadiAnalyses.py
Edited By: Liz Cooper; September 18, 2015
Original Author: Eric N. Rittmeyer

Created by Eric N. Rittmeyer on 10 December 2013

Description: This script runs five replicate analyses of dadi on the Tribolonotus pseudoponceleti dataset of Rittmeyer & Austin (in review) under Model 9. Requires the dadi, numpy, and scipy python packages, as well as the demographic models defined in RittmeyerAustin_Tribolonotus_dadimodels_7jan14.py
To run other models defined in the aforementioned file, changes to the 'func' definition, and the dimensionality of the parameter array ('params', 'upper_bound','lower_bound') are necessary. 

"""



data = dadi.Spectrum.from_file("/home/ecoope4/dadiMonarcha/MAK_SA_UGI.fs")
ns = data.sample_sizes

pts = [40,50,60]

func = Liz_Monarcha_dadimodels_FIX.Model4

params=array([1,1,1,1,1,1])
upper_bound = [10,10,10,10,10,10]
lower_bound = [1e-4,1e-4,1e-4,1e-4,1e-4,1e-4]

func_ex = dadi.Numerics.make_extrap_log_func(func)
model = func_ex(params, ns, pts)
ll_model = dadi.Inference.ll_multinom(model, data)
print 'Model log-likelihood:', ll_model
theta = dadi.Inference.optimal_sfs_scaling(model, data)
p0 = dadi.Misc.perturb_params(params, fold=1, upper_bound=upper_bound)
popt = dadi.Inference.optimize_log(p0, data, func_ex, pts, 
                                   lower_bound=lower_bound,
                                   upper_bound=upper_bound,
                                   verbose=len(params),
                                   maxiter=100)
print 'Optimized parameters', repr(popt)
model = func_ex(popt, ns, pts)
ll_opt = dadi.Inference.ll_multinom(model, data)
print 'Optimized log-likelihood:', ll_opt
