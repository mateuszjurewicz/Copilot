"""
Let's try to train a simple neural network on the mnist dataset.
"""

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# get mnist dataset
mnist_train = torchvision.datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)

# get train loader
train_loader = torch.utils.data.DataLoader(mnist_train, batch_size=64, shuffle=True)


# define a classifier network for MNIST
class Net(nn.Module):
    """
    Fully-connected classifier for MNIST.
    """

    # define the layers
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 10)

    # define the forward pass
    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# define the training function
def train(model, device, train_loader):
    """
    Train the model.
    """
    # define the loss function
    criterion = nn.CrossEntropyLoss()

    # define the optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # loop over the dataset
    for epoch in range(1, 20 + 1):
        # set the model to training mode
        model.train()

        # loop over the batches
        for batch_idx, (data, target) in enumerate(train_loader):
            # send the data to the device
            data, target = data.to(device), target.to(device)

            # zero the gradients
            optimizer.zero_grad()

            # forward pass
            output = model(data)

            # calculate the loss
            loss = criterion(output, target)

            # backward pass
            loss.backward()

            # update the parameters
            optimizer.step()

            # print the loss
            if batch_idx % 100 == 0:
                print('Loss: {}'.format(loss.item()))

    # return the model
    return model


if __name__ == '__main__':
    # define the device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # define the model
    model = Net()

    # send the model to the device
    model.to(device)

    # train the model
    model = train(model, device, train_loader)

    # save the model
    torch.save(model.state_dict(), 'model.pt')
