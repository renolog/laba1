n = int(input())

if n % 2:
    if n <= 36:
        print("Ваше место - верхее, не боковое")
    elif (n > 36) and (n <= 54):
        print("Ваше место - верхее, боковое")
else:
    if n <= 36:
        print("Ваше место - нижнее, не боковое")
    elif (n > 36) and (n <= 54):
        print("Ваше место - нижнее, боковое")
