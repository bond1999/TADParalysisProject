import serial
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

try:
    arduino = serial.Serial("/port/name")
    """arduino.flushInput()"""
except:
    print('Wrong port!!')

lines=[]
data=[]
i=0

while i<6:
    lines[i]=(str(arduino.readline()))
    j+=1

for each in lines:
    for number in each.split()
        if (number.isdigit()):
            data.append(int(number)) 

"""print(lines)"""
"""print(data)"""
 
set1 = ('Analog Reading', 'Voltage Reading(mV)')
set2 = ('Resistance(ohms)', 'Conductance(ohms)', 'Force(N)')
range1 = numpy.arange(len(set1))
range2 = numpy.arange(len(set2))

y1 = [data[0],data[1]]
y2 = [data[2],data[3],data[4]]

fig = plt.figure(figsize=(10,10))
p1 = plt.subplot(211)
plt.bar(range1, y1, align='center', alpha=0.5)
plt.xticks(range1, set1)
plt.title('FSR Reading')

p2 = plt.subplot(212)
plt.bar(range2, y2, align='center', alpha=0.5)
plt.xticks(range2, set2)

def animate(i):
    j=0
    while j<6:
    lines[j]=(str(arduino.readline()))
    j+=1

    k=0
    for each in lines:
        for number in each.split()
            if len(number)>1:
                if (number.isdigit()):
                    data[k]=(int(number))
                    k+=1

    y1 = [data[0],data[1]]
    y2 = [data[2],data[3],data[4]]
    
    ax1.clear()
    ax1.bar(range1, y1, align='center', alpha=0.5)
    ax2.clear()
    ax2.bar(range2, y2, align='center', alpha=0.5)
    
ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()

"""To write data to file-

def clean(L):#L is a list
    newl=[]#initialising the new list
    for i in range(len(L)):
        temp=L[i][2:]
        newl.append(temp[:-5])
    return newl
    
cleandata=clean(rawdata)

def write(L):
    file=open("data.txt",mode='w')
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()

write(cleandata)
"""
