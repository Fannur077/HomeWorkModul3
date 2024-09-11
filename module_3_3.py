def print_params(a = 2, b = 'строка', c = True):
    print(a, b, c)
print_params(3, 'str')
print_params( 10,None, False)
print_params(43)
print_params()
print_params(b=25)
print('Замена (b=25) работает')
print_params(c = [1,2,3])
print('Замена (c = [1,2,3]) работает')

values_list = [12, True, 'apple']
values_dict = {'a':98.98, 'b':"fruit", 'c':None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print('Добавление (*values_list_2, 42) работает')