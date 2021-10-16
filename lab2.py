import math

def horizontal_distance(v, theta, del_h):
    """ (num, num, num) -> (num)
    This function recieves initial velocity, launch angle, and altitute change
    in the landing position and returns the horizontal range of a projectile.

    v is in [m/s]
    theta is in [degrees]
    del_h is in [m]
    
    >>> range = horizontal_distance(100, 20, 40)
    >>> range
	515.5652309241808
    """
    g = 9.81 #constant for gravitational acceleration in m/s^2
    rad_theta = theta*(math.pi/180) #converts from theta degrees to radians
    #range_formula = ((math.cos(rad_theta))*(((v*math.sin(rad_theta))/g)+(math.sqrt((((v**2)*((math.sin(rad_theta))**2))/(g**2)) - ((2*del_h)/g)))))*100
    
    p1 = math.cos(rad_theta)
    p2 = (v*math.sin(rad_theta))/g
    p4 = ((v**2)*((math.sin(rad_theta))**2))/(g**2)
    p5 = (2*del_h)/g
    p3 = math.sqrt(p4 - p5)
    range = (p1*(p2 + p3))*100
    
    return range

""" THIS CAN TEST YOUR CODE """
velocity = int(input("v = "))
angle = int(input("theta = "))
delta_h = int(input("del_h = "))

range = horizontal_distance(velocity, angle, delta_h)
print("The range is: "+str(range))
