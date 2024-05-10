fileread = open('DataXIVE.txt', 'r')
filewrite=open('GoogleEarth.txt','w')
line1 = fileread.readline()
line = fileread.readline()
line = fileread.readline()
while line != '':
    trozos = line.split('|')
    latitud = float(trozos[46])
    longitud = float(trozos[47])
    altitude = float(trozos[51]) * 0.305
    filewrite.write(str(longitud) + ',' + str(latitud) + ',' + str(altitude)+' ')
    line = fileread.readline()
filewrite.close()
fileread.close()

