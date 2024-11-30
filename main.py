import matplotlib.pyplot as plt
import json

plt.plot()

with open('data.json') as f:
    measurements = json.load(f)

# print(measurements)

print(measurements[0]['mac'])
print(measurements[1]['mac'])

ia1 = measurements[0]['ia']#[1700:1900:]
ib1 = measurements[0]['ib']#[1700:1900:]
ic1 = measurements[0]['ic']#[1700:1900:]
ia2 = measurements[1]['ia']#[1700:1900:]
ib2 = measurements[1]['ib']#[1700:1900:]
ic2 = measurements[1]['ic']#[1700:1900:]
print(ia1)
print(ib1)
print(ic1)
print(ia2)
print(ib2)
print(ic2)

time = range(len(ia1))

# # Создание первого графика
# plt.subplot(2, 1, 1) # указываем 2 строки, 1 столбец, выбираем первое место
# plt.plot(time, ia1, 'y')
# plt.plot(time, ib1, 'g')
# plt.plot(time, ic1, 'r')
# plt.title('Токи с первой стороны линии')
#
# # Создание второго графика
# plt.subplot(2, 1, 2) # указываем 2 строки, 1 столбец, выбираем второе место
# plt.plot(time, ia2, 'y')
# plt.plot(time, ib2, 'g')
# plt.plot(time, ic2, 'r')
# plt.title('Токи со второй стороны линии')

# plt.plot(time, ia1, 'k.')
# plt.plot(time, ia2, 'r.')
plt.plot(time, ia1, 'k')
plt.plot(time, ia2, 'r')
plt.plot([time[0], time[len(time) - 1]], [0,0], 'k')

plt.show()

