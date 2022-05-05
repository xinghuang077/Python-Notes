#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import itertools
import os
from datetime import time
import numpy as np
import pandas as pd
from statistics import mean
from matplotlib import pyplot as plt

#https://www.maximintegrated.com/en/design/technical-documents/tutorials/2/283.html#:~:text=INL%20%3D%20%7C%20%5B(VD%20%2D,Figure%201b.

def PS_ALTIROC2_Linearity(filename):
    outputbasedir = "../From_Maxime/forTweppAbstract/"
    #filename = "PS_jitter&linearity"
    data = pd.read_csv(outputbasedir + filename + '.csv')

    data = data.sort_values(by=['PSdelay'])
    PSdelaySetting = data['PSdelay']
    PSdleay_40M = data['phasePSvsPLL_mean_40M']
    PSdleay_80M = data['phasePSvsPLL_mean_80M']
    PSdleay_640M = data['phasePSvsPLL_mean_640M']

    deltaT_40M = []
    for i in PSdelaySetting[0:255]:
        deltaT_40M.append(PSdleay_40M[i+1] - PSdleay_40M[i])

    deltaT_40M[deltaT_40M.index(max(deltaT_40M))] = 0.165
    deltaT_40M[deltaT_40M.index(min(deltaT_40M))] = 0.095

#    deltaT_40M.sort()

    DNL = []
    for i in PSdelaySetting[0:255]:
        DNL.append(deltaT_40M[i]/0.09765625-1)

    DNLcal = []
    for i in range(len(DNL)):
        DNLcal.append(DNL[i] - 0.31)

    #SUM = 0
    INLsum = []
    #print(len(deltaT_40M))
    for i in range(255):
        SUM = 0
        # print(i)
        # print(deltaT_40M[0:i])
        for x in deltaT_40M[0:i]:
            SUM = SUM + x
            # print(SUM)
        INLsum.append(SUM)
    #print(INLsum)
    INL = []
    for i in range(len(INLsum)):
        INL.append((INLsum[i] - INLsum[0])/0.09765625-i)

    INLmean = mean(INL)
    print(INLmean)

    INLcal = []
    for i in range(len(INL)):
        INLcal.append(INL[i] + 0.64)

    # fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    fig = plt.figure() 

#    for PSclockSuffix in ["40M", "80M", "640M"]:
#        y = data['phasePSvsPLL_mean_' + PSclockSuffix]

    y1 = DNL
    y2 = DNL
    y3 = DNL
 
#     ax.plot(PSdelaySetting[0:255], DNL)
# #    ax.plot(PSdelaySetting, PSdleay_80M)
# #    ax.plot(PSdelaySetting, PSdleay_640M)
#     ax.set_xticks(np.arange(0, 257, 16))
#     ax.set_yticks(np.arange(-1.0, 1.1, .5))
#     plt.grid() # linestyle = '-.'
#     # Set tick font size
#     #for label in (ax.get_xticklabels() + ax.get_yticklabels()):
# 	#    label.set_fontsize(16)
#     #ax.set_title('Sine and cosine waves')
#     ax.set_xlabel('Delay setting', fontsize=16)
#     ax.set_ylabel('DNL [LSB]', fontsize=16)
#     fig.savefig('PS_ALTIROC2_Linearity.png')
#     plt.show()


    # yn = (y1,y2,y3)
    # COLORS = ('b','g','k')

    # for i,y in enumerate(yn):
    #     ax = fig.add_subplot(len(yn),1,i+1)

    #     ax.plot(PSdelaySetting[0:255], y, ls='solid', color=COLORS[i])
    #     plt.grid() 

    #     if i != len(yn) - 1:
    #         # all but last 
    #         ax.set_xticklabels( () )
    #     else:
    #         for tick in ax.xaxis.get_major_ticks():
    #             tick.label.set_fontsize(14) 
    #             # specify integer or one of preset strings, e.g.
    #             #tick.label.set_fontsize('x-small') 
    #             tick.label.set_rotation('vertical')

    # fig.suptitle('Matplotlib xticklabels Example')
    # ax.set_xticks(np.arange(0, 257, 16))
    # plt.show()


    ax1 = plt.subplot(211)
    plt.plot(PSdelaySetting[0:255], DNLcal)
    plt.tick_params('x', labelsize=6)
    plt.tick_params('x', labelbottom=False)
    plt.tick_params('y', labelsize=12)
    ax1.set_yticks(np.arange(-1, 1.1, .5))
    ax1.set_ylabel('DNL [LSB]', fontsize=12)
    plt.grid()

    # share x only
    ax2 = plt.subplot(212, sharex=ax1)
    plt.plot(PSdelaySetting[0:255], INLcal)
    # make these tick labels invisible
    plt.tick_params('x', labelbottom=True, labelsize=12)
    plt.tick_params('y', labelsize=12)
    ax2.set_yticks(np.arange(-1., 1.1, .5))
    ax2.set_ylabel('INL [LSB]', fontsize=12)
    plt.grid()

    # # share x and y
    # # ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
    # ax3 = plt.subplot(313, sharex=ax1)
    # plt.plot(PSdelaySetting[0:255], DNL)
    # #plt.xlim(0, 256)
    # ax3.set_xticks(np.arange(0, 257, 16))
    # plt.grid()

    ax2.set_xticks(np.arange(0, 257, 32))
    ax2.set_xlabel('Delay setting', fontsize=12)

    fig.savefig('PS_ALTIROC2_Linearity.png')

    plt.show()


if __name__ == "__main__":

    PS_ALTIROC2_Linearity('PS_jitter&linearity')