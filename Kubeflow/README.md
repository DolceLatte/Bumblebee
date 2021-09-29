# Kubeflow start 

### Single node kubernetes cluster에 kubeflow 올리기

#### 1. Docker Desktop 설치

- 우선 상단에 톱니바퀴를 클릭하고 setting에 들어가면 아래와 같은 화면이 뜬다. <br/> <br/>
![제목 없음](https://user-images.githubusercontent.com/45285053/135270980-b06de25b-5fba-4c66-87a0-9454bc7d71c9.png)
 <br/>
빨간박스의 Enable Kubernetes를 선택하고 하단의 k8s가 초록색이 되어야 kubernetes클러스터가 설치된 것<br/>
- 나같은 경우에는 WSL에서 작업했는데 "kubectl get nodes" 명령어를 쳤을 때 컨트롤 플레인이 찍혀야 잘 설치된 것! <br/>

