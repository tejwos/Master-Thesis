import torch
import torch.nn as nn
import torch.nn.functional as F

class FocalLoss(nn.Module):
    def __init__(self, weight=None, size_average=True):
        super(FocalLoss, self).__init__()

    def forward(self, inputs, targets, alpha=0.8, gamma=2, smooth=1, classes = 2):

        if classes == 2:
            ### Using BC for Cases with 2 Classes
            # Use sigmoid() bevor for this step
            # 
            inputs = inputs.view(-1)
            targets = targets.view(-1)
            BCE = F.binary_cross_entropy(inputs, targets, reduction='mean')
        else:
            ### BCE for >2 Classes
            BCE = F.cross_entropy(inputs, targets, reduction='mean')
        BCE_EXP = torch.exp(-BCE)
        focal_loss = alpha * (1-BCE_EXP)**gamma * BCE
                       
        return focal_loss