# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:56:52 2016

@author: sarapeletz

"""

import math


"""
Function: calculate_n
Description: Calculates the day of the year 

Input: 
day: date used for calculation | Integer [1,31] (days)
month: month used for calculation | Integer [1,365] (months)

Output:
n: Day of the year | Integer [1,365] (days)

"""

def calculate_n(day,month):
    if month==1: 
        n=day
    elif month==2: 
        n=day+31
    elif month==3: 
        n=day+59
    elif month==4:
        n=day+90
    elif month==5: 
        n=day+120
    elif month==6: 
        n=day+151
    elif month==7:
        n=day+181
    elif month==8: 
        n=day+212
    elif month==9: 
        n=day+243
    elif month==10:
        n=day+273
    elif month==11: 
        n=day+304
    else:
        n=day+334
    return n



"""
Function: calculate_std_time
Description: Calculates the standard time for the year 2015 in Central Time Zone
Source: http://www.timeanddate.com/time/dst/2015.html to know DST start/end date

Input: 
hour: hour used for calculation | Integer [0,24] (hours)
minutes: minutes used for calculation | Integer [0,59] (minutes)

Output:
std_time: Standard time | Integer [0,1440] (minutes)

"""

def calculate_std_time(hour,minutes,n):
    if n>=88 and n<298: 
        std_time=(hour*60)+minutes-60
    else:
        std_time=(hour*60)+minutes
    return std_time



"""
Function: calculate_et
Description: Calculates the error time related to experimental results

Input: 
n: Day of the year | Integer [1,365] (days)

Output:
et: Error time | Integer [**range**] (**UNITS**)

"""

def calculate_et(n):
    d=360.0*(n-81.0)/365.0
    et=9.87*math.sin(2*d*math.pi/180.0)-7.53*math.cos(d*math.pi/180.0)-1.50*math.sin(d*math.pi/180.0)
    return et



"""
Function: calculate_long_st
Description: Calculates the time zone

Input: 
longitude: Longitude | Float value [-180,180] (degrees)

Output:
long_st: Longitude rounded to nearest integer | Integer [-180,180] (degrees)

"""
 
def calculate_long_st(longitude):
   long_st=15*math.ceil(longitude/15)
   return long_st    
   

   
   
"""
Function: calculate_solar_time
Description: Calculates the solar time

Input: 
et: Error time | Integer [**range**] (**units**)
std_time: Standard time | Integer [0,1440] (minutes)
long_st: Longitude rounded to nearest integer | Integer [-180,180] (degrees)
longitude: Longitude | Float value [-180,180] (degrees)

Output:
solar_time: Solar time | Integer [**range**] (**units**)

"""   

def calculate_solar_time(et,std_time,long_st,longitude):
    solar_time=std_time+(4)*(long_st-longitude)+et
    return solar_time  







"""
Function: calculate_omega
Description: Calculates omega

Input: 
solar_time: Solar time | Float value [**range**] (**units**)

Output:
omega: Hour angle | Float value [**range**] (degrees where morning is negative)

"""  

def calculate_omega(solar_time):
    omega = (solar_time-720)/4
    return omega
    
    

"""
Function: calculate_delta
Description: Calculates delta

Input: 
n: Day of the year | Integer [1,365] (days)

Output:
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)

"""  

def calculate_delta(n):
    delta=(180.0/math.pi)*(23.45*math.sin(360.0*(math.pi/180.0)*((284.0+n)/365.0)))
    return delta



"""
Function: calculate_theta
Description: Calculates the angle theta

Input: 
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)
phi: Latitude | Float value [-90,90] (degrees where north is positive)
beta: Slope | Float value [0,180] (degrees)
gamma: Surface azimuth angle | Float value [-180,180] (degrees where east is negative)
omega: Hour angle | Float value [**range**] (degrees where morning is negative)

Output:
theta: Angle of incidence between sun and surface normal | Float value [**range**] (degrees)

"""  

def calculate_theta(delta,phi,beta,gamma,omega):
    a=math.sin(delta*math.pi/180.0)*math.sin(phi*math.pi/180.0)*math.cos(beta*math.pi/180.0)
    b=math.sin(delta*math.pi/180.0)*math.cos(phi*math.pi/180.0)*math.sin(beta*math.pi/180.0)*math.cos(gamma*math.pi/180.0)
    c=math.cos(delta*math.pi/180.0)*math.cos(phi*math.pi/180.0)*math.cos(beta*math.pi/180.0)*math.cos(omega*math.pi/180.0)
    d=math.cos(delta*math.pi/180.0)*math.sin(phi*math.pi/180.0)*math.sin(beta*math.pi/180.0)*math.cos(gamma*math.pi/180.0)*math.cos(omega*math.pi/180.0)
    e=math.cos(delta*math.pi/180.0)*math.sin(beta*math.pi/180.0)*math.sin(gamma*math.pi/180.0)*math.sin(omega*math.pi/180.0)
    theta = math.acos(a-b+c+d+e)*(180.0/math.pi)
    return theta
    


'''

#Calculates the solar time for Santander, 3rd january, 11:50h
santander_n = calculate_n(3,1)
santander_std_time = calculate_std_time(11,50,santander_n)
santander_et = calculate_et(santander_n)
santander_long_st = calculate_long_st(-3.81)
santander_solar_time = calculate_solar_time(santander_et,santander_std_time,santander_long_st,-3.81)
santander_omega = calculate_omega(santander_solar_time)
santander_delta = calculate_delta(santander_n)
santander_theta = calculate_theta(santander_delta,43.4623,36,-2,santander_omega)


#Prints the results
print "\nSantander at 11:50AM on January 3"
print "standard time = %.0f" % santander_std_time
print "error time = %.3f" % santander_et
print "longitude st = %.0f" % santander_long_st
print "solar time = %.3f" % santander_solar_time
print "omega = %.3f degrees" % santander_omega
print "delta = %.3f degrees" % santander_delta
print "theta = %.3f degrees" % santander_theta
'''







"""
Function: obtimize_beta
Description: Calculates the optimum beta

