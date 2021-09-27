# Bumblebee
## MLOps Tech Stack

- [Machine Learning Experiment Management](https://github.com/DolceLatte/Bumblebee/tree/main/Experiment%20Management)
  - Weights & Bias : Developer tools for machine learning
- [Machine Learning Pipeline](https://github.com/DolceLatte/Bumblebee/tree/main/MLOps_ML_Pipeline)
  - TensorFlow Data Validation : Data Vaildation tool in TFX
  - What if tool : Model understanding
- [Model Serving]()
  - Model Management
    - MLflow
    - BentoML
  - Example : [Model Serving using Flask](https://github.com/DolceLatte/Malware_Detector_w-CNN)
- [DevOps CI/CD in k8s](https://github.com/DolceLatte/Bumblebee/tree/main/DevOps)

## What is MLOps
- 간단하게 말하면 프로덕션 레벨로 머신러닝 프로젝트를 끌어올리는 과정
- 프로덕션 레벨에서 필요한 머신러닝 기술들을 파이프라인을 구현하여 기술 부채 해결, 모델 운영의 어려움을 해결
- [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)<br/>
관련 논문도 있다. 

#### Machine Learning Pipeline


[CI/CD 및 자동화된 ML 파이프라인](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- 머신러닝 모델의 관리를 위한 표준화된 프로세스 <br/>
- 파이프라인의 설계를 통해 생산성 향상, 성능에 대한 품질 관리, 장애 대응 능력 향상 등의 이점을 얻을 수 있음 

#### Challenge of Machine Learning
1. 빠른 데이터 변화
2. 모델 성능 저하로 인한 재학습
3. 모델 성능에 대한 직접적인 피드백이 어려움
4. 머신러닝 모델에 대한 검증

