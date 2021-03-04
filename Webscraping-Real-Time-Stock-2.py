# Credits - eMaster Class Academy
# Webscraping RT part 1 needs to be running simutaneously for this to work
# CSV file name need to be changed accordingly 


## USING MATPLOTLIB TO CREATE THE ANIMATIONS

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation  #used for animations
from matplotlib import style

# STEPS - PULL DATE FROM WEB PAGE | PLACE IN CSV | PLOT CSV DATA

style.use('fivethirtyeight')   # is a style name in style.use function
fig = plt.figure()

# create a 2x2 figure, so need subplot (grids)

ax1 = fig.add_subplot(2,2,1)   #used to add an Axes to the figure as part of a subplot arrangement.

#Syntax: add_subplot(self, *args, **kwargs) ie 2x2, figure 1

# keep repeating for number of subplots (HSI had 4 )

ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)



# CREATE AN ANIMATION FUNCTION TO PULL DATA AND ADD INTO SUBPLOTS

def animate(i):
    df = pd.read_csv('rt1-stockdata.csv')
    
    # place what goes in y-axis ys and x-axis xs
    
    ys = df.iloc[1:, 2].values # .iloc = method to retrieve rows from a Data frame
    
    # for x-axis we place a list that contatins step size of y-axis
    
    xs = list(range(1, len(ys) + 1))
    
    ax1.clear() #clears existing results and wel replot values
    ax1.plot(xs, ys)
    
    ax1.set_title('CHK Holdings', fontsize = 12)
    
    #repleat for other graphs | no need to define xs again since its same for all graphs
    ys = df.iloc[1:, 3].values
    ax2.clear()
    ax2.plot(xs, ys)
    ax2.set_title('CLP Holdings', fontsize = 12)
    
    ys = df.iloc[1:, 4].values  
    ax3.clear()
    ax3.plot(xs, ys)
    ax3.set_title('HK & China Gas', fontsize = 12)
    
    ys = df.iloc[1:, 5].values   
    ax4.clear()
    ax4.plot(xs, ys)
    ax4.set_title('HSBC Holdings', fontsize = 12)
    
# ANIMATING THE RESULT

ani = animation.FuncAnimation(fig, animate, interval = 100) # .FuncAnimation(figure, function, update interval in ms)

plt.tight_layout
plt.show()