import torch
import torch.nn as nn

#CNN网络
class ASCADCNN(nn.Module):
    def __init__(self, num_classes=256, input_dim=700):
        super().__init__() 
        self.features = nn.Sequential(
            nn.Conv1d(1, 64, kernel_size=11, padding=5),
            nn.ReLU(inplace=True),
            nn.AvgPool1d(kernel_size=2, stride=2),
            
            nn.Conv1d(64, 128, kernel_size=11, padding=5),
            nn.ReLU(inplace=True),
            nn.AvgPool1d(kernel_size=2, stride=2),
            
            nn.Conv1d(128, 256, kernel_size=11, padding=5),
            nn.ReLU(inplace=True),
            nn.AvgPool1d(kernel_size=2, stride=2),
            
            nn.Conv1d(256, 512, kernel_size=11, padding=5),
            nn.ReLU(inplace=True),
            nn.AvgPool1d(kernel_size=2, stride=2),
            
            nn.Conv1d(512, 512, kernel_size=11, padding=5),
            nn.ReLU(inplace=True),
            nn.AvgPool1d(kernel_size=2, stride=2),
        )
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(512 * 21, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
    