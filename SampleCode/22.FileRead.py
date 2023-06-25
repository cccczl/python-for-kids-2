filename = "C:\\temp\\myfile.txt"

with open(filename,"r") as f:
    line = f.read(100) #read 100 letters

#read multiple lines
# f=open(filename,"r")
# line = f.readline()
# while line != '':
#     print(line)
#     line = f.readline()

#better way to read all the line 
# for line in f:
#     print(line)
# f.close()
