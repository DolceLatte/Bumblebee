# Bumblebee
쿠버네티스, MLOps 등등 관심있는 내용 정리한 레포
- bnm961126@gmail.com 

## Reference
###### 커뮤니티 돌아다니면 좋은 글이 많은 것 같다
- [MLOps KR](https://www.facebook.com/groups/748639598856641)
- [https://github.com/chris-chris](https://github.com/chris-chris)
- [k8skr](https://www.facebook.com/groups/k8skr)
- [인강 보고 정리함](https://www.inflearn.com/course/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4-%EC%8B%A4%EB%AC%B4#curriculum)
## MLOps Tech Stack

- [Machine Learning Experiment Management](https://github.com/DolceLatte/Bumblebee/tree/main/Experiment%20Management)
  - Weights & Bias : Developer tools for machine learning
- [Machine Learning Pipeline](https://github.com/DolceLatte/Bumblebee/tree/main/MLOps_ML_Pipeline)
  - TensorFlow Data Validation : Data Vaildation tool in TFX
  - What if tool : Model understanding
- [Model Serving]()
  - Network Exchange 
    - Open Neural Network Exchange [ONNX](https://github.com/onnx/onnx)
  - Model Management
    - BentoML
  - Example : [Model Serving using Flask](https://github.com/DolceLatte/Malware_Detector_w-CNN)
- [DevOps CI/CD in k8s](https://github.com/DolceLatte/Bumblebee/tree/main/DevOps)
## What is MLOps
- 간단하게 말하면 프로덕션 레벨로 머신러닝 프로젝트를 끌어올리는 과정
- 프로덕션 레벨에서 필요한 머신러닝 기술들을 파이프라인을 구현하여 기술 부채 해결, 모델 운영의 어려움을 해결
- [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)<br/>
관련 논문도 있다. 

#### Challenge of Machine Learning
1. 빠른 데이터 변화
2. 모델 성능 저하로 인한 재학습
3. 모델 성능에 대한 직접적인 피드백이 어려움
4. 머신러닝 모델에 대한 검증

**진화하는 데이터셋, 매트릭에 대한 대처와 머신러닝 모듈의 trigger point에 대한 구체적인 정의가 되어있는 파이프라인을 통해 문제를 해결해야함**

### Good example : CI/CD and automated ML pipelines 
![캡처](https://user-images.githubusercontent.com/45285053/134847379-676cb203-25c7-44d3-9946-b0a5f07e1935.JPG)
|:--:|
|<b>[ML Pipeline](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)</b>|

##### What is Pipeline?
- 머신러닝 모델의 관리를 위한 표준화된 프로세스 <br/>
- 파이프라인의 설계를 통해 생산성 향상, 성능에 대한 품질 관리, 장애 대응 능력 향상 등의 이점을 얻을 수 있음 

