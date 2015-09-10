
f = open('text.txt', 'a')

for i in range(0, 2):    
    print(i, end=' ')    
    f.write(str(i))
    
f.write("\n")
f.close()


#with - as
''' with as it`s work '''
with open('text.txt', "a") as f:
    f.write("add line \n")
    

    

