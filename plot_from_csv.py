import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('experiments/neuron_network/kz_abc/common.csv')

start_index = 180
end_index = 650
print(len(df[df.columns[1]]))

time = [i for i in df[df.columns[0]][start_index:end_index:1]]

ia1 = [i * 1000 for i in df[df.columns[1]][start_index:end_index:1]]
ib1 = [i * 1000 for i in df[df.columns[2]][start_index:end_index:1]]
ic1 = [i * 1000 for i in df[df.columns[3]][start_index:end_index:1]]

ia2 = [i * 1000 for i in df[df.columns[4]][start_index:end_index:1]]
ib2 = [i * 1000 for i in df[df.columns[5]][start_index:end_index:1]]
ic2 = [i * 1000 for i in df[df.columns[6]][start_index:end_index:1]]

flt = [i for i in df[df.columns[7]][start_index:end_index:1]]
rz = [i for i in df[df.columns[8]][start_index:end_index:1]]

print(time, '\n',
      ia1, '\n',
      ib1, '\n',
      ic1, '\n',
      ia2, '\n',
      ib2, '\n',
      ic2, '\n',
      flt, '\n',
      rz)

plt.figure(figsize=(14, 9))
plt.subplots_adjust(wspace=0.2, hspace=0.3, left=0.09, right=0.98, top=0.98, bottom=0.08)

plt.subplot(4, 1, 1)
plt.grid(True)
plt.ylabel("Ia, A")
plt.xlabel("time, s")
plt.plot(time, ia1, 'r')
plt.plot(time, ia2, 'k')
plt.legend(['first side current', 'second side current'], loc='upper right')

plt.subplot(4, 1, 2)
plt.grid(True)
plt.ylabel("Ib, A")
plt.xlabel("time, s")
plt.plot(time, ib1, 'r')
plt.plot(time, ib2, 'k')
plt.legend(['first side current', 'second side current'], loc='upper right')

plt.subplot(4, 1, 3)
plt.grid(True)
plt.ylabel("Ic, A")
plt.xlabel("time, s")
plt.plot(time, ic1, 'r')
plt.plot(time, ic2, 'k')
plt.legend(['first side current', 'second side current'], loc='upper right')

plt.subplot(4, 1, 4)
plt.grid(True)
plt.ylabel("Discrete commands")
plt.xlabel("time, s")
plt.plot(time, flt, 'r')
plt.plot(time, rz, 'k')
plt.legend(['fault command', 'rz command'], loc='upper right')

plt.show()