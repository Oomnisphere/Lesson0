immutable_var="apple",2,True,[6,7,8]
print(immutable_var)
#immutable_var[0]=1 #ну и пучарм не дает в автозаполнении использовать .append, .expend
#print(immutable_var)
mutable_list=["apple",2,True,[6,7,8]]
print(mutable_list)
mutable_list[3]=6
mutable_list.append(False)
print(mutable_list)
mutable_list.extend('LoL')
mutable_list.reverse()
#mutable_list[3[2]]=6    #хотел к списку в списке обратиться что то не вышло. но думаю это уже не в формате задания.
print(mutable_list)