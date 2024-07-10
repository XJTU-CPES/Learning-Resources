"""
Here are a list of different reinforcement learning algorithms.
"""
import random
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import matplotlib.pyplot as plt


##############################################    DDPG    ###########################################################

class PolicyNet(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim, action_dim, action_bound, scaled_action_indices):
        super(PolicyNet, self).__init__()

        self.fc1 = torch.nn.Linear(state_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, action_dim)
        self.action_bound = action_bound                    # action_bound是环境可以接受的动作最大值
        self.scaled_action_indices = scaled_action_indices



    def forward(self, x):    ### x表示状态
        x = F.relu(self.fc1(x))
        a = torch.sigmoid(self.fc2(x)) * self.action_bound
        # a = torch.tanh(self.fc2(x)) * self.action_bound
        for idx in self.scaled_action_indices:
            a[:, idx] = a[:, idx] * 2 - 1
        return a         
    

class QValueNet(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim, action_dim):
        super(QValueNet, self).__init__()
     
        self.fc1 = torch.nn.Linear(state_dim + action_dim, 2*hidden_dim)
        self.fc2 = torch.nn.Linear(2*hidden_dim, 2*hidden_dim)
        self.fc_out = torch.nn.Linear(2*hidden_dim, 1)


    def forward(self, x, a):
        cat = torch.cat([x, a], dim=1) # 拼接状态和动作
        cat = cat.to( self.fc1.weight.dtype )
        x = F.relu(self.fc1(cat))
        x = F.relu(self.fc2(x))
        return self.fc_out(x)




##############################################    PPO       #########################################################



class PolicyNetContinuous(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim, action_dim):
        super(PolicyNetContinuous, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim)
        self.fc_mu = torch.nn.Linear(hidden_dim, action_dim)
        self.fc_std = torch.nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        mu = 2.0 * torch.tanh(self.fc_mu(x))
        std = F.softplus(self.fc_std(x))
        return mu, std

class ValueNet(torch.nn.Module):
    def __init__(self, state_dim, hidden_dim):
        super(ValueNet, self).__init__()
        self.fc1 = torch.nn.Linear(state_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)