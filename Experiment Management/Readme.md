# Experiment Management : MNIST example classifier

## What is Weight & Bias ([wandb.ai](https://wandb.ai/site))
<p>
머신러닝을 위한 성능 시각화 도구, 어려운 머신 러닝 실험관리를 위해 사용할 수 있는 Developer tool
</p>

- 실험 결과 매트릭의 정리
- 실험 결과의 재연
- Hyperparameter Optimization : 가장 큰 영향을 미치는 HP 확인 가능
- GPU 사용률 역시 확인 가능


### 1. Use Weight & Bias for Experiment Management
#### LOSS REPORT USING W&B : [Source Code](https://github.com/DolceLatte/Bumblebee/blob/main/Experiment%20Management/wandb_mnist.ipynb)
![image](https://user-images.githubusercontent.com/45285053/133961332-7e602bdd-b051-4ceb-b3c1-c842a51dfaa2.png)

### 2. Hyperparameter Optimization : W&B Sweep
#### Result REPORT USING W&B Sweep : [Source Code](https://github.com/DolceLatte/Bumblebee/blob/main/Experiment%20Management/sweep_mnist.ipynb)

<img width="1440" alt="스크린샷 2021-09-20 오후 7 34 13" src="https://user-images.githubusercontent.com/45285053/133989185-7d548c76-e0e7-43d6-88ee-026aaef000fd.png">

[view report](https://wandb.ai/dolcelatte/Pytorch-sweeps-example/reports/MNIST-Classification-Report--VmlldzoxMDM4ODM0?accessToken=bnki6vzye51elx0s1fhk4s33xmq6vhn0jm6pjqzmr5bs2z9ihhkal24ho0vfprsc)