Input: 
delta: **what is this** | Float value [**range**] (degrees)
phi: **what is this** | Float value [**range**] (degrees)
beta: **what is this** | Float value [**range**] (degrees)
gamma: **what is this** | Float value [**range**] (degrees)
omega: **what is this** | Float value [**range**] (degrees)

Output:
beta: angle **what is this** | Float value [**range**] (degrees)

"""  


#Calculate the optimum value for beta 



"""
Function: calculate_theta_z
Description: Calculates the zenith angle 

Input: 
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)
phi: Latitude | Float value [-90,90] (degrees where north is positive)
omega: Hour angle | Float value [**range**] (degrees where morning is negative)

Output:
theta_z: Zenith angle | Float value [**range**] (degrees **where**)

"""  

def calculate_theta_z(delta,phi,omega):
    f=math.sin(delta*math.pi/180.0)*math.sin(phi*math.pi/180.0)
    g=math.cos(delta*math.pi/180.0)*math.cos(phi*math.pi/180.0)*math.cos(omega*math.pi/180.0)
    theta_z=math.acos(f+g)*(180.0/math.pi)
    return theta_z


"""
Function: calculate_gamma_s
Description: Calculates the solar azimuth angle

Input: 
omega: Hour angle | Float value [**range**] (degrees where morning is negative)
theta_z: Zenith angle | Float value [**range**] (degrees **where**)
phi: Latitude | Float value [-90,90] (degrees where north is positive)
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)

Output:
gamma_s: Solar azimuth angle | Float value [**range**] (degrees **where**)

"""  

def calculate_gamma_s(omega,theta_z,phi,delta):
    h=math.sin(omega*math.pi/180.0)
    i=math.cos(theta_z*math.pi/180.0)*math.sin(phi*math.pi/180.0)-math.sin(delta*math.pi/180.0)
    j=math.sin(theta_z*math.pi/180.0)*math.cos(phi*math.pi/180.0)
    gamma_s=h*math.acos(i/j)*(180.0/math.pi)
    return gamma_s




'''


#Calculates the zenith and solar azimuth angles for Santander at 9:30 AM on February 13
#Assumes horizontal surface (beta=0)
santander2_n = calculate_n(13,2)
santander2_std_time = calculate_std_time(9,30,santander2_n)
santander2_et = calculate_et(santander2_n)
santander2_long_st = calculate_long_st(-3.81)
santander2_solar_time = calculate_solar_time(santander2_et,santander2_std_time,santander2_long_st,-3.81)
santander2_omega = calculate_omega(santander2_solar_time)
santander2_delta = calculate_delta(santander2_n)
santander2_theta_z = calculate_theta_z(santander2_delta,43.4623,santander2_omega)
santander2_gamma_s = calculate_gamma_s(santander2_omega,santander2_theta_z,43.4623,santander2_delta)

#Prints the results
print "\n\nSantander at 9:30AM on February 13"
print "standard time = %.0f" % santander2_std_time
print "error time = %.3f" % santander2_et
print "longitude st = %.0f" % santander2_long_st
print "solar time = %.3f" % santander2_solar_time
print "omega = %.3f degrees" % santander2_omega
print "delta = %.3f degrees" % santander2_delta
print "theta_z = %.3f degrees" % santander2_theta_z
print "gamma_s = %.3f degrees" % santander2_gamma_s

'''






"""
Function: calculate_omega_s
Description: Calculates the sunset hour angle

Input: 
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)
phi: Latitude | Float value [-90,90] (degrees where north is positive)

Output:
omega_s: Sunset hour angle | Float value [**range**] (degrees **where**)

"""  

def calculate_omega_s(delta,phi):
    omega_s=math.acos(-math.tan(delta*math.pi/180.0)*-math.tan(phi*math.pi/180.0))*(180.0/math.pi)
    return omega_s



"""
Function: calculate_omega_sr
Description: Calculates the sunrise hour angle

Input: 
omega_s: Sunset hour angle | Float value [**range**] (degrees **where**)

Output:
omega_sr: Sunrise hour angle | Float value [**range**] (degrees **where**)

"""  

def calculate_omega_sr(omega_s):
    omega_sr=-omega_s
    return omega_sr




"""
Function: calculate_n_dh
Description: Calculates the number of daylight hours

Input: 
phi: Latitude | Float value [-90,90] (degrees where north is positive)
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)

Output:
n_dh: Daylight hours | Float value [**range**] (hours)

"""  

def calculate_n_dh(phi,delta):
    n_dh=(2/15)*math.acos(-math.tan(phi*math.pi/180.0)*math.tan(delta*math.pi/180.0))*(180.0/math.pi)
    return n_dh


"""
Function: calculate_alpha_p
Description: Calculates the profile angle

Input: 
alpha_s: Latitude | Float value [-90,90] (degrees where north is positive)
gamma_s: Solar azimuth angle | Float value [**range**] (degrees **where**)
gamma: Surface azimuth angle | Float value [-180,180] (degrees where east is negative)


Output:
alpha_p: Profile angle | Float value [**range**] (degrees **where**)

"""  

def calculate_alpha_p(alpha_s,gamma_s,gamma):
    alpha_p=math.atan(math.tan(alpha_s*math.pi/180.0)/math.cos((math.pi/180.0)*(gamma_s-gamma)))*(180.0/math.pi)
    return alpha_p    


'''

#Calculates the time of sunrise, solar altitude, zenith, solar azimuth, profile angles
#For a 60degrees sloped surface facing 25degrees W of S at 4:00 PM solar time 
#On March 16 at latitude of 43degrees
santander3_n = calculate_n(16,3)
santander3_omega = calculate_omega(960)
santander3_delta = calculate_delta(santander3_n)
santander3_theta_z = calculate_theta_z(santander3_delta,43,santander3_omega)
santander3_gamma_s = calculate_gamma_s(santander3_omega,santander3_theta_z,43,santander3_delta)
santander3_omega_s = calculate_omega_s(santander3_delta,43)
santander3_omega_sr = calculate_omega_sr(santander3_omega_s)
santander3_n_dh = calculate_n_dh(43,santander3_delta)
santander3_alpha_p = calculate_alpha_p(60,santander3_gamma_s,25)



#Prints the results
print "\n\n60 degrees sloped surface facing 25 degrees W of S at 4:00PM solar time on March 16 at latitude of 43 degrees"
print "delta = %.3f degrees" % santander3_delta
print "omega_s = %.3f degrees" % santander3_omega_s
print "omega_sr = %.3f degrees" % santander3_omega_sr
print "n_dh = %.3f daylight hours" % santander3_n_dh
print "alpha_p = %.3f degrees" % santander3_alpha_p

'''




"""
Function: calculate_ratio_b
Description: Calculates the ratio of beam radiation

Input: 
theta: Angle of incidence between sun and surface normal | Float value [**range**] (degrees)
theta_z: Zenith angle | Float value [**range**] (degrees **where**)

Output:
ratio_b: Ratio of beam radiation | Float value [**range**] 

"""  

def calculate_ratio_b(theta,theta_z):
    ratio_b=math.cos(theta*math.pi/180.0)/math.cos(theta_z*math.pi/180.0)
    return ratio_b



"""
Function: calculate_h_o
Description: Calculates the daily solar radiation

Input: 
n: Day of the year | Integer [1,365] (days)
phi: Latitude | Float value [-90,90] (degrees where north is positive)
delta: Declination | Float value [-23.45,23.45] (degrees where north is positive)
omega_s: Sunset hour angle | Float value [**range**] (degrees **where**)

Output:
h_o: daily solar radiation | Float value [**range**] (**units**)

"""  

def calculate_h_o(n,phi,delta,omega_s):
    g_sc=1367 
    k=24*3600*g_sc/math.pi
    l=1+0.033*math.cos((360*math.pi/180.0)*n/365)
    m=math.cos(phi*math.pi/180.0)*math.cos(delta*math.pi/180.0)*math.sin(omega_s*math.pi/180.0)
    n=(math.pi*omega_s/180)*math.sin(phi*math.pi/180.0)*math.sin(delta*math.pi/180.0)
    h_o=k*l*(m+n)
    return h_o



'''

#Calculates the day's solar radiation on a horizontal surface in the absence of the atmosphere, at latitude 43 degrees N on April 15
#Assumes horizontal surface (beta=0)
santander4_n = calculate_n(15,4)
santander4_delta = calculate_delta(santander4_n)
santander4_omega_s = calculate_omega_s(santander4_delta,43)
santander4_h_o = calculate_h_o(santander4_n,43,santander4_delta,santander4_omega_s)

#Prints the results
print "\n\nHorizontal surface in the absense of the atmosphere at latitude 43 degrees N on April 15"
print "delta = %.3f degrees" % santander4_delta
print "omega_s = %.3f degrees" % santander4_omega_s
print "h_o = %.3f W/m^2" % santander4_h_o


'''