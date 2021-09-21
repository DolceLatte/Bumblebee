# MLOps Machine Learning Pipeline

## 1. TensorFlow Data Validation [repo](https://github.com/tensorflow/data-validation)
TFDV(TensorFlow Data Validation)는 기계 학습 데이터를 탐색하고 검증하기 위한 라이브러리

[Source code](https://github.com/DolceLatte/Bumblebee/blob/main/MLOps_ML_Pipeline/TFDV.ipynb)
#### TFDV example : [택시 여행 데이터 세트](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew)
##### USAGE
**1. 훈련 및 테스트 데이터의 요약 통계에 대한 확장 가능한 계산**
- 교육 데이터 example
<img width="1400" alt="스크린샷 2021-09-21 오후 2 18 07" src="https://user-images.githubusercontent.com/45285053/134116002-d3a02ed4-57a1-4cd4-9330-e88e4fd4ae4b.png">
- 교육 데이터의 시각화

```python

train_stats = tfdv.generate_statistics_from_csv(data_location=TRAIN_DATA)
tfdv.visualize_statistics(train_stats)

```
<img width="692" alt="스크린샷 2021-09-21 오후 2 28 58" src="https://user-images.githubusercontent.com/45285053/134116324-61bb3a38-7819-458d-8fe2-24557a72032e.png">

**2. 데이터 셋의 스키마 추론과 평가, 환경을 구성하여 요구사항을 표현할 수 있음**
<br/>- TFDV를 통해 스키마의 도메인에 대한 제약조건을 정의 가능
![스크린샷 2021-09-21 오후 2 35 25](https://user-images.githubusercontent.com/45285053/134116778-3f11356f-6be9-4155-953f-7bbc2f5a4adc.png)

- 평가 데이터 오류 확인 : 훈련데이터와 평가데이터의 데이터 비교를 통해 vaildation을 수행
<img width="786" alt="스크린샷 2021-09-21 오후 2 47 33" src="https://user-images.githubusercontent.com/45285053/134118527-35a947b6-9f24-481a-9d6e-18f24beb691f.png">

- 평가 데이터 스키마의 이상을 수정하고 반영
<img width="1370" alt="스크린샷 2021-09-21 오후 2 56 40" src="https://user-images.githubusercontent.com/45285053/134119291-1c69ac74-8923-415b-b47c-77c4f867af63.png">

**3. 데이터 드리프트, 스큐 확인**
<br/>입력되는 데이터의 임계 : 드리프트
<br/>입력되는 데이터의 편향 정도: 스큐
1. 스키마 스큐 : 학습 및 평가 데이터가 동일한 스키마를 준수하지 않는 경우
2. 피쳐 스큐 : 모델이 훈련하는 피쳐 값이 평가 데이터의 피쳐 값과 다른 경우
3. 분포 스큐 : 학습 데이터 세트의 분포가 평가 데이터 세트의 분포와 다른 경우
- example
<img width="769" alt="스크린샷 2021-09-21 오후 3 08 27" src="https://user-images.githubusercontent.com/45285053/134120244-a0c52394-a7f3-4682-886c-8275d4d0af58.png">
데이터의 infinity_norm.threshold을 지정해 스큐에 대한 조정을 수행

## 2. What-if-tool [repo](https://github.com/PAIR-code/what-if-tool)
ML 모델을 쉽게 분석할 수 있는 Google의 오픈 소스 도구

#### [Source code]()
<img width="1367" alt="스크린샷 2021-09-21 오후 3 56 17" src="https://user-images.githubusercontent.com/45285053/134125379-d5839d1a-38cb-422f-baac-5e668a9d298d.png">
