#работа со словарями
my_dict={'Anton':'evel','Andrei':'good','Anna':'evel','Bob':['evel','good']}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Bil'))
my_dict.update({'Olga':'neutral','Gogi':'good'})
a=my_dict.pop('Andrei')
print(a)
print(my_dict)
#работа со множествами
my_set={1,2,3,4,5,6,66,5,4,44,4,3,2,'cool','false','ups',True,True,23.33,33.23}
print(my_set)
my_set.add('yohoho')
my_set.update(['sun',5])
print(my_set)
my_set.discard(44)
my_set.remove(1)
print(my_set)