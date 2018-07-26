coding = 'utf-8'

import os

file = os.listdir('d:\\video\\QQ音乐助手')
os.chdir('d:\\video\\QQ音乐助手')
for i in file:
    p = i.rfind('15')
    if p != -1:
        os.rename(i, i[0:p-1] + '.mp3')
print (file)