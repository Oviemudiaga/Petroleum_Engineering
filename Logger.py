import pandas as pd
import matplotlib.pyplot as plt
import lasio

class Logger():
    def __init__(self,well_name):
        self.well_name = well_name
        #self.no_axis = no_axis
        self.get_data()
        self.axes = []
        self.fig, self.ax1 = plt.subplots(figsize=(15, 10))
        self.ax = []

    def get_data(self):
        base_log = lasio.read('/Users/mudi/OneDrive/Codes/RE_WorkFold/Elcrest_Gbetiokun-6_LWD_Data \
@3490ft - 10337ft/Elcrest_Gbetiokun-6_LWD_12.25in_3450ft-10337ft_RT_Non_Interpolated.las')
        self.base_log = base_log
        self.base_log_frame = self.base_log.df()

    def get_axis(self,count = 1):
        self.fig, self.ax1 = plt.subplots(figsize=(15, 10))
        self.count = count
        list = [self.count]
        #axes = []
        while (self.count) > 0:
            self.axes.append('ax{}'.format(list[-1]))
            list.append(self.count-1)
            self.count = self.count -1
        # Set up the plot axes
        for self.ax in self.axes:
            for self.ax_no in range(len(self.axes)):
                self.ax = self.ax.append((plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).plot(self.base_log_frame["GR"], self.base_log_frame.index, color="green", linewidth=0.5))
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).set_xlabel("Gamma: GB_6")
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).xaxis.label.set_color("green")
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).set_xlim(0, 200)
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).set_ylabel("Depth (ft)")
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).tick_params(axis='x', colors="green")
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).spines["top"].set_edgecolor("green")
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).title.set_color('green')
                self.ax = (plt.subplot2grid((1, 4), (0, self.ax_no), rowspan=1, colspan=1)).set_xticks([0, 50, 100, 150, 200])
        print(self.ax)
        #self.fig.savefig('test1')

    def plot_gr(self):
        self.get_axis()
        # Gamma Ray track
        #for self.ax in self.axes:
        self.ax.set_ylim(9950, 9500)
        self.ax.grid(which='major', color='lightgrey', linestyle='-')
        self.ax.xaxis.set_ticks_position("top")
        self.ax.xaxis.set_label_position("top")
        self.fig.savefig('test1')

test = Logger('Gbet_6')

#print(test.plot_gr())
print(test.get_axis(count=1))