import os
file = "file.txt"

with open("file.txt", "r+") as f:
    
    newdata, newdata2 = [], []
    data = f.readlines()

    for line in data:
        if "a" in line:
            newdata.append(line)
        else:
            newdata2.append(line)
    
    
os.remove(file)
    
with open("file.txt", "w") as f:
    f.writelines(newdata2)
    
with open("newfile.txt", "w") as f2:
    f2.writelines(newdata)