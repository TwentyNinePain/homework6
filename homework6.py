my_dict = {'Максим': 19, 'Олег': 25, 'Дима': 40}
print(my_dict)
print(my_dict.get('Максим'))
print(my_dict.get('Вася'))
my_dict.update({'Никита': 17,
                'Гоша': 15})
print(my_dict)
a = my_dict.pop('Олег')
print(a)
print(my_dict)

my_set = {1, 2, 'Олег', 'Максим', 1, 2, 'Олег', 'Максим', 5, 6, 'Никита'}
print(my_set)
my_set.add(7)
my_set.add(9)
print(my_set)
my_set.discard(2)
print(my_set)