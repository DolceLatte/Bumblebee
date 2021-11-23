import mlflow
import pandas as pd
from torchvision import datasets
import numpy
import torch
import pytorch_lightning as pl

import requests
from io import BytesIO
from werkzeug.exceptions import BadRequest
from PIL import Image
from flask import jsonify

URL = 'url'
CLASS = 'class'
CODE = 'code'
MESSAGE = 'message'
DATA = 'data'
model = None

class LightningMNISTClassifier(pl.LightningModule):
    def __init__(self, **kwargs):
        """
        Initializes the network
        """
        super(LightningMNISTClassifier, self).__init__()

        # mnist images are (1, 28, 28) (channels, width, height)
        self.optimizer = None
        self.scheduler = None
        self.layer_1 = torch.nn.Linear(28 * 28, 128)
        self.layer_2 = torch.nn.Linear(128, 256)
        self.layer_3 = torch.nn.Linear(256, 10)
        self.args = kwargs

    def forward(self, x):
        """
        :param x: Input data
        :return: output - mnist digit label for the input image
        """
        #batch_size = x.size()[0]
        batch_size = 1
        # (b, 1, 28, 28) -> (b, 1*28*28)
        x = x.view(batch_size, -1)
        # layer 1 (b, 1*28*28) -> (b, 128)
        x = self.layer_1(x)
        x = torch.relu(x)
        # layer 2 (b, 128) -> (b, 256)
        x = self.layer_2(x)
        x = torch.relu(x)
        # layer 3 (b, 256) -> (b, 10)
        x = self.layer_3(x)
        # probability distribution over labels
        x = torch.log_softmax(x, dim=1)

        return x

def predict_interface(url):
    global model

    # Model load which only happens during cold starts
    if model is None:
        model = LightningMNISTClassifier()
        loaded_model = model.load_from_checkpoint("epoch=3-step=3439.ckpt")

    response = requests.get(url)
    pix = Image.open(BytesIO(response.content))
    numpy.array(pix).reshape(-1, 784)
    input_np = torch.tensor(numpy.array(pix).reshape(-1, 784),dtype=torch.float32)
    predictions = loaded_model.forward(input_np)
    predicted_class = numpy.argmax(predictions.detach().numpy())

    print(predicted_class)

    return predicted_class

def predict(request):
    parameters = [
        URL,
    ]
    if request.get_json():
        json_request = request.get_json()
        for parameter in parameters:
            if not json_request.get(parameter) is None:
                continue
            raise BadRequest('invalid request parameter: %s' % parameter)

        url = json_request.get(URL)

    else:
        raise BadRequest('invalid arguments error')

    predicted_class = predict_interface(url)

    data = {
        CLASS: predicted_class,
    }

    res = {
        CODE: 200,
        MESSAGE: 'OK',
        DATA: data,
    }
    return jsonify(res)

if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/DolceLatte/Bumblebee/main/2019_AI_Engineer_Party/digit_7.jpg"
    predict_interface(url)