File = open("file reading\hello.txt", "r")
f= File.readlines()
print(f)

newlist = []
for line in f:
    if line[-1] == '\n':
        newlist.append(line[:-1])  #removing the /n from the end of the list of above file contents
    else:
        newlist.append(line)
print(newlist)
File.close()