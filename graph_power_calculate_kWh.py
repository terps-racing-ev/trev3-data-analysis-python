import matplotlib.pyplot as plt

from src.data_pair import DataPair
from src.data_file import DataFile

FILENAME = "csvs/rc_354.csv"

# import the file
file = DataFile(FILENAME)

pack_power_channel = file.get_data_pair("PackPower")
pack_power_channel.set_y_unit("kWh")

pack_power_channel.graph()


ocv = file.get_data_pair("PackVoltage")
temp = file.get_data_pair("ThermAvg")

ocv.set_y_label("OCV")
ocv.set_y_unit("V")

temp.set_y_unit("deg C")


DataPair.graph_multiple([[ocv], [temp]], 
                        ['blue'], 
                        # voltage will be solid line, temp will be dotted line
                        ['-', ':'])


print("kWh consumed: ")
print(pack_power_channel.integrate() / (3.6 * 1000000))

plt.show()
