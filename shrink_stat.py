import numpy as np

# Open npy file
tmp = np.load("statistics_small.npy", allow_pickle=True)
tmp = tmp[:10]
# Save the statistics over statsitics_small.npy
np.save("statistics_small.npy", tmp)