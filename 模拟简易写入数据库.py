#coding = gbk

f = open('d:\\1.txt', 'w')
f.write('name'+'\tsex'+'\ttele'+'\t\taddress'+'\n')

flag = 1

while flag == 1:
    name = input("Please input name:")
    sex = input("Please input sex:")
    tele = input("Please input tele:")
    address = input("Please input address:")
    s = name + '\t' + sex + '\t' + tele + '\t' + address + '\n'
    f.write(s)
    flag = int(input("Please input flag:"))
f.close()
