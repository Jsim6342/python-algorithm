a = input()
b = input()

a_list = list(a)
b_list = list(b)

com_unit = []
for x in a_list:
    if x in b_list:
        com_unit.append(x)
        b_list.remove(x)

a_len = len(a_list) - len(com_unit)
b_len = len(b_list)

if a_len >= b_len:
    print(a_len)
else:
    print(b_len)