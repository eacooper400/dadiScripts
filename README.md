# 6 Migration Models for running dadi on Monarcha data

Original python scripts created by Eric Rittmeyer (2015).  Please cite ![this paper](http://onlinelibrary.wiley.com/doi/10.1111/mec.13030/abstract)
Scripts edited by L. Cooper, 2016

## 1.  dadimodels_FIX.py
This file contains ALL 6 migration models tested in dadi.
*  Model 1 = No migration; SNAPP tree
*  Model 2 = Adjacent migration; SNAPP tree
*  Model 3 = Full migration; SNAPP tree
	
*  Model 4 = No migration; Original/plumage color tree
*  Model 5 = Adjacent migration; plumage color tree
*  Model 6 = Full Migration; plumage color tree

## 2.  Three files called "Liz_Monarcha_dadi_*Mig.py"
These are the files to run each model (with the SNAPP tree) for 100 iterations.  Each of these runs was submitted 10 independent times 

## 3.  Three files called "Liz_Monarcha_dadi_*Mig_alt.py"
Same as above, but for running models with the plumage color tree
