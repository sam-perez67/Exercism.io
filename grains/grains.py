def square(number):
    if number < 1: 
        raise ValueError("square must be between 1 and 64")
    elif number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        grains = 2**(number - 1)
    return grains
    



def total():
    total = (2**64) - 1
    return total
