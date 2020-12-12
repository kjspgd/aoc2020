#!/usr/local/bin/python3

#with open("input.txt", "a") as file:
#  file.write("\n")
#
#file.close()
results = []
for line in open("input.txt"):
    binary = line.rstrip().replace("F","0").replace("B","1").replace("L","0").replace("R","1")
    #print(str(binary))
    results.append((int(binary[0:7],2) * 8 + (int(binary[-3:],2))))
    #print(int(binary[-3:],2))
    print(str(int(binary[0:7],2)) + "," + str((int(binary[-3:],2))))
print(max(results))
