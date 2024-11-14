#import packages
import matplotlib.pyplot as plt

#Functions
#plt.plot(x-axis, y-axis) #takes arguments that describe the data to be plotted, can call plt.plot() function again to add another line
#Add labels
#plt.xlabel('---')
#plt.ylabel('---')
#plt.title('---')
#plt.show()  #displays plot to screen, always at the end of the all the plt functions

#Scatterplots
#plt.scatter(x = , y = , color = , s = #size of markers)

#Histograms
#Is your data skewed? 
# Is your data centered around the average? 
# Do you have any abnormal data points (outliers) in your data?
#plt.hist(x = , bins = )
# normalize the frequency to 1, instead of frequency counts, add the argument normed=1 to normalize
#plt.hist(x = , bins = , normed=1)
#to layer the histogram with 2 or more histograms add another plt.hist() to the script before plt.show()
#add the alpha argument to change the transparency of the histogram (0-1)
#add the label argument (variable type str) within the plt.hist() function and then initialize the legend
#plt.legend() #initialize the legend