# taken from https://pynative.com/python-list-exercise-with-solutions/#h-exercise-2-concatenate-two-lists-index-wise
# Exercise 1: Reverse a list in Python output ; [500, 400, 300, 200, 100]
list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

# Exercise 2: Concatenate two lists index-wise output ; ['My', 'name', 'is', 'Kelly']
list2 = ["M", "na", "i", "Ke"]
list3 = ["y", "me", "s", "lly"]

list4 = []
for i, j in zip(list2, list3):
    list4.append(i + j)
print(list4)

# Exercise 3: Turn every item of a list into its square output ; [1, 4, 9, 16, 25, 36, 49]
numbers = [1, 2, 3, 4, 5, 6, 7]
result = list(map(lambda x: x ** 2, numbers))
print(result)

#Exercise 4: Concatenate two lists in the following order output ; ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list5 = ["Hello ", "take "]
list6 = ["Dear", "Sir"]