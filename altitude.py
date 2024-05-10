import matplotlib.pyplot as plt
altitudevector = []
timevector = []
fileread = open('DataXIVE.txt', 'r')
line1 = fileread.readline()
line2 = fileread.readline()
line = fileread.readline()
while line != '':
    trozos = line.split('|')
    altitude = float(trozos[51]) * 0.305
    time = float(trozos[1])
    altitudevector.append(altitude)
    timevector.append(time)
    line = fileread.readline()
fileread.close()


plt.plot(timevector, altitudevector)
plt.xlabel('Time of flight (in seconds)')
plt.ylabel("Variations of Altitude")
plt.show()
