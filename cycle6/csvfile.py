f= open('D:\demo\csvfile.file','r')
f_contents=f.readlines()
list1=list(f_contents)
print(list1)
f.close()