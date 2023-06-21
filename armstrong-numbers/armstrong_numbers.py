def is_armstrong_number(number):
    num_str = str(number)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if number == sum:
        return True
    else:
        return False
