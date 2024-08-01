my_list = [42, 69, 322, 0, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while zero < len(my_list):
    number = my_list[zero]
    if number < 0:
        break
    if number == 0:
        zero += 1
        continue
    print(number)
    zero += 1