from DataProcessing import Preprocessor, Trial, Subject
import pandas as pd
import numpy as np
import os
import re
import attr
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, hilbert

if __name__ == "__main__":
    a = Subject('../1', r'C:\Users\meyra\Desktop\s')
    a.create_total_df()
    lt = a.stimuli_df('square_left')
    idx = lt.index()
    print(idx.max)
    #block_amount = max(lt.loc['Block'])
    #print(block_amount)    