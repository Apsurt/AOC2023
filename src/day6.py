from utils import *
import numpy as np
import torch

time = 48989083
distance = 390110311121360
device = torch.device("mps")

holding_times = torch.arange(0, time+1, 1, device=device)
vs = holding_times
total_times_left = time - holding_times
distances = vs*total_times_left
answer = distances[distances>distance].size()[0]

print(answer)
#upload(answer)