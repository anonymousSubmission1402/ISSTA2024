
def find_largest_num(my_list):
    return max(my_list[5:7])
```
<Write a function called 'is_sorted' that takes one argument, a list of numbers, and returns True if the elements in the list are sorted in ascending order, False otherwise.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def is_sorted(my_list):
    return all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
```
<Write a function called 'find_duplicates' that takes one argument, a list of numbers, and returns the duplicates from the list.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def find_duplicates(my_list):
    return list(set([x for x in my_list if my_list.count(x) > 1]))
```
<Write a function called 'group_by_sign' that takes one argument, a list of numbers, and returns the elements from the list grouped by their sign (positive, negative or zero).> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def group_by_sign(my_list):
    return {'+': [x for x in my_list if x > 0], '-': [x for x in my_list if x < 0], '0': [x for x in my_list if x == 0]}
