#Stress testing is the technique which will be used when anyone get stuck in
#competitive programming especially by failing testcases.
#Hence, by using this technique you can know exactly what are the testcase patterns
#that are failing.
#So here is the step-by-step flow:
#1. First write the naive approach to the problem.
#2. Then write the efficient algorithm which you have worked on.
#3. Check if all edge cases satisfied.
#4. Apply thr Technique as given below.
#---------------------------------------------------------------------------------#
#So let's take an easy example so that we can understand it better. 
#Maximum-pairwise-product-problem
#here, the problem is to find the maximum product of a pair in an array.

import random
#The below method is a naive approach  for finding the maximum product of 2 elements
def maxpairproduct(array):
	maximum = float('-inf')
	for i in range(len(array)-1):
		for j in range(i+1,len(array)):
			if (array[i] * array[j]) > maximum:
				maximum = array[i] * array[j]
	return maximum

#The below method is an efficent approach with O(n) complexity, the idea is to find
#two maximum elements and return their product
def maxpairproductfast(array):
	maxelement1 = -1
	for i in range(len(array)):
		if maxelement1 == -1 or array[i] >= maxelement1 :
			maxelement1 = array[i]

	maxelement2 = -1
	for j in range(len(array)):
		if (maxelement2 == -1 or array[j] >= maxelement2) and array[j] != maxelement1:
			maxelement2 = array[j]
	return maxelement1 * maxelement2

#But eventually the above method does not pass all the testcases,
#here is the reason because if there are two same numbers which are maximum, but we
# are checking if both numbers should not be same here, that is the reason it won't give us the correct solution

#Hence try this code with the above method and see, those randomly generated testcases
#will help you to know the reason why the testcases doesn't pass.

#After that "remove the comments" of below code and test it, as it is the correct and efficient solution
#which doesn't fail any testcase because, we are noting down the indices of two maximum elements
# so that even though the numbers are repeating we get the right solution.

'''
def maxpairproductfast(array):
	index1 = -1
	for i in range(len(array)):
		if index1 == -1 or array[i] > array[index1] :
			index1 = i
	index2 = -1
	for j in range(len(array)):
		if index2 == -1 or array[j] > array[index2] :
			index2 = j
	return array[index1] * array[index2]
'''

while(True):
	n = random.randint(2,12)
	#Generating random length of array at each iteration
	print('Size of array =',n)
	array = []
	for i in range(n):
		#append random elements each time into the array range between 0-1000
		array.append(random.randint(0,1000))
	print('Random Array')
	print(*array)
	result_naive = maxpairproduct(array)
	result_efficient = maxpairproductfast(array)

	#As we know the standard naive approach always gives the correct answer hence,
	#we test that result with our efficient solution result, so that if they don't 
	#match then the efficient our approach is wrong and with the random generated integers
	#you can find what causes the error.

	if result_naive != result_efficient:
		print('---Wrong Solution---')
		print('result_naive = ',result_naive,end=" ")
		print('result_efficient = ',result_efficient)
		break
	else:
		print('Test passed')