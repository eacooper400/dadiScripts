#!/usr/bin/python
import numpy
import dadi
from dadi import Numerics, PhiManip,Integration,Spectrum

def Model1((nuMAK,nuSAN,nuUGI,nuMAKSA,T1,T2),(n1,n2,n3),pts):
	xx=Numerics.default_grid(pts)
	phi = dadi.PhiManip.phi_1D(xx)
	phi = PhiManip.phi_1D_to_2D(xx,phi)
	phi = Integration.two_pops(phi,xx,T1,nu1=nuUGI,nu2=nuMAKSA,m12=0,m21=0)
	phi = PhiManip.phi_2D_to_3D_split_2(xx,phi)
	phi = Integration.three_pops(phi,xx,T2,nu1=nuMAK,nu2=nuSAN,nu3=nuUGI,m12=0,m21=0,m13=0,m31=0,m23=0,m32=0)
	sfs = dadi.Spectrum.from_phi(phi, (n1,n2,n3), (xx,xx,xx))
	return sfs

def Model2((nuMAK,nuSAN,nuUGI,nuMAKSA,T1,T2,m13,m31,m12,m21),(n1,n2,n3),pts):
	xx=Numerics.default_grid(pts)
	phi = dadi.PhiManip.phi_1D(xx)
	phi = PhiManip.phi_1D_to_2D(xx,phi)
	phi = Integration.two_pops(phi,xx,T1,nu1=nuUGI,nu2=nuMAKSA,m12=0,m21=0)
	phi = PhiManip.phi_2D_to_3D_split_2(xx,phi)
	phi = Integration.three_pops(phi,xx,T2,nu1=nuMAK,nu2=nuSAN,nu3=nuUGI,m12=m12,m21=m21,m13=m13,m31=m31,m23=0,m32=0)
	sfs = dadi.Spectrum.from_phi(phi, (n1,n2,n3), (xx,xx,xx))
	return sfs

def Model3((nuMAK,nuSAN,nuUGI,nuMAKSA,T1,T2,m23,m32,m12,m21,m13,m31),(n1,n2,n3),pts):
    	xx=Numerics.default_grid(pts)
    	phi = dadi.PhiManip.phi_1D(xx)
    	phi = PhiManip.phi_1D_to_2D(xx,phi)
    	phi = Integration.two_pops(phi,xx,T1,nu1=nuUGI,nu2=nuMAKSA,m12=0,m21=0)
	phi = PhiManip.phi_2D_to_3D_split_2(xx,phi)
    	phi = Integration.three_pops(phi,xx,T2,nu1=nuMAK,nu2=nuSAN,nu3=nuUGI,m12=m12,m21=m21,m13=m13,m31=31,m23=m23,m32=m32)
    	sfs = dadi.Spectrum.from_phi(phi, (n1,n2,n3), (xx,xx,xx))
	return sfs

def Model4((nuMAK,nuSAN,nuUGI,nuUGISAN,T1,T2),(n1,n2,n3),pts):
	xx=Numerics.default_grid(pts)
	phi = dadi.PhiManip.phi_1D(xx)
	phi = PhiManip.phi_1D_to_2D(xx,phi)
	phi = Integration.two_pops(phi,xx,T1,nu1=nuMAK,nu2=nuUGISAN,m12=0,m21=0)
	phi = PhiManip.phi_2D_to_3D_split_2(xx,phi)
	phi = Integration.three_pops(phi,xx,T2,nu1=nuMAK,nu2=nuSAN,nu3=nuUGI,m12=0,m21=0,m13=0,m31=0,m23=0,m32=0)
	sfs = dadi.Spectrum.from_phi(phi, (n1,n2,n3), (xx,xx,xx))
	return sfs

def Model5((nuMAK,nuSAN,nuUGI,nuUGISAN,T1,T2,m13,m31,m12,m21),(n1,n2,n3),pts):
	xx=Numerics.default_grid(pts)
	phi = dadi.PhiManip.phi_1D(xx)
	phi = PhiManip.phi_1D_to_2D(xx,phi)
	phi = Integration.two_pops(phi,xx,T1,nu1=nuMAK,nu2=nuUGISAN,m12=0,m21=0)
	phi = PhiManip.phi_2D_to_3D_split_2(xx,phi)
	phi = Integration.three_pops(phi,xx,T2,nu1=nuMAK,nu2=nuSAN,nu3=nuUGI,m12=m12,m21=m21,m13=m13,m31=m31,m23=0,m32=0)
	sfs = dadi.Spectrum.from_phi(phi, (n1,n2,n3), (xx,xx,xx))
	return sfs

def Model6((nuMAK,nuSAN,nuUGI,nuUGISAN,T1,T2,m23,m32,m12,m21,m13,m31),(n1,n2,n3),pts):
    	xx=Numerics.default_grid(pts)
    	phi = dadi.PhiManip.phi_1D(xx)
    	phi = PhiManip.phi_1D_to_2D(xx,phi)
    	phi = Integration.two_pops(phi,xx,T1,nu1=nuMAK,nu2=nuUGISAN,m12=0,m21=0)
	phi = PhiManip.phi_2D_to_3D_split_2(xx,phi)
    	phi = Integration.three_pops(phi,xx,T2,nu1=nuMAK,nu2=nuSAN,nu3=nuUGI,m12=m12,m21=m21,m13=m13,m31=31,m23=m23,m32=m32)
    	sfs = dadi.Spectrum.from_phi(phi, (n1,n2,n3), (xx,xx,xx))
	return sfs
