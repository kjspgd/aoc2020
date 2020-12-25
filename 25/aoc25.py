#!/usr/local/bin/python3
def transform(incKey, subject=7):
    #print("subject" + str(subject))
    outgoingKey = (incKey*subject)%20201227
    return outgoingKey

def init():
   global keys
   for line in open("input.txt"):
      keys.append(int(line.rstrip()))

#samples
#doorPubkey = 17807724
#cardPubkey = 5764801
keys = []
init()
doorPubkey = keys[0]
cardPubkey = keys[1]
subject = 7
candidate = subject
solvedCard = 0
solvedDoor = 0
cardLoops = 0
doorLoops = 0
i=0
while True:
   candidate = transform(candidate)
   i=i+1
   #print(candidate)
   if solvedCard and solvedDoor: break
   else:
       if(candidate == cardPubkey):
           cardLoops = i+1
           print("The Card loops are " + str(cardLoops))
           solvedCard = 1
       if(candidate == doorPubkey):
           doorLoops = i+1
           print("The door loops are " + str(doorLoops))
           solvedDoor = 1

encKey1 = 0
doorEnc = 1
for i in range(0,cardLoops):
    doorEnc = transform(doorEnc,doorPubkey)
print("Door Encryption key: " + str(doorEnc))

cardSeed = 1
for i in range(0,doorLoops):
    cardSeed = transform(cardSeed,cardPubkey)
print("Card Encryption key: " + str(cardSeed))
