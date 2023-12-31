
def identical_elements(list1, list2):
    return {x for x in list1 if x in list2}
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_unique' that takes one argument, a string, and returns True if all characters in the string are unique, and False otherwise.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_unique(s):
    return len(set(s)) == len(s)
