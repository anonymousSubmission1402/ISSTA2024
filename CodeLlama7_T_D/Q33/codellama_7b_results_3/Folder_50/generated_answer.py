
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 11
    end_index = 53
    filtered_list = []
    for i in range(start_index, end_index + 1):
        if string[i] in vowels and (string[i] > '+' or string[i] <= 'W'):
            filtered_list.append(string[i])
    return filtered_list
