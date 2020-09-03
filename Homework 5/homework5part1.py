cipherText = "TEBKFKQEBZLROPBLCERJXKBSBKQP"

counter = 0.0
tCounter = 0.0
eCounter = 0.0
bCounter = 0.0
kCounter = 0.0
fCounter = 0.0
qCounter = 0.0
zCounter = 0.0
lCounter = 0.0
rCounter = 0.0
oCounter = 0.0
pCounter = 0.0
cCounter = 0.0
jCounter = 0.0
xCounter = 0.0
sCounter = 0.0

sum = 0

for letter in cipherText:
   counter += 1.0
   if letter == "T":
      tCounter += 1.0
   elif letter == "E":
      eCounter += 1.0
   elif letter == "B":
      bCounter += 1.0
   elif letter == "K":
      kCounter += 1.0
   elif letter == "F":
      fCounter += 1.0
   elif letter == "Q":
      qCounter += 1.0
   elif letter == "Z":
      zCounter += 1.0
   elif letter == "L":
      lCounter += 1.0
   elif letter == "R":
      rCounter += 1.0
   elif letter == "O":
      oCounter += 1.0
   elif letter == "P":
      pCounter += 1.0
   elif letter == "C":
      cCounter += 1.0
   elif letter == "J":
      jCounter += 1.0
   elif letter == "X":
      xCounter += 1.0
   elif letter == "S":
      sCounter += 1.0

tFrequency = tCounter/counter
eFrequency = eCounter/counter
bFrequency = bCounter/counter
kFrequency = kCounter/counter
fFrequency = fCounter/counter
qFrequency = qCounter/counter
zFrequency = zCounter/counter
lFrequency = lCounter/counter
rFrequency = rCounter/counter
oFrequency = oCounter/counter
pFrequency = pCounter/counter
cFrequency = cCounter/counter
jFrequency = jCounter/counter
xFrequency = xCounter/counter
sFrequency = sCounter/counter


textFrequency = []
textFrequency.append(0)
textFrequency.append(bFrequency)
textFrequency.append(cFrequency)
textFrequency.append(0)
textFrequency.append(eFrequency)
textFrequency.append(fFrequency)
textFrequency.append(0)
textFrequency.append(0)
textFrequency.append(0)
textFrequency.append(jFrequency)
textFrequency.append(kFrequency)
textFrequency.append(lFrequency)
textFrequency.append(0)
textFrequency.append(0)
textFrequency.append(oFrequency)
textFrequency.append(pFrequency)
textFrequency.append(qFrequency)
textFrequency.append(rFrequency)
textFrequency.append(sFrequency)
textFrequency.append(tFrequency)
textFrequency.append(0)
textFrequency.append(0)
textFrequency.append(0)
textFrequency.append(xFrequency)
textFrequency.append(0)
textFrequency.append(zFrequency)

'''
print("T: " + str(tCounter/counter))
print("E: " + str(eCounter/counter))
print("B: " + str(bCounter/counter))
print("K: " + str(kCounter/counter))
print("F: " + str(fCounter/counter))
print("Q: " + str(qCounter/counter))
print("Z: " + str(zCounter/counter))
print("L: " + str(lCounter/counter))
print("R: " + str(rCounter/counter))
print("O: " + str(oCounter/counter))
print("P: " + str(pCounter/counter))
print("C: " + str(cCounter/counter))
print("J: " + str(jCounter/counter))
print("X: " + str(xCounter/counter))
print("S: " + str(sCounter/counter))
'''

normalFrequency = []
normalFrequency.append(.080)
normalFrequency.append(.015)
normalFrequency.append(.030)
normalFrequency.append(.040)
normalFrequency.append(.130)
normalFrequency.append(.020)
normalFrequency.append(.015)
normalFrequency.append(.060)
normalFrequency.append(.065)
normalFrequency.append(.005)
normalFrequency.append(.005)
normalFrequency.append(.035)
normalFrequency.append(.030)
normalFrequency.append(.070)
normalFrequency.append(.080)
normalFrequency.append(.020)
normalFrequency.append(.002)
normalFrequency.append(.065)
normalFrequency.append(.060)
normalFrequency.append(.090)
normalFrequency.append(.030)
normalFrequency.append(.010)
normalFrequency.append(.015)
normalFrequency.append(.005)
normalFrequency.append(.020)
normalFrequency.append(.002)


for i in range(0,26):
   for j in range(0,26):
      index = j - i
      if index < 0:
         index += 26
      sum += textFrequency[j] * normalFrequency[index]
      j += 1
   print (str(i) + "\t" + "%.4f" % sum + "\n")
   sum = 0
   i += 1
