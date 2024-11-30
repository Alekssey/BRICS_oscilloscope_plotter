from scapy.all import *
import matplotlib.pyplot as plt

# file_path = "dumpsRecording/regimes/dump1.pcapng"
# file_path = "dumpsRecording/regimes/kzDump1.pcapng"
# file_path = "dumpsRecording/regimes/kzDump2.pcapng"
# file_path = "dumpsRecording/regimes/normDump.pcapng"
# file_path = "dumpsRecording/receiveWithoutNotifying/dump2.pcapng" #screenshots from here
# file_path = ''
# file_path = "dumps_from_acer/records_witwout_algoritm/normal_regim_5_sec.pcapng"
# file_path = 'dumps_from_acer/records_with_algoritm/reseive_during_work.pcapng'
# file_path = 'ligth_model/norm_reg.pcapng'
# file_path = 'dumps_from_acer/records_witwout_algoritm/kz_ac.pcapng'
file_path = 'dumpsRecording/newDumps/wtf.pcapng'


oscilloscopes = dict()
mac1 = ''
mac2 = ''

try:
    packets = rdpcap(file_path)
    mac1 = packets[0].dst
    mac2 = packets[1].dst

    oscilloscopes[mac1] = [[], [], []]
    oscilloscopes[mac2] = [[], [], []]

    print('mac1: ', mac1, '\nmac2: ', mac2, '\ndict: ', oscilloscopes)
    for packet in packets:
        if packet.type != 35002 or packet.dst == "ff:ff:ff:ff:ff:ff":
            continue
        load_bytes = packet.payload.load
        oscilloscopes[packet.dst][0].append(int.from_bytes(load_bytes[49:53:], 'big', signed=True)/10000)
        oscilloscopes[packet.dst][1].append(int.from_bytes(load_bytes[57:61:], 'big', signed=True) / 10000)
        oscilloscopes[packet.dst][2].append(int.from_bytes(load_bytes[65:69:], 'big', signed=True) / 10000)

except FileNotFoundError:
    print("Error: PCAPNG file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

"""# Создание первого графика
time = range(len(oscilloscopes[mac1][0]))
plt.subplot(2, 1, 1)
plt.plot(time, oscilloscopes[mac1][0], 'y')
plt.plot(time, oscilloscopes[mac1][1], 'g')
plt.plot(time, oscilloscopes[mac1][2], 'r')
plt.title('Токи с первой стороны линии')

# Создание второго графика
time = range(len(oscilloscopes[mac2][0]))
plt.subplot(2, 1, 2)
plt.plot(time, oscilloscopes[mac2][0], 'y')
plt.plot(time, oscilloscopes[mac2][1], 'g')
plt.plot(time, oscilloscopes[mac2][2], 'r')
plt.title('Токи со второй стороны линии')"""

max_size = min(len(oscilloscopes[mac1][0]), len(oscilloscopes[mac2][0]))
time = range(max_size)
plt.plot(time, oscilloscopes[mac1][0][:max_size:], color='skyblue')
plt.plot(time, oscilloscopes[mac2][0][:max_size:], color='seagreen')
plt.plot([0, len(time) - 1], [0, 0], 'k')

plt.show()

