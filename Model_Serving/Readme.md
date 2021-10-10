# Model_Serving

## Network Exchange tool 
### ONNX
pytorch, tensorflow 등 다양한 딥러닝 프레임워크가 있음, 이를 통해 모델을 구축할 수 있음 <br/>
학습된 모델을 가져다가 내가 잘 쓰는 프레임워크로 구현하려면 구현된 모델의 표준이 필요함 
  - ONNX는 중간언어를 통해 구현되는 프레임워크 간의 인터페이스...?라고 생각함
  
### ONNX tutorial 
[https://github.com/onnx/onnx](https://github.com/onnx/onnx) 여기에 너무 잘 나와있어서 정리가 따로 필요없는 듯

### ONNX example : Pytorch2ONNX
- 예제에 사용된 모델은 사진이 타코인지, 브리또인지 분류하는 모델 <br/>
![360](https://user-images.githubusercontent.com/45285053/135749903-e6b7fb9c-96cc-4aea-950b-5c1b9752fd16.jpg)

- 아래와 같이 onnx 라이브러리의 export 함수를 통해 모델을 ONNX 포맷으로 변형가능 <br/>

```python
import torch.onnx
torch.onnx.export(model,               # 실행될 모델
                  data,                         # 모델 입력값 (튜플 또는 여러 입력값들도 가능)
                  "model.onnx",   # 모델 저장 경로 (파일 또는 파일과 유사한 객체 모두 가능)
                  export_params=True,        # 모델 파일 안에 학습된 모델 가중치를 저장할지의 여부
                  ##opset_version=10,          # 모델을 변환할 때 사용할 ONNX 버전
                  do_constant_folding=True,  # 최적화시 상수폴딩을 사용할지의 여부
                  input_names = ['input'],   # 모델의 입력값을 가리키는 이름
                  output_names = ['output'], # 모델의 출력값을 가리키는 이름
                  )
```

- 입력 데이터의 shape를 함께 넘겨주어 모델 입력 값을 정해줘야하나 보다 <br/>
- 모델을 변환하고 나면 반드시 모델이 잘 변환되었는지를 아래와 같이 확인해야 함 <br/>

<img width="1094" alt="스크린샷 2021-10-03 오후 7 30 43" src="https://user-images.githubusercontent.com/45285053/135749783-2f8c64af-f9e2-4dca-9797-1aa34b4b4dc5.png">
<br/>


## Model registry 
### MLflow
원래는 pytorch ignite를 사용했는데, mlflow는 pytorch_lightning과 연동해서 사용해야 하는 듯 하다.<br/>

### pytorch_lightning
pytorch_lightning은 pytorch에 대한 인터페이스를 지원하는 파이썬 API
- Model checkpointing
- Early stopping
- etc..

다양한 인터페이스를 통해 머신러닝 개발에 도움을 줌<br/>
+ mlflow와 자동으로 연동되어 모델 학습, 결과, 서빙에 활용가능<br/>

[https://www.mlflow.org/docs/latest/python_api/mlflow.pytorch.html](https://www.mlflow.org/docs/latest/python_api/mlflow.pytorch.html)<br/>
잘된다고 하니.. 일단 모델을 학습시키고 레지스트리를 확인해보자, 모델을 pytorch_lightning API를 통해서 학습시키면, 자동으로 log가 mlflow에 남는다. 

```python
class CNNClassifier_custom(pl.LightningModule):
    def __init__(self,input_channel):
        pass

    def forward(self, x):
        out = self.conv_module(x)
        out = torch.flatten(out, 1)
        y = self.generator(out)
        #y = self.activation(y)
        return y

    def configure_optimizers(self):
        learning_rate = 1e-5
        optimizer = torch.optim.Adam(self.parameters(), lr= learning_rate)
        return optimizer

    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        out = self(x)
        loss = F.cross_entropy(out, y)
        # Use the current of PyTorch logger
        self.log("train_loss", loss, on_epoch=True)
        return loss

    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        out = self(x)
        loss = F.cross_entropy(out, y)
        preds = torch.argmax(out,dim=1)
        acc = accuracy(preds,y)
        # Use the current of PyTorch logger
        self.log("val_loss", loss, on_epoch=True)
        self.log("acc", acc, on_epoch=True)
        return loss
```

위와 같이 작성해주고 <br/>

```python
    trainer = pl.Trainer(gpus=1,max_epochs=2)
    mlflow.pytorch.autolog()
    with mlflow.start_run() as run:
        trainer.fit(cnn, train_dataloader=trn_loader, val_dataloaders=val_loader)

    print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))

    with mlflow.start_run() as run:
        # Save PyTorch models to current working directory
        mlflow.pytorch.save_model(cnn, "model")

    for model_path in ["model"]:
        model_uri = "{}/{}".format(os.getcwd(), model_path)
        loaded_model = mlflow.pytorch.load_model(model_uri)
        print(type(loaded_model))
```

main을 돌리면

```python
run_id: 87d864d55e79417b90cca1d58bed90d2
artifacts: ['model/MLmodel', 'model/conda.yaml', 'model/data', 'model/requirements.txt']
params: {'amsgrad': 'False', 'betas': '(0.9, 0.999)', 'epochs': '2', 'eps': '1e-08', 'lr': '1e-05', 'optimizer_name': 'Adam', 'weight_decay': '0'}
metrics: {'acc': 0.9411223530769348, 'train_loss': 0.24587100744247437, 'train_loss_epoch': 0.24587100744247437, 'train_loss_step': 0.16865096986293793, 'val_loss': 0.2339341789484024}
tags: {'Mode': 'training'}
```

이렇게 뜬다. mlflow ui를 통해 서버에 접속하면 내가 만든 모델에 대한 정보가 출력된다. 
![캡처](https://user-images.githubusercontent.com/45285053/136686979-2f4b7561-4f62-4c22-8374-d8d6a4effee1.PNG)
<br/>
실험에 들어가면 내가 구현한 모델이 들어가 있는데, 여기서 register를 통해 모델 버전 관리를 할 수 있다.

