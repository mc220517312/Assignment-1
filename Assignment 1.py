####Section 1####
###Exercise 1###
# Import pandas
import pandas as pd

recent_grade_url = "https://raw.githubusercontent.com/mc220517312/Assignment-1/master/recent_grads.csv"


# Use pandas to read in recent_grads.csv
recent_grads = pd.read_csv(recent_grade_url, sep=',')

# Print Exercise 1
print('Section 1, Exercise 1')

# Print the shape
print(recent_grads.shape)

###Exercise 2###

# Print Exercise 2
print('Section 1, Exercise 2')

# Print .dtypes
print(recent_grads.dtypes)

# Output summary statistics
print(recent_grads.describe())

# Exclude data of type object
print(recent_grads.describe(exclude=["object"]))

###Exercise 3###

# Import numpy
import numpy as np

# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']

# Print Exercise 3
print('Section 1, Exercise 3')

# Take a look at the dtypes
print(recent_grads[columns].dtypes)

# Find how missing values are represented
print(recent_grads["median"].unique())

# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan

###Exercise 4###
# Select sharewomen column
df = pd.DataFrame(recent_grads)
sw_col = df['sharewomen']

# Print Exercise 4
print('Section 1, Exercise 4')

# Output first five rows
print(sw_col.head(5))

###Exercise 5###
#import numpy need to be define at exercise 3

# Use max to output maximum values
max_sw = np.max(sw_col)

# Print Exercise 5
print('Section 1, Exercise 5')

# Print column max
print(max_sw)

###Exercise: Selecting a Row###
# Output the row containing the maximum percentage of women
print(recent_grads[sw_col == max_sw])

###Exercise 6###
# Convert to numpy array
recent_grads_np = recent_grads[["unemployed", "low_wage_jobs"]].values

# Print Exercise 6
print('Section 1, Exercise 6')

# Print the type of recent_grads_np
print(type(recent_grads_np))

###Exercise 7###

# Print Exercise 7
print('Section 1, Exercise 7')

# Calculate correlation matrix
print(np.corrcoef(recent_grads_np[:,0], recent_grads_np[:,1]))

####Section 2####
###Exercise 1###
# Add sharemen column
recent_grads['sharemen'] = recent_grads['men'] / recent_grads['total']

###Exercise 2###
# Find the maximum percentage value of men
max_men = np.max(recent_grads['sharemen'])

# Print Exercise 2
print('Section 2, Exercise 2')
 
# Output the row with the highest percentage of men
print(recent_grads[recent_grads['sharemen'] == max_men])

###Exercise 3###
# Add gender_diff column
recent_grads['gender_diff'] = recent_grads['sharewomen'] - recent_grads['sharemen']

###Exercise 4###
# Make all gender difference values positive
recent_grads['gender_diff'] = np.abs(recent_grads['gender_diff'])

# Print Exercise 3
print('Section 2, Exercise 4')

# Find the 5 rows with lowest gender rate difference
print(recent_grads.nsmallest(5, 'gender_diff'))

###Exercise 5###
# Rows where gender rate difference is greater than .30 
diff_30 = recent_grads['gender_diff'] > .30

# Rows with more men
more_men = recent_grads['sharemen'] > recent_grads['sharewomen']

# Combine more_men and diff_30
more_men_and_diff_30 = np.logical_and(more_men, diff_30)

# Find rows with more men and and gender rate difference greater than .30
fewer_women = recent_grads[more_men_and_diff_30]

###Exercise 6###

# Print Exercise 6
print('Section 2, Exercise 6')

# Group by major category and count
print(recent_grads.groupby(['major_category']).major_category.count())

###Exercise 7###

# Print Exercise 7
print('Section 2, Exercise 7')

# Group departments that have less women by category and count
print(fewer_women.groupby(['major_category']).major_category.count())

###Exercise 8###

# Print Exercise 8
print('Section 2, Exercise 8')

# Report average gender difference by major category
print(recent_grads.groupby(['major_category']).gender_diff.mean())

###Exercise 9###

# Print Exercise 9
print('Section 2, Exercise 9')

# Find average number of low wage jobs and unemployment rate of each major category
dept_stats = recent_grads.groupby(['major_category'])['low_wage_jobs', 'unemployment_rate'].mean()
print(dept_stats)

####Section 3####
###Exercise 1###

low_wage_jobs = recent_grads['low_wage_jobs']
unemployment_rate = recent_grads['unemployment_rate']

# Import matplotlib
import matplotlib.pyplot as plt

# Create scatter plot
plt.scatter(unemployment_rate, low_wage_jobs)

# Label x axis
plt.xlabel('Unemployment rate')

# Label y axis
plt.ylabel('Low pay jobs')

# Display the graph 
plt.show()

###Exercise 2###
# Plot the red and triangle shaped scatter plot  
plt.scatter(unemployment_rate, low_wage_jobs, color = "r", marker = "^")

# Display the visualization
plt.show()

###Exercise 3###
sharewomen = recent_grads['sharewomen']

# Plot a histogram of sharewomen
plt.hist(sharewomen)

# Show the plot
plt.show()

###Exercise 4###
# Import matplotlib and pandas
import matplotlib.pyplot as plt
import pandas as pd

# Create histogram
recent_grads.sharewomen.plot(kind='hist')
plt.show()

