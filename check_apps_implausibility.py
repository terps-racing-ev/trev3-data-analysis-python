import matplotlib.pyplot as plt
import os

from src.data_pair import DataPair
from src.data_file import DataFile


FILENAME = "csvs/rc_354.csv"

file = DataFile(FILENAME)

APPS1 = file.get_data_pair("APPS1_V")
APPS2 = file.get_data_pair("APPS2_V")

imp = file.get_data_pair("APPS_IMP")


APPS1_PCT = APPS1.perform_op_return_copy(lambda v: ((v - 1039) * 255) / (4400 - 1039), "APPS 1 Pct")

APPS2_PCT = APPS2.perform_op_return_copy(lambda v: ((v - 660) * 255) / (4016 - 660), "APPS 2 Pct")

diff = DataPair.merge_pairs(APPS1_PCT, APPS2_PCT, lambda o, t: abs(o - t), "Diff", "%")

DataPair.graph_multiple([[diff], [imp]], ['b'], ['-', '--'])

DataPair.graph_multiple([[APPS1_PCT, APPS2_PCT], [imp]], ['b', 'r'], ['-', ':', '--'])

plt.show()