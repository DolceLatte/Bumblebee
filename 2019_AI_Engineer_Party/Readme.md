# 2019_AI_Engineer_Party

#### 옛날거지만, 한번 풀어보자

- Machine Learning Serving Pipeline 구축

<li>
요구사항1. Serverless API(Google Functions, Azure Functions, AWS Lambda)로 머신러닝 모델 CPU 서빙
</li>
<li>
요구사항2. 데이터셋은 Google BigQuery에 적재하고 꺼내서 사용
</li>
<li>
요구사항3. 학습 실험 관리 Opensource(Microsoft NNI, Google Adanet, Optuna 등)를 사용하여 AutoML 수행
</li>
<li>
요구사항4. 학습이 완료되면 Model Validation을 자동으로 수행해서 지금 서빙되고 있는 모델보다 우수한지 자동으로 검증
</li>
<li>
요구사항5. 모델리스트가 관리되어야 하고, 선택적으로 배포 및 롤백이 가능함
</li>
<li>
요구사항6. 모든 코드는 Pylint 가이드에 맞춰 깔끔함을 유지 (PEP8, Google Style 등)
</li>
서빙할 딥러닝 모델은 뭐든 상관없습니다. MNIST, 얼굴 인식, Object Detection
