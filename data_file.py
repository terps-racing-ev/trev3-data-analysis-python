from data_pair import DataPair


# class encompassing all the data in a file
# holds a bunch of data pairs of time, <column>
class DataFile:
    def __init__(self, filename):
        self.data = {}
        self.import_file(filename)
        

    def get_data_pair(self, name):
        return self.data[name]

    def add_data_pair(self, pair):
        self.data[pair.y_label] = pair

    def import_file(self, filename):
        first_line = True
        column_heads = []
        for line in open(filename):
            if first_line:
                column_heads = line.split(",")

                # exclude the time column
                column_heads = column_heads[1:]

                i = 0

                while i < len(column_heads):
                    column_heads[i] = (column_heads[i].split("|")[0].replace("\"", ""), column_heads[i].split("|")[1].replace("\"", ""))
                    i += 1

                for c in column_heads:
                    self.data[c[0]] = DataPair("time", c[0], [], [], "ms", c[1], filename)

                first_line = False

            else:
                line_arr = line.split(",")

                time = int(line_arr[0])

                line_arr = line_arr[1:]

                i = 0

                while i < len(line_arr):
                    if line_arr[i] != "" and line_arr[i] != "\n":
                        self.data[column_heads[i][0]].x.append(time)
                        self.data[column_heads[i][0]].y.append(float(line_arr[i]))
                    i += 1




