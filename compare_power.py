import matplotlib.pyplot as plt

from src.data_pair import DataPair
from src.data_file import DataFile

# import the file
rc_319 = DataFile("rc_319.csv")
rc_318 = DataFile("rc_318.csv")

# get voltage values from both
pack_voltage_319 = rc_319.get_data_pair("PackVoltage")
pack_voltage_318 = rc_318.get_data_pair("PackVoltage")
pack_current_319 = rc_319.get_data_pair("PackCurrent")
pack_current_318 = rc_318.get_data_pair("PackCurrent")

# calculate power
# this function will work even if the two columns are logged at different rates
pack_power_318 = DataPair.merge_pairs(pack_voltage_318, pack_current_318, 
                                      # multiplication op
                                      lambda v, c: v * c,
                                      # new label
                                      "Power",
                                      # new unit (matters for label)
                                      "W")

pack_power_319 = DataPair.merge_pairs(pack_voltage_319, pack_current_319, 
                                      lambda v, c: v * c,
                                      "Power",
                                      "W")

# shift the x axis so they both start at 0
# (to overlay them instead of one after the other)
zeroed_318 = pack_power_318.get_zeroed_x_axis_copy()
zeroed_319 = pack_power_319.get_zeroed_x_axis_copy()

# graph both in one 
DataPair.graph_multiple([[zeroed_318, zeroed_319]], 
                        # 318 will be blue, 319 will be red
                        ['blue', 'red'])

print("318 and 319 kWh")
print(pack_power_318.integrate() / (3.6 * 1000000000))
print(pack_power_319.integrate() / (3.6 * 1000000000))
plt.show()
