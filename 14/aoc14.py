#!/usr/local/bin/python3


theLines = []
debug = 1

def eval(maskin, intin):
   calcedInt = 0
   global debug
   binIn = bin(intin)[2:].zfill(36)
   if debug: print(str(binIn) + " << Original" )
   if debug: print(str(maskin) + " << Mask")
   outbin = '' 
   for i in range(0,len(maskin)):
      if maskin[i] != 'X':
          outbin += maskin[i]
      else:
          outbin += binIn[i]
   if debug: print(str(outbin) + " << calced")
   calcedInt=int(outbin, 2)
   if debug: print(str(int(outbin, 2)))
   return calcedInt


def getnewregisterlist(maskin,registerin):
   newRegisters = []
   global debug
   binregIn = bin(registerin)[2:].zfill(36)
   outbin ='' 
   xCount = 0
   for i in range(0,len(maskin)):
      if 'X' in maskin[i]:
          outbin += 'k'
          xCount += 1
      elif int(maskin[i]) == 1:
          outbin += '1'
      elif int(maskin[i]) == 0:
          outbin += binregIn[i]
#   if debug: print(outbin)
#   if debug: print("There are " + str(xCount) + " xvals for a total combination count of " + str(2**xCount))
#   if debug: input("waithere")
   startingbin = outbin
   bini_iter = 0
   for i in range (0,2**xCount):
#      print("i is " + str(i))
      bini_iter = 0      
      newout = ''
      bini = str(bin(i)[2:].zfill(xCount))
      #print("processing " + bini)
      for i2 in range(0,len(startingbin)):
          if 'k' in startingbin[i2]: 
             #print("khit writing " + str(bini[bini_iter]))
             newout += bini[bini_iter]
             bini_iter += 1
          else: 
             newout += startingbin[i2]
#      print(newout + " " + str(int(newout,2)))
      newRegisters.append(newout)   
   print(newRegisters)    
   #if debug: input("Anotha?") 
   return newRegisters

for line in open("input.txt"):
   theLines.append((line.rstrip()))



#print(theLines)
lastMask = ''
registers = {}
for line in theLines:
   if 'mask =' in line:
      if debug: print("Here's a mask: " + line.split()[2])
      lastMask = line.split()[2]
   else:
      returnVal = 0
      register = int(line.split()[0][4:len(line.split()[0])-1])
      writeVal = int(line.split()[2])
      writableRegisters = []
      writeableRegisters = getnewregisterlist(lastMask, register)
      for reg in writeableRegisters:
          registers.update({reg:writeVal})
      #if debug: print("A register at " + register + " for " + line.split()[0] + " with an eval of " + str(evalNo))
      #returnVal = eval(lastMask, evalNo)
      #if debug: print("Write " + str(returnVal) + " at register " + str(register))
      #registers.update({register:returnVal})

if debug: print(registers)
if debug: print(len(registers))
if debug: print(len(theLines))
total = 0
for item in registers.values():
   total += item

print("The total is " + str(total))
