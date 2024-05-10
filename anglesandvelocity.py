import matplotlib.pyplot as plt
velocity = []
timevector = []
fileread = open('DataXIVE.txt', 'r')
line1 = fileread.readline()
line2 = fileread.readline()
line = fileread.readline()
while line != '':
    trozos = line.split('|')
    ias = abs(float(trozos[11]) * 1.609)  # Si es de angles es trozos[37] cambiar el nombre tambien
    time = float(trozos[1])
    velocity.append(ias)
    timevector.append(time)
    line = fileread.readline()
fileread.close()


plt.plot(timevector, velocity)
plt.xlabel('Time of flight (in seconds)')
plt.ylabel("Variations of Indicated Air Speed")
plt.show()
