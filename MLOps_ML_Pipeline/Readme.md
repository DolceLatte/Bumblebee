# MLOps Machine Learning Pipeline

## 1. TensorFlow Data Validation [repo](https://github.com/tensorflow/data-validation)
TFDV(TensorFlow Data Validation)는 기계 학습 데이터를 탐색하고 검증하기 위한 라이브러리

#### TFDV example : [택시 여행 데이터 세트](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew)
##### USAGE
1. 훈련 및 테스트 데이터의 요약 통계에 대한 확장 가능한 계산
- 교육 데이터 example
<img width="1400" alt="스크린샷 2021-09-21 오후 2 18 07" src="https://user-images.githubusercontent.com/45285053/134116002-d3a02ed4-57a1-4cd4-9330-e88e4fd4ae4b.png">
- 교육 데이터의 시각화

```python

train_stats = tfdv.generate_statistics_from_csv(data_location=TRAIN_DATA)
tfdv.visualize_statistics(train_stats)

```

<img width="692" alt="스크린샷 2021-09-21 오후 2 28 58" src="https://user-images.githubusercontent.com/45285053/134116324-61bb3a38-7819-458d-8fe2-24557a72032e.png">



2. 데이터 셋의 스키마 추론과 평가, 환경을 구성하여 요구사항을 표현할 수 있음

3. 데이터 드리프트, 스큐 확인
