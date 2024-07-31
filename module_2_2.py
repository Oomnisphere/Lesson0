first=input('Первое число:')
second=input('Второе число:')
third=input('Третье число:')
if first==second==third:
    print('Бинго!!!')
elif first==second or second==third or first==third:
    print('Два из трёх!!')
else:
    print('Мимо')