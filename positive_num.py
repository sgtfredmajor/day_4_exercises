# Build a code to determine and print positive numbers in a list
numbers = [10, 20, 0, 17, 25, 30]
print("The original numbers list: ", numbers)
# lamda function is a single in-line function that does not have a sigle pupose 
new_numbers = list(filter(lambda x: x >0, numbers))
print("Positive numbers list: ", new_numbers)