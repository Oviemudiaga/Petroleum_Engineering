import pandas as pd
import matplotlib.pyplot as plt
import lasio

class Logger():
    def __init__(self,well_name, figures, top_depth, bottom_depth):
        self.well_name = well_name
        self.figures = figures
        self.top_depth = top_depth
        self.bottom_depth = bottom_depth
        self.get_data()
        self.axes = [] #to store the number of plot axis that will be print out
        self.fig, self.ax = plt.subplots(figsize=(15, 10))
        self.dict = {}

    def get_data(self):
        base_log = lasio.read('/Users/mudi/OneDrive/Codes/RE_WorkFold/Elcrest_Gbetiokun-6_LWD_Data @3490ft - 10337ft/\
Elcrest_Gbetiokun-6_LWD_12.25in_3450ft-10337ft_RT_Interpolated.las') #read the file into base_log
        self.base_log = base_log #call is self.base_log so it can be manipulated
        self.base_log_frame = self.base_log.df() #create dataframe

    def plot_axis(self):
        self.count = self.figures
        list = [self.count]
        while (self.count) > 0:
            self.axes.append('ax{}'.format(list[-1]))
            list.append(self.count-1)
            self.count = self.count -1
        # Set up the plot axes
        count = 0
        for self.ax in self.axes:
            self.dict[self.ax] = plt.subplot2grid((1, 3), (0, count), rowspan=1, colspan=1)
            count += 1

    def plot_gr(self):
        self.plot_axis()
        for ax in list(self.dict.values()):
            ax.plot(self.base_log_frame["GR"], self.base_log_frame.index, color="green", linewidth=0.5)
            ax.set_xlabel(self.well_name)
            ax.xaxis.label.set_color("green")
            ax.set_xlim(0, 200)
            ax.set_ylabel("Depth (ft)")
            ax.tick_params(axis='x', colors="green")
            ax.spines["top"].set_edgecolor("green")
            ax.title.set_color('green')
            #ax.set_xticks([0, 50, 100, 150, 200])
        self.fig.savefig('test1')

    def plot_gr_res(self):
        self.plot_axis()
        (ax,ay) = (list(self.dict.values())[0],list(self.dict.values())[1])
        # GR track
        ax.plot(self.base_log_frame["GR"], self.base_log_frame.index, color="green", linewidth=0.5)
        ax.set_xlabel("Gamma: {}".format(self.well_name))
        ax.xaxis.label.set_color("green")
        ax.set_xlim(0, 200)
        ax.set_ylabel("Depth (ft)")
        ax.tick_params(axis='x', colors="green")
        ax.spines["top"].set_edgecolor("green")
        ax.title.set_color('green')
        # ax.set_xticks([0, 50, 100, 150, 200])
        # Resistivity track
        ay.plot(self.base_log_frame["P40H"], self.base_log_frame.index, color="red", linewidth=0.5)
        ay.set_xlabel("Resistivity - Deep")
        ay.set_xlim(0.2, 2000)
        ay.xaxis.label.set_color("red")
        # ax2.spines["top"].set_position(("axes", 1.08))
        ay.tick_params(axis='x', colors="red")
        ay.spines["top"].set_edgecolor("red")
        #ax.set_xticks([0.1, 1, 10, 100, 1000])
        ay.semilogx()
        for i in (ax,ay):
            i.set_ylim(self.bottom_depth, self.top_depth)  # Change depth interval
            i.grid(which='major', color='lightgrey', linestyle='-')
            i.xaxis.set_ticks_position("top")
            i.xaxis.set_label_position("top")
        self.fig.savefig('Well_A')

test = Logger('Well_A',figures=2, bottom_depth=9700, top_depth=9000)
#print(test.plot_gr())
print(test.plot_gr_res())
