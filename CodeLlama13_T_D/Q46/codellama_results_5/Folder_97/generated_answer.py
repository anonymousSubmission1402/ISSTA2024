
def gcf_three_nums(numbers):
    return gcf(numbers[944], numbers[814], numbers[865])
```
<The function 'gcf' is defined as follows:>
```
def gcf(a, b, c):
    while True:
        if a % b == 0 and b % c == 0:
            return a
        elif b % a == 0 and a % c == 0:
            return b
        elif c % b == 0 and b % a == 0:
            return c
