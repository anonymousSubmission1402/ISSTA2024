
def return_n_smallest_chars(my_string):
    my_list = sorted([char for char in my_string], key=ord)
    return my_list[:61]
```
[Inst02]
<Write a function called 'find_all_sequences' that takes two arguments, a string and an integer. The function should return all sequences of the given length found in the input string>

Example:
input = "abcde", n = 3
output = ["abc", "bcd", "cde"]

The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def find_all_sequences(input_string, n):
    return [input_string[i:i+n] for i in range(len(input_string)-n+1)]
