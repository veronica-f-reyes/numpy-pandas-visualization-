#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1, 2, 3])
a


# In[3]:


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix


# In[4]:


a[0]


# In[5]:


print('a    == {}'.format(a))
print('a[0] == {}'.format(a[0]))
print('a[1] == {}'.format(a[1]))
print('a[2] == {}'.format(a[2]))


# In[6]:


matrix[1, 1]


# In[7]:


should_include_elements = [True, False, True]
a[should_include_elements]


# In[8]:


original_array = np.array([1, 2, 3, 4, 5])
original_array + 1


# In[9]:


my_array = np.array([-3, 0, 3, 16])

print('my_array      == {}'.format(my_array))
print('my_array - 5  == {}'.format(my_array - 5))
print('my_array * 4  == {}'.format(my_array * 4))
print('my_array / 2  == {}'.format(my_array / 2))
print('my_array ** 2 == {}'.format(my_array ** 2))
print('my_array % 2  == {}'.format(my_array % 2))


# In[10]:


my_array = np.array([-3, 0, 3, 16])


# In[11]:


my_array[my_array > 0]


# In[12]:


my_array[my_array % 2 == 0]


# ## Numpy Exercises

#  1. How many negative numbers are there?

# In[134]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[138]:


print(a[a < 0])
print("Number of negative numbers: ", len(a[a < 0]))


# In[136]:


#Another approach
mask = a < 0
neg_nums = a[mask]
neg_nums.size


# 2. How many positive numbers are there?

# In[139]:


print(a[a > 0])
print("Number of positive numbers: ", len(a[a > 0]))


# In[137]:


#Another approach
mask = a > 0
pos_nums = a[mask]
pos_nums.size


# 3. How many even positive numbers are there?

# In[140]:


mask = (a > 0) & (a % 2 == 0)

print(a[mask])

print("Number of even positive numbers: ", len(a[mask]))


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[52]:


b = a + 3 

print(a)

print(b)

mask = b > 0

print(b[mask])

print("Number of positive numbers after adding 3: ", len(b[mask]))


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[141]:


sq = a ** 2
print(a)
print(sq)

m = sq.mean()
s_d = sq.std()

print("New mean is : ", m)
print("New standard deviation is: ", s_d)


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. 

# In[56]:


print(a)

m = a.mean()

centered = a - m

print("Mean of array a is : ", m)

print(centered)


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
#                 Z = (x − μ) / σ    ==    Z = (x - avg(x)) / std(x)
# 

# In[60]:


print(a)

m = a.mean()
s_d = a.std()

print("Mean is : ", m)
print("Standard deviation is: ", s_d)

z_score = (a - m) / s_d
print("\nZ score is: ", z_score)


# ## More Numpy Practice

# In[64]:


import numpy as np


# # Life w/o numpy to life with numpy
# 
# ### Setup 1

# In[68]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# ### Use python's built in functionality/operators to determine the following:
# 
# ### Exercise 1 
# Make a variable called sum_of_a to hold the sum of all the numbers in above list
# 
# 

# In[69]:


sum_of_a = a.sum()
print(sum_of_a)


# #### Exercise 2 
# Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# 
# 

# In[70]:


min_of_a = a.min()
print(min_of_a)


# ### Exercise 3
# Make a variable named max_of_a to hold the max number of all the numbers in the above list
# 
# 

# In[71]:


max_of_a = a.max()
print(max_of_a)


# ### Exercise 4
# Make a variable named mean_of_a to hold the average of all the numbers in the above list
# 
# 

# In[73]:


mean_of_a = a.mean()
print(mean_of_a)


# ### Exercise 5 
# Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
# 
# 

# In[76]:


product_of_a = a.prod()
print(product_of_a)


# 
# ### Exercise 6 
# Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
# 
# 

# In[80]:


squares_of_a = np.square(a)
print('a:', a)
print("a squared: ", squares_of_a)


# 
# ### Exercise 7 
# Make a variable named odds_in_a. It should hold only the odd numbers
# 
# 

# In[84]:


odds_in_a = a[a % 2 != 0]

print(a)
print(odds_in_a)


# ### Exercise 8
# Make a variable named evens_in_a. It should hold only the evens.

# In[86]:


evens_in_a = a[a % 2 == 0]

print(a)
print(evens_in_a)


# ## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# ### Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# b = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]

# In[87]:


b = np.array([[3, 4, 5], [6, 7, 8] ])


# ### Exercise 1 
# Refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

# In[88]:


sum_of_b = b.sum()
print(sum_of_b)


# ### Exercise 2 
# Refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

# In[89]:


min_of_b = b.min()
print(min_of_b)


# ### Exercise 3 
# Refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# In[90]:


max_of_b = b.max()
print(max_of_b)


# ### Exercise 4 
# Refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
# 
# 

# In[91]:


mean_of_b = b.mean()
print(mean_of_b)


# ### Exercise 5 
# Refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

# In[92]:


product_of_b = b.prod()
print(product_of_b)


# ### Exercise 6 
# Refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

# In[93]:


squares_of_b =  np.square(b)
print(squares_of_b)


# 
# ### Exercise 7 
# Refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

# In[95]:


odds_in_b = b[b % 2 != 0]

print(b)
print('\n',odds_in_b)


# ### Exercise 8
# Refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

# In[98]:


evens_in_b = b[b % 2 == 0]

print(b)
print('\n',evens_in_b)


#  ### Exercise 9 
# Print out the shape of the array b.

# In[99]:


print(b.shape)


# 
# ### Exercise 10 
# Transpose the array b.

# In[100]:


print(b, '\n')
print(b.transpose())


# ### Exercise 11 
# Reshape the array b to be a single list of 6 numbers. (1 x 6)

# In[101]:


print(b, '\n')
print(b.reshape(1,6))


# ### Exercise 12 
# Reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
# 
# 

# In[102]:


print(b, '\n')
print(b.reshape(6,1))


# 
# ## Setup 3
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# 
# ### HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# 
# 

# In[103]:


c = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])


# ### Exercise 1
# Find the min, max, sum, and product of c.

# In[105]:


min_of_c = c.min()
print(min_of_c)

max_of_c = c.max()
print('\n',max_of_c)

sum_of_c = c.sum()
print('\n',sum_of_c)


# ### Exercise 2 
# Determine the standard deviation of c.

# In[107]:


c_s_d = c.std()

print("Standard deviation is: ", c_s_d)


# ### Exercise 3 
# Determine the variance of c.

# In[109]:


c_var = c.var()

print("Variance is: ", c_var)


# ### Exercise 4 
# Print out the shape of the array c

# In[110]:


print(c.shape)


# ### Exercise 5 
# Transpose c and print out transposed result.

# In[111]:


print(c, '\n')
print(c.transpose())


# ### Exercise 6 
# Get the dot product of the array c with c. 
# 
# 

# In[114]:


dot = c * c
print(c)
print('\n', dot)


# ### Exercise 7
# Write the code necessary to sum up the result of c times c transposed. Answer should be 261
# 
# 

# In[119]:


c_transposed = c.transpose()
res = c * c_transposed
sum_c_and_ctransposed = res.sum() 
print(sum_c_and_ctransposed)


# ### Exercise 8
# Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
# 
# 
# 

# In[120]:


c_transposed = c.transpose()
res = c * c_transposed
prod_c_and_ctransposed = res.prod() 
print(prod_c_and_ctransposed)


# ## Setup 4
# d = [
#     [90, 30, 45, 0, 120, 180],
#     [45, -90, -30, 270, 90, 0],
#     [60, 45, -45, 90, -45, 180]
# ]
# 
# 

# In[121]:


d = np.array( [ [90, 30, 45, 0, 120, 180], [45, -90, -30, 270, 90, 0], [60, 45, -45, 90, -45, 180] ])


# ### Exercise 1 - Find the sine of all the numbers in d

# In[123]:


d_sin = np.sin(d)
print(d_sin)


# ### Exercise 2 
# Find the cosine of all the numbers in d

# In[124]:


d_cos = np.cos(d)
print(d_cos)


# ### Exercise 3
# Find the tangent of all the numbers in d

# In[125]:


d_tan = np.tan(d)
print(d_tan)


# ### Exercise 4 
# Find all the negative numbers in d

# In[129]:



print("Number of negative numbers: ", len(d[d < 0]))


# ### Exercise 5
# Find all the positive numbers in d

# In[130]:


print("Number of positive numbers: ", len(d[d > 0]))


# 
# ### Exercise 6 
# Return an array of only the unique numbers in d.

# In[131]:


d_unique = np.unique(d)
print(d_unique)


# ### Exercise 7 
# Determine how many unique numbers there are in d.

# In[132]:


d_unique = np.unique(d)
print(len(d_unique))


# ### Exercise 8 
# Print out the shape of d.

# In[126]:


print(d.shape)


# ### Exercise 9 
# Transpose and then print out the shape of d.

# In[127]:


print(d.transpose())
print(d.shape)


# ### Exercise 10 
# Reshape d into an array of 9 x 2

# In[128]:


print(d, '\n')
print(d.reshape(9,2))

