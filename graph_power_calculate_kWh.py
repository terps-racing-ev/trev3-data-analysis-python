import matplotlib.pyplot as plt

from src.data_pair import DataPair
from src.data_file import DataFile

FILENAME = "csvs/rc_319.csv"

# import the file
file = DataFile(FILENAME)

# get voltage and current
pack_voltage = file.get_data_pair("PackVoltage")
pack_current = file.get_data_pair("PackCurrent")

# calculate power
# this function will work even if the two columns are logged at different rates
pack_power = DataPair.merge_pairs(pack_voltage, pack_current, 
                                      # multiplication op
                                      lambda v, c: v * c,
                                      # new label
                                      "Power",
                                      # new unit (matters for label)
                                      "W")

pack_power.graph()

print("kWh consumed: ")
print(pack_power.integrate() / (3.6 * 1000000000))

plt.show()
