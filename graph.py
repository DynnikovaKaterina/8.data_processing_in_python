import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

with open ('//home//b03-404//Desktop//7.lab_automated_measurements//settings.txt', 'r') as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print(tmp)

data_array = np.loadtxt("//home//b03-404//Desktop//7.lab_automated_measurements//data.txt", dtype = int)
U_capacitor = data_array / 255 * 3.3
T = 7.3689210414886475 #длительность эксперимента
n = 223 #количество измерений
t  = np.arange(0, T - T/n, T/n)
points = np.arange(0, n, 20)
t_U_max = U_capacitor.argmax()

#построение графика
fig, ax = plt.subplots(figsize = (16, 10), dpi = 100) #
ax.set_xlabel('время с начала эксперимента в секундах',fontsize = 10) #подпись к оси х
ax.set_ylabel('напряжение на конденсаторе в Вольтах',fontsize = 10) #подпись к оси у
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке')#подпись к графику

ax.xaxis.set_major_locator(ticker.MultipleLocator(2)) #частота крупных делений по х
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5)) #частота мелких делений по х
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.grid(which = 'major', color = 'k')#крупная сетка
ax.minorticks_on()
ax.grid(which = 'minor', color = 'grey')#мелкая сетка

#ax.legend('U(t)')
ax.plot(t, U_capacitor, label = "U(t)", marker = ".", markevery = points)
plt.figtext(0.4, 0.4,f"Время заряда = {round(t[t_U_max], 2)} с", fontsize = 8, color = 'blue')
plt.figtext(0.4, 0.3,f"Время разряда = {round(T - t[t_U_max], 2)} с", fontsize = 8, color = 'blue')
plt.xlim([0, 7.4]) #границы по х
plt.ylim([0, 3.3]) #границы по у
plt.show()
fig.savefig("/home//b03-404//Desktop//8.data_processing_in_python//U_capacitor(t).svg")
fig.savefig("/home//b03-404//Desktop//8.data_processing_in_python//U_capacitor(t).png")