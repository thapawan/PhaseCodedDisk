#import libaries
import numpy as np
import math
import matplotlib.pyplot as plt

'''kernel_size = 3
from PIL import Image as im

st = int(kernel_size / 2) - kernel_size + 1
end = kernel_size - int(kernel_size / 2)
loc_temp = np.arange(st,end)

for i in range(kernel_size):
    if i == 0:
        loc_x = loc_temp
    else:
        loc_x = np.append(loc_x,loc_temp)

x_arr = loc_x.reshape(kernel_size,kernel_size)
y_arr = np.transpose(x_arr)
r = 2 * np.arctan2(y_arr,x_arr)

dist = int(kernel_size / 2) * int(kernel_size / 2)
r_cos = np.cos(np.where(x_arr * x_arr + y_arr * y_arr > dist,math.nan,r)) # real part
r_sin = np.sin(np.where(x_arr * x_arr + y_arr * y_arr > dist,math.nan,r)) # imaginary part

# Calculate the complex values of the PCD
pcd = r_cos + 1j * r_sin

# Plot the PCD using matplotlib
plt.plot(pcd, label="PCD")

# Add a legend
plt.legend()

# Show the plot
plt.show()

'''# Create the plot
'''

plt.scatter(r_cos, r_sin, c=r, cmap="hsv")

# Add a colorbar
plt.colorbar()

# Show the plot
plt.show()

# Create the plot
'''
'''plt.plot(r, label="angle")

# Set the x-axis range
plt.xlim(-180, 180)

# Add a legend
plt.legend()

# Show the plot
plt.show()'''

'''
#print (r_cos)
#print (r_sin)

# Create the plot
#plt.plot(r_cos, r_sin)
#plt.plot(r_cos, label="r_cos")
#plt.plot(r_sin, label="r_sin")

# Add a legend
#plt.legend()

# Show the plot
#plt.show()
#print (r)'''
#change
#try
