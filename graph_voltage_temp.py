import matplotlib.pyplot as plt

from src.data_pair import DataPair
from src.data_file import DataFile



# import the file
rc_319 = DataFile("csvs/rc_319.csv")
rc_318 = DataFile("csvs/rc_318.csv")

# get voltage values from both
pack_voltage_319 = rc_319.get_data_pair("PackVoltage")
pack_voltage_318 = rc_318.get_data_pair("PackVoltage")

# get therm values from both
pack_temp_319 = rc_319.get_data_pair("ThermAvg")
pack_temp_318 = rc_318.get_data_pair("ThermAvg")

# set units because spreadsheet doesn't specify them
# units are just for labels
pack_voltage_318.set_y_unit("V")
pack_voltage_319.set_y_unit("V")
pack_temp_318.set_y_unit("deg C")
pack_temp_319.set_y_unit("deg C")

# graph all 4 in one 
DataPair.graph_multiple([[pack_voltage_318, pack_voltage_319], [pack_temp_318, pack_temp_319]], 
                        # 318 will be blue, 319 will be red
                        ['blue', 'red'], 
                        # voltage will be solid line, temp will be dotted line
                        ['-', ':'])

plt.show()
