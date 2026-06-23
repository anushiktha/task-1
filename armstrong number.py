num = 111
num_str = str(num)
order = len(num_str)
total = 0
for digit in num_str:
    total += int(digit) ** order
    if num == total:
        print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is NOT an Armstrong number")
