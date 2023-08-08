# Object: 
# Calculate the average inflammation per day across all patients.
# Plot the result to discuss and share with colleagues.

import numpy
import glob
import matplotlib
import matplotlib.pyplot

# Create a sorted list of all file paths

filepaths = sorted(glob.glob(
    'C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation*.csv'))

data_list = []  # List to store all mean data arrays

# Loop over each file path and load data, calculate the mean, and store in the list
for filepath in filepaths:
    print(filepath)
    data = numpy.loadtxt(fname=filepath, delimiter=',')
    mean_data = numpy.mean(data, axis=1)
    data_list.append(mean_data)

# Now data_list is a list of mean data arrays, each representing the mean data from one of your files.
# You can then process each array in data_list as needed.

# Print the average inflammation for each file
print("Average inflammation for this file: ", numpy.mean(mean_data))


# Average inflammation per day

# Replace the '-01' with approriate day, such as '-02' or '*'
filepaths = glob.glob(
    'C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-01.csv') 


# Initialize a numpy array with zeroes of the same size as one day's data
# Assuming all files have same number of days (columns), we can use the shape from the first file

first_file_data = numpy.loadtxt(fname=filepaths[0], delimiter=',')
num_days = first_file_data.shape[1]
cumulative_daily_means = numpy.zeros(num_days)

# Iterate over all files
for filepath in filepaths:
    data = numpy.loadtxt(fname=filepath, delimiter=',')
    
    # Calculate the mean of each day (column-wise) for the current file
    daily_means = numpy.mean(data, axis=0)
    
    # Add these means to our cumulative sum
    cumulative_daily_means += daily_means

# Divide by the number of files to get the average across all files
average_daily_means = cumulative_daily_means / len(filepaths)

print(average_daily_means)

# Plot average, max, min of one file

data = numpy.loadtxt(
    fname= 'C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-01.csv',
    delimiter =',')

fig = matplotlib.pyplot.figure(figsize=(10.0,3.0))

axes1 = fig.add_subplot(1,3,1) # add_subplot(1, 3, index), which means 1 row and 3 columns and index is the position
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis = 0))
axes1.set_xlabel('day')

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis = 0))
axes2.set_xlabel('day')

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis = 0))
axes3.set_xlabel('day')

fig.tight_layout()

matplotlib.pyplot.savefig('inflammation.png')
matplotlib.pyplot.show()

#Plot the difference between the average inflammations reported in the first and second datasets
#(stored in inflammation-01.csv and inflammation-02.csv, correspondingly), i.e., 
#the difference between the leftmost plots of the first two figures.

data1 = numpy.loadtxt(
    fname='C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-01.csv',
    delimiter =',')
data2 = numpy.loadtxt(
    fname='C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-02.csv',
    delimiter =',')


average_inflammation1 = numpy.mean(data1, axis =0)
average_inflammation2 = numpy.mean(data2, axis =0)

difference = average_inflammation1-average_inflammation2

matplotlib.pyplot.plot(difference)
matplotlib.pyplot.title('Difference between data 1 and 2')
matplotlib.pyplot.xlabel('Measurement')
matplotlib.pyplot.ylabel('Difference in average measurement')
matplotlib.pyplot.show()

# Heat map between file 1 and file 2

import matplotlib.pyplot

# Replace the directory as needed
data1 = numpy.loadtxt(
    fname='C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-01.csv',
    delimiter =',')
data2 = numpy.loadtxt(
    fname='C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-02.csv',
    delimiter =',')

# Changing the size
fig = matplotlib.pyplot.figure(figsize=(10, 3)) 

# the location where graph will be located
axes1 = fig.add_subplot(1,2,1) # add_subplot(1, 2, index), which means 1 row and 2 columns and index is the position
axes2 = fig.add_subplot(1,2,2)


# Graphing the heatmap
heatmap1 = axes1.imshow(data1)
axes1.set_title('Heatmap for file #1')

Heatmap2 = axes2.imshow(data2)
axes2.set_title('Heatmap for file #2')

matplotlib.pyplot.show()

# Another heatmap

data1 = numpy.loadtxt(fname=
                   'C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-01.csv', 
                   delimiter=',')
data2 = numpy.loadtxt(fname=
                   'C:/Users/Owner/Downloads/swc-python/python-novice-inflammation-data/data/inflammation-02.csv', 
                   delimiter=',')

# create a figure object
fig, ax = matplotlib.pyplot.subplots(1, 2, figsize=(10, 3)) 

# create the heatmap on the first subplot
cax1 = ax[0].imshow(data1, aspect='auto', cmap='hot', interpolation='nearest')
ax[0].set_title('Heatmap for file #1')
fig.colorbar(cax1, ax=ax[0])

# create the heatmap on the second subplot
cax2 = ax[1].imshow(data2, aspect='auto', cmap='hot', interpolation='nearest')
ax[1].set_title('Heatmap for file #2')
fig.colorbar(cax2, ax=ax[1])

# show the plot

matplotlib.pyplot.show()

