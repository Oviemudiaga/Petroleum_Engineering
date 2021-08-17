import pandas as pd
import matplotlib.pyplot as plt
import lasio

PC_well_6 = 'C:/Users/MSO/OneDrive/Codes/RE_WorkFold/Elcrest_Gbetiokun-6_LWD_Data @3490ft - 10337ft/Elcrest_Gbetiokun-6_LWD_12.25in_3450ft-10337ft_RT_Non_Interpolated.las'
Mac_well_6 = '/Users/mudi/OneDrive/Codes/RE_WorkFold/Elcrest_Gbetiokun-6_LWD_Data @3490ft - 10337ft/Elcrest_Gbetiokun-6_LWD_12.25in_3450ft-10337ft_RT_Interpolated.las'

PC_well_4 = 'C:/Users/MSO/OneDrive/Codes/RE_WorkFold/Offset Wells/Gbetiokun_4.las'
Mac_well_4 = '/Users/mudi/OneDrive/Codes/RE_WorkFold/Offset Wells/Gbetiokun_4.las'

PC_well_5 = 'C:/Users/MSO/OneDrive/Codes/RE_WorkFold/Offset Wells/Gbetiokun_5.las'
Mac_well_5 = '/Users/mudi/OneDrive/Codes/RE_WorkFold/Offset Wells/Gbetiokun_5.las'

#well logs import
las_6 = lasio.read(PC_well_6)
well_6 = las_6.df()
well_nan = well_6.notnull() * 1
#----------------------------------------------------
las_4 = lasio.read(PC_well_4)
well_4 = las_4.df()
well_nan4 = well_4.notnull() * 1
#----------------------------------------------------
las_5 = lasio.read(PC_well_5)
well_5 = las_5.df()
well_nan5 = well_5.notnull() * 1
#----------------------------------------------------
fig, ax = plt.subplots(figsize=(15, 10))
# Set up the plot axes
ax1 = plt.subplot2grid((1, 5), (0, 0), rowspan=1, colspan=1) #to make ax1 the first subplot that is on the left
ax2 = plt.subplot2grid((1, 5), (0, 1), rowspan=1, colspan=1, sharey=ax1) #the 1 here makes ax2 to be on the right side of ax1
ax3 = ax2.twiny()
ax4 = ax3.twiny()

# As our curve scales will be detached from the top of the track,
# this code adds the top border back in without dealing with splines

# Gamma Ray track
ax1.plot(well_6["GR"], well_6.index, color="green", linewidth=0.5)
ax1.set_xlabel("Gamma: GB_6")
ax1.xaxis.label.set_color("green")
ax1.set_xlim(0, 200)
ax1.set_ylabel("Depth (ft)")
ax1.tick_params(axis='x', colors="green")
ax1.spines["top"].set_edgecolor("green")
ax1.title.set_color('green')
ax1.set_xticks([0, 50, 100, 150, 200])

# Resistivity track
ax2.plot(well_6["P40H"], well_6.index, color="red", linewidth=0.5)
ax2.set_xlabel("Resistivity - Deep")
ax2.set_xlim(0.2, 2000)
ax2.xaxis.label.set_color("red")
#ax2.spines["top"].set_position(("axes", 1.08))
ax2.tick_params(axis='x', colors="red")
ax2.spines["top"].set_edgecolor("red")
ax2.set_xticks([0.1, 1, 10, 100, 1000])
ax2.semilogx()
# Resistivity track - Curve 2
ax3.plot(well_6["P28H"], well_6.index, color="green", linewidth=0.5)
ax3.set_xlabel("Resistivity - Med")
ax3.set_xlim(0.2, 2000)
ax3.xaxis.label.set_color("green")
#ax3.spines["top"].set_position(("axes", 1.08))
ax3.spines["top"].set_visible(True)
ax3.tick_params(axis='x', colors="green")
ax3.spines["top"].set_edgecolor("green")
ax3.set_xticks([0.1, 1, 10, 100, 1000])
ax3.semilogx()
# Resistivity track - Curve 3
ax4.plot(well_6["P16H"], well_6.index, color="yellow", linewidth=0.5)
ax4.set_xlabel("Resistivity - Small")
ax4.set_xlim(0.2, 2000)
ax4.xaxis.label.set_color("yellow")
#ax4.spines["top"].set_position(("axes", 1.16))
ax4.spines["top"].set_visible(True)
ax4.tick_params(axis='x', colors="yellow")
ax4.spines["top"].set_edgecolor("yellow")
ax4.set_xticks([0.1, 1, 10, 100, 1000])
ax4.semilogx()

# Common functions for setting up the plot can be extracted into
# a for loop. This saves repeating code.
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(9900, 9500) #Change depth interval
    ax.grid(which='major', color='lightgrey', linestyle='-')
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    #ax.spines["top"].set_position(("axes", 1.02))

for ax in [ax2, ax3, ax4]:
    plt.setp(ax.get_yticklabels(), visible=False)

plt.tight_layout()
fig.subplots_adjust(wspace=0.15)
plt.savefig('GR_Res.pdf')
