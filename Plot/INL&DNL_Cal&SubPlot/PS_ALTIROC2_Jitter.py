#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import itertools
import os
from datetime import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def PS_ALTIROC2_Jitter(filename):
    outputbasedir = "../forTweppAbstract/"
    #filename = "PS_jitter&linearity"
    data = pd.read_csv(outputbasedir + filename + '.csv')

    data = data.sort_values(by=['PSdelay'])
    PSdelaySetting = data['PSdelay']
    PSdleay_40M = data['phasePSvsPLL_mean_40M']
    PSdleay_80M = data['phasePSvsPLL_mean_80M']
    PSdleay_640M = data['phasePSvsPLL_mean_640M']

   # fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    fig = plt.figure()

    ax1 = plt.subplot(211)
    plt.plot(PSdelaySetting[0:255], DNL)
    plt.tick_params('x', labelsize=6)
    plt.tick_params('x', labelbottom=False)
    plt.tick_params('y', labelsize=12)
    ax1.set_xticks(np.arange(0, 257, 32))
    ax1.set_yticks(np.arange(-1.0, 1.1, .5))
    ax1.set_xlabel('Delay setting', fontsize=12)
    ax1.set_ylabel('DNL [LSB]', fontsize=12)
    plt.grid()



    fig.savefig('PS_ALTIROC2_Linearity.png')

    plt.show()

    if __name__ == "__main__":

    PS_ALTIROC2_Linearity('PS_jitter&linearity')