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

