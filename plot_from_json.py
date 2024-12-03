import matplotlib.pyplot as plt
import json

start_index = 9500
end_index = 10000

with open('experiments/neuron_network/kz_ab/buffered_data.json') as f:
    measurements = json.load(f)

print(len(measurements[0]['ia']))
print(measurements[0]['mac'])
print(measurements[1]['mac'])

ia1 = [i / 10 for i in measurements[0]['ia'][start_index:end_index:1]]
ib1 = [i / 10 for i in measurements[0]['ib'][start_index:end_index:1]]
ic1 = [i / 10 for i in measurements[0]['ic'][start_index:end_index:1]]
ia2 = [i / 10 for i in measurements[1]['ia'][start_index:end_index:1]]
ib2 = [i / 10 for i in measurements[1]['ib'][start_index:end_index:1]]
ic2 = [i / 10 for i in measurements[1]['ic'][start_index:end_index:1]]

time = range(end_index - start_index)

print(time, '\n', ia1, '\n', ib1, '\n', ic1, '\n', ia2, '\n', ib2, '\n', ic2)

plt.figure(figsize=(14, 9))
plt.subplots_adjust(wspace=0.2, hspace=0.3, left=0.09, right=0.98, top=0.98, bottom=0.08)

plt.subplot(4, 1, 1)
plt.grid(True)
plt.ylabel("Ia, A")
plt.xlabel("point number")
plt.plot(time, ia1, 'r')
plt.plot(time, ia2, 'k')
plt.legend(['first side current', 'second side current'], loc='upper right')

plt.subplot(4, 1, 2)
plt.grid(True)
plt.ylabel("Ib, A")
plt.xlabel("point number")
plt.plot(time, ib1, 'r')
plt.plot(time, ib2, 'k')
plt.legend(['first side current', 'second side current'], loc='upper right')

plt.subplot(4, 1, 3)
plt.grid(True)
plt.ylabel("Ic, A")
plt.xlabel("point number")
plt.plot(time, ic1, 'r')
plt.plot(time, ic2, 'k')
plt.legend(['first side current', 'second side current'], loc='upper right')

plt.show()