import matplotlib.pyplot as plt
import numpy as np

with open ('settings.txt', 'r') as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print(tmp)

data_array = np.loadtxt("data.txt", dtype = int)