
#
# This file is automatically generated with 
# the System Biology Format Converter (http://sbfc.sourceforge.net/)
# from an SBML file.
#
# The conversion system has the following limitations:
#  - You may have to re order some reactions and Assignment Rules definition
#  - Delays are not taken into account
#  - You should change the lsode parameters (start, end, steps) to get better results
#

#
# The following line is there to be sure that Octave think that this file 
# is a script and not function file
#
1;

#
# Model name = Smith1980_HypothalamicRegulation
#
# is urn:miriam:biomodels.db:MODEL7898438988
# isDescribedBy urn:miriam:pubmed:6986927
#
function z=pow(x,y),z=x^y;endfunction
function z=root(x,y),z=y^(1/x);endfunction
function z = piecewise(varargin)
	numArgs = nargin;
	result = 0;
	foundResult = 0;
	for k=1:2: numArgs-1
		if varargin{k+1} == 1
			result = varargin{k};
			foundResult = 1;
			break;
		endif
	end
	if foundResult == 0
		result = varargin{numArgs};
	endif
z = result;
endfunction

function xdot=f(x,t)
# Compartment: id = Compartment, name = Compartment, constant
	compartment_Compartment=1.0;
# Parameter:   id =  R, name = R
# Parameter:   id =  h, name = h
	global_par_h=12.0;
# Parameter:   id =  c, name = c
	global_par_c=100.0;
# Parameter:   id =  b1, name = b1
	global_par_b1=1.29;
# Parameter:   id =  H, name = H
# Parameter:   id =  x, name = x
# Parameter:   id =  L, name = L
# Parameter:   id =  g1, name = g1
	global_par_g1=10.0;
# Parameter:   id =  b2, name = b2
	global_par_b2=0.97;
# Parameter:   id =  T, name = T
# Parameter:   id =  g2, name = g2
	global_par_g2=0.7;
# Parameter:   id =  b3, name = b3
	global_par_b3=1.39;
# rateRule: variable = R
global_par_R = x(1);
# rateRule: variable = L
global_par_L = x(2);
# rateRule: variable = T
global_par_T = x(3);
# assignmentRule: variable = x
	global_par_x=global_par_T-global_par_c/global_par_h;
# assignmentRule: variable = H
	global_par_H=piecewise(1, global_par_x > 0, 0);
	xdot=zeros(3,1);
	# rateRule: variable = R
	xdot(1) = (global_par_c-global_par_h*global_par_T)*(1-global_par_H)-global_par_b1*global_par_R;

	# rateRule: variable = L
	xdot(2) = global_par_g1*global_par_R-global_par_b2*global_par_L;

	# rateRule: variable = T
	xdot(3) = global_par_g2*global_par_L-global_par_b3*global_par_T;

endfunction

#Initial conditions vector
x0=zeros(3,1);
x0(1) = 0.5;
x0(2) = 22.0;
x0(3) = 15.0;


#Creating linespace
t=linspace(0,90,100);

#Solving equations
x=lsode("f",x0,t);

#ploting the results
plot(t,x);