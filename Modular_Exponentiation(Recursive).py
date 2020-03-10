def mod_exp(base, power, mode):
    if power == 0:  #Zero power of zero is 1 that's why taking power as the first condition before base
        return 1
    if base == 0:
        return 0
    temp = mod_exp(base, power//2, mode)%mode
    if power & 1:
        return (temp*base*temp)%mode
    else:
        return (temp*temp)%mode
print(mod_exp(2, 5, 3))