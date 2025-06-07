import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# an x-y pair of data,
# usually time is x

class DataPair:

    def __init__(self, xlabel, ylabel, x, y, x_unit = "", y_unit = "", filename = ""):
        self.xlabel = xlabel
        self.ylabel = ylabel

        self.x = x
        self.y = y

        self.x_unit = x_unit
        self.y_unit = y_unit

        self.type = type

        self.filename = filename

    def set_x_unit(self, unit):
        self.x_unit = unit

    def set_y_unit(self, unit):
        self.y_unit = unit

    def set_y_label(self, label):
        self.ylabel = label
    
    def set_x_label(self, label):
        self.xlabel = label

    def set_filename(self, filename):
        self.filename = filename
    

    # draw this graph
    def graph(self):
        plt.plot(self.x, self.y)
        plt.xlabel(self.xlabel + "(" + self.x_unit + ")" + str(len(self.x)))
        plt.ylabel(self.ylabel + "(" + self.y_unit + ")")
        plt.figure()

    # perform a moving average on this data and return the result
    # period: number of data points considered in the moving average
    # new_y_name: name of new y axis
    def get_smoothed_version(self, period, new_y_name):
        i = 0

        d = []

        while i < len(self.y):
            right = 0
            left = 0

            if i + ((period - 1) / 2) < len(self.y):
                right = int(((period - 1) / 2))
            else :
                right = len(self.y) - (i + 1)


            if i - ((period - 1) / 2) >= 0:
                left = int(((period - 1) / 2))
            else:
                left = i

            d.append(sum(self.y[(i - left): (i + right) + 1]) / ((i + right) + 1 - (i - left)))

            i += 1


        ret = DataPair(self.xlabel, new_y_name, self.x.copy(), d, self.x_unit, self.y_unit, self.type)

        return ret

    # creates a new data pair out of two data pairs
    # the x column has to be the same thing but one can be less "complete" than
    # the other: i.e. if the two channels were logged at different rates
    # the specified operation is applied to the two y columns and the result is
    # the new y column
    def merge_pairs(pair_1, pair_2, operation, new_y_label, new_unit):
        i = 0
        j = 0

        x = []
        y = []

        
        while i < len(pair_1.x) and j < len(pair_2.x):
            if pair_1.x[i] > pair_2.x[j]:
                j += 1
            elif pair_1.x[i] < pair_2.x[j]:
                i += 1
            # find an entry where the x axis values are the same
            else:
                x.append(pair_1.x[i])
                # create a new y axis
                y.append(operation(pair_1.y[i], pair_2.y[j]))
                i += 1
                j += 1

        filename = pair_1.filename

        if pair_1.filename != pair_2.filename:
            filename += "/"
            filename += pair_2.filename

        return DataPair(pair_1.xlabel, new_y_label, x, y, pair_1.x_unit, new_unit, filename)
    
    # graphs multiple data pairs on the same graph, sharing the same x axis. 
    # the first parameter, axis_groups, should be a list of lists
    # grouping together DataPairs by y axes.
    # the label and unit of each y axis will be the same as the label and unit
    # of the first data pair in each list
    # the second parameter, colors, is a list of colors for the data
    # e.g ['red', 'blue'] will put the first data series in each
    # axis as red and the second as blue
    # type is either plot or scatter
    # the first axis will be
    def graph_multiple(axis_groups, colors, line_styles=None):
        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        if line_styles == None:
            line_styles = ['-'] * len(axis_groups)


        # draw data on the first y axis
        i = 0
        for dp in axis_groups[0]:
            ax.plot(dp.x, dp.y, colors[i], linestyle = line_styles[0], label = dp.ylabel + " (" + dp.filename + ") ")
            i += 1

        ax.set_xlabel(axis_groups[0][0].xlabel + "(" + (axis_groups[0][0].x_unit + ")"))
        ax.set_ylabel(axis_groups[0][0].ylabel + "(" + (axis_groups[0][0].y_unit + ")"))

        ax.legend()

        # if we have additional y axes
        if len(axis_groups) > 0:
            current_offset = 1

            j = 1

            for group in axis_groups[1:]:
                # create the new axis
                new_ax = ax.twinx()
                
                # set its position
                new_ax.spines.right.set_position(("axes", current_offset))

                # draw all the data on the axis
                i = 0
                for dp in group:
                    new_ax.plot(dp.x, dp.y, colors[i], linestyle = line_styles[j], label = dp.ylabel + " (" + dp.filename + ") ")
                    i += 1
                
                new_ax.set_xlabel(axis_groups[j][0].xlabel + "(" + (axis_groups[j][0].x_unit + ")"))
                new_ax.set_ylabel(axis_groups[j][0].ylabel + "(" + (axis_groups[j][0].y_unit + ")"))

                new_ax.legend()
                j += 1

                current_offset += 0.2
                
        plt.figure()
        
    # shift the x axis by x_shift units on the x axis
    def get_x_shifted_copy(self, x_shift):
        new_x = self.x.copy()

        i = 0

        while i < len(self.x):
            new_x[i] += x_shift
            i += 1
        
        return DataPair(self.xlabel, self.ylabel, new_x, self.y.copy(), self.x_unit, self.y_unit, self.filename)
    
    def get_zeroed_x_axis_copy(self):
        return self.get_x_shifted_copy(-1 * self.x[0])
    
    def integrate(self):
        sum = 0

        i = 1
        for val in self.y[1:]:
            sum += val * (self.x[i] - self.x[i - 1])
        
        return sum

    
