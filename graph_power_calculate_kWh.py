import matplotlib.pyplot as plt

from src.data_pair import DataPair
from src.data_file import DataFile


# import the file
rc_354 = DataFile("csvs/rc_354.csv")
rc_355 = DataFile("csvs/rc_355.csv")

pack_power_354 = rc_354.get_data_pair("PackPower")
pack_power_355 = rc_355.get_data_pair("PackPower")


DataPair.graph_multiple([[pack_power_354, pack_power_355]], ['blue', 'red'], ['--'])



print("kWh consumed: ")
print(pack_power_354.integrate() / (3.6 * 1000000))


print(pack_power_355.integrate() / (3.6 * 1000000))

plt.show()
