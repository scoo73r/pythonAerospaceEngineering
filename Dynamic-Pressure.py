from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

def density(height: float) -> float:
    """Returns the air density in slug/ft^3 based on altitude.
       Equations from https://www.grc.nasa.gov/www/k-12/rocket/atmos.html
    Args:
        height (float): altitude in feet

    Returns:
        float: Density in slugs/ft^3
    """
    if height < 36152.0:
        temp = 59 - 0.00356 * height
        p = 2116 * ((temp + 459.7)/518.6)**5.256
    elif 36152 <= height < 82345:
        temp = -70
        p = 473.1 * np.exp(1.73 - 0.000048 * height)
    else:
        temp = -205.05 + 0.00164 * height
        p = 51.97 * ((temp + 459.7)/389.98)**-11.388
    rho = p/(1718*(temp+459.7))
    return rho

def velocity(time: float, acceleration: float) ->float:
    """
    Convert time to velocity using Vf = Vi + at
    Vf = final velocity,
    Vi = initial velocity [0 in this case]
    a = acceleration
    t = time

    Args:
        time (float): time in seconds   
        acceleration (float): acceleration in ft/s^2

    Returns:
        float: velocity in ft/s
    """
    return acceleration*time

def altitude(time: float, acceleration: float) -> float:
    """
    Convert time to altitude using the constant time acceleration equation
    x = vi*t + 0.5*a*t^2 where vi = 0

    Args:
        time (float): Time in seconds
        acceleration (float): acceleration in ft/s^2

    Returns:
        float: Altitude in feet
    """
    return 0.5*acceleration*time**2

if __name__ == '__main__':
    
    plt.style.use('bmh')
    y_values = []
    x_values = np.arange(0.0, 550.0, 0.5)
    
    for elapsed_time in x_values:
        accel = 51.76 # ft/s^s
        alt = altitude(elapsed_time, accel)
        # Dynamic pressure q = 0.5 * density * velocity^2
        q = 0.5 * density(alt) * velocity(elapsed_time, accel) ** 2
        y_values.append(q)
    
    
    max_val = max(y_values)
    ind = y_values.index(max_val)
    
    
    plt.plot(x_values, y_values, 'b-', label=r"a = 51.76 $\frac{ft}{s^2}$")
    plt.annotate('{:.0f} psf @ {} s'.format(max_val, x_values[ind]),
                 xy=(x_values[ind] + 2, max_val),
                 xytext=(x_values[ind] + 15, max_val +15),
                 arrowprops=dict(facecolor='blue', shrink=0.05))
    
    plt.plot(x_values[ind], max_val, 'rx')
    
    
    y2_values = []
    for elapsed_time in x_values:
        accel = 32.2
        alt = altitude(elapsed_time, accel)
        q = 0.5 * density(alt) * velocity(elapsed_time, accel) ** 2
        y2_values.append(q)
    
    max_val = max(y2_values)
    ind = y2_values.index(max_val)
    plt.plot(x_values, y2_values, 'k-', label=r"a = 32.2 $\frac{ft}{s^2}$")
    plt.annotate('{:.0f} psf @ {} s'.format(max_val, x_values[ind]),
                 xy=(x_values[ind] + 2, max_val),
                 xytext=(x_values[ind] + 15, max_val +15),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    
    plt.plot(x_values[ind], max_val, 'rx')
    
    y3_values = []
    for elapsed_time in x_values:
        accel = 20.0
        alt = altitude(elapsed_time, accel)
        q = 0.5 * density(alt) * velocity(elapsed_time, accel) ** 2
        y3_values.append(q)
    
    max_val = max(y3_values)
    ind = y3_values.index(max_val)
    plt.plot(x_values, y3_values, 'g-', label=r"a = 20.0 $\frac{ft}{s^2}$")
    plt.annotate('{:.0f} psf @ {} s'.format(max_val, x_values[ind]),
                 xy=(x_values[ind] + 2, max_val),
                 xytext=(x_values[ind] + 15, max_val +15),
                 arrowprops=dict(facecolor='green', shrink=0.05))
    
    plt.plot(x_values[ind], max_val, 'rx')
    
    plt.xlim(0, 150)
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (psf)')
    plt.title('Dynamic pressure as a function of time')
    plt.legend()
    plt.show()