
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
# Model name = Lenbury2001_InsulinKineticsModel_A
#
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
# Compartment: id = COMpartment, name = COMpartment, constant
	compartment_COMpartment=1.0;
# Parameter:   id =  time_environment, name = time
	global_par_time_environment=NaN;
# Parameter:   id =  x, name = x
# Parameter:   id =  r_1, name = r_1
	global_par_r_1=0.2;
# Parameter:   id =  r_2, name = r_2
	global_par_r_2=0.1;
# Parameter:   id =  c_1, name = c_1
	global_par_c_1=0.1;
# Parameter:   id =  y, name = y
# Parameter:   id =  r_3, name = r_3
	global_par_r_3=0.1;
# Parameter:   id =  r_4, name = r_4
	global_par_r_4=0.1;
# Parameter:   id =  c_2, name = c_2
	global_par_c_2=0.1;
# Parameter:   id =  z, name = z
# Parameter:   id =  r_5, name = r_5
	global_par_r_5=0.1;
# Parameter:   id =  r_6, name = r_6
	global_par_r_6=0.1;
# Parameter:   id =  r_7, name = r_7
	global_par_r_7=0.05;
# Parameter:   id =  z_hat, name = z_hat
	global_par_z_hat=2.0;
# Parameter:   id =  y_hat, name = y_hat
	global_par_y_hat=1.24;
# Parameter:   id =  epsilon, name = epsilon
	global_par_epsilon=0.1;
# rateRule: variable = x
global_par_x = x(1);
# rateRule: variable = y
global_par_y = x(2);
# rateRule: variable = z
global_par_z = x(3);
	xdot=zeros(3,1);
	# rateRule: variable = x
	xdot(1) = global_par_z*(global_par_r_1*global_par_y+(-global_par_r_2)*global_par_x+global_par_c_1);

	# rateRule: variable = y
	xdot(2) = global_par_epsilon*(global_par_r_3/global_par_z-global_par_r_4*global_par_x+global_par_c_2);

	# rateRule: variable = z
	xdot(3) = global_par_r_5*(global_par_y-global_par_y_hat)*(global_par_z_hat-global_par_z)+global_par_r_6*global_par_z*(global_par_z_hat-global_par_z)-global_par_r_7*global_par_z;

endfunction

#Initial conditions vector
x0=zeros(3,1);
x0(1) = 4.0;
x0(2) = 0.0;
x0(3) = 1.0;


#Creating linespace
t=linspace(0,90,100);

#Solving equations
x=lsode("f",x0,t);

#ploting the results
plot(t,x);