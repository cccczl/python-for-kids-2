# Write to a file 
filename = "C:\\temp\\myfile.txt"
with open(filename,"w") as f:
    f.write("Hello from code to write to a file.")


def readFile(filename):
    with open(filename,"r") as f:
        for line in f:     
            print(line)

filename = "C:\\temp\\myfile2.txt"
with open(filename, "w") as f:
    lines = ["Line1\n", "Line2\n", "Line3\n"]
    f.writelines(lines)
readFile(filename)


