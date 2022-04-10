
import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('temperature_history.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "History Temperature")
  
plt.xticks(rotation = 25)
plt.xlabel('Hora')
plt.ylabel('Temperature(°C)')
plt.title('Temperature History', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
