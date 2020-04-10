
import numpy as np
from numpy import moveaxis
import torch
import torch.nn.functional as F
import torch.nn as nn                                                
import cv2
import argparse

classes = ["gastrula", "comma", "fold", "l1" ]


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, 3)
        self.pool = nn.MaxPool2d(5,5)

        self.pool2 = nn.MaxPool2d(3,3)
        self.dropout = nn.Dropout(p=0.5)
        self.conv2 = nn.Conv2d(10, 10, 3)
        self.conv3 = nn.Conv2d(10, 10, 3)
        
        self.fc1 = nn.Linear(150, 110)
        self.fc2 = nn.Linear(110, 100)
        self.fc3 = nn.Linear(100, 4)

    def forward(self, x):
        x = F.relu(self.pool(self.conv1(x)))
        x = F.relu(self.pool2(self.conv2(x)))
        x = F.relu(self.conv3(x))

        x = x.view(x.size(0), -1)
        
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = (self.fc3(x))      ## removed relu
        return x


class Net_2(nn.Module):
    def __init__(self):
        super(Net_2, self).__init__()
        self.conv1 = nn.Conv2d(1, 4, 5)
        self.pool = nn.MaxPool2d(3,3)
        self.dropout = nn.Dropout(p=0.5)
        self.conv2 = nn.Conv2d(4, 8, 5)

        self.fc1 = nn.Linear(704,200)
        self.fc2 = nn.Linear(200, 50)
        self.fc3 = nn.Linear(50, 20)

        self.fc4 = nn.Linear(20, 4)

    def forward(self, x):
        x = F.relu(self.pool(self.conv1(x)))
        x = F.relu(self.pool(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))

        x = (self.fc4(x))      ## removed relu
        return x


class MyEnsemble(nn.Module):
    def __init__(self, modelA, modelB):
        super(MyEnsemble, self).__init__()
        self.modelA = modelA
        self.modelB = modelB
        self.classifier = nn.Linear(8, 4)
        self.classifier2 = nn.Linear(4, 4)

    def forward(self, x1, x2):
        x1 = self.modelA(x1)
        x2 = self.modelB(x2)
        x = torch.cat((x1, x2), dim=1)
        x = self.classifier(F.relu(x))
        x = self.classifier2(F.relu(x))
        return x
    
cellnet_1 = Net()
cellnet_1.zero_grad()
cellnet_1.load_state_dict(torch.load("weights_c1.pth"))
cellnet_1.eval()

cellnet_2 = Net_2()
cellnet_2.zero_grad()
cellnet_2.load_state_dict(torch.load("weights_c2.pth"))
cellnet_2.eval()

model = MyEnsemble(cellnet_1, cellnet_2)
model.load_state_dict(torch.load("weights_combined.pth"))

model.eval()

def preprocess_image_for_model(img_path):
    im = cv2.imread(img_path, 0)
    im = cv2.resize(im, (120,90))
    input_tensor =  torch.from_numpy(im).unsqueeze(0).unsqueeze(0).float()
    return input_tensor


def result_to_prob_dist_percentage(output_tensor):
	prob_dist = torch.softmax(output_tensor.flatten(), dim = 0)
	index = torch.argmax(prob_dist).item()
	percentage = prob_dist[index]*100
	return index, percentage.item()

def pipeline(img_path, model):
    ten = preprocess_image_for_model(img_path)
    res = model(ten, ten)
    index, prob = result_to_prob_dist_percentage(res)

    print("\n  result = ", classes[index], " ", round(prob,3), "%")



def main ():

	parser = argparse.ArgumentParser(description='image path')
	parser.add_argument('indir', type=str, help='specify the image_path as <xyz>.png')
	args = parser.parse_args()

	pipeline(args.indir, model)

main()
