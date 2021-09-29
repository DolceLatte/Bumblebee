# Kubeflow start 

### Single node kubernetes cluster에 kubeflow 올리기

#### 1. Docker Desktop에 k8s 설치
[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)링크에 들어가서 docker desktop을 설치한다. (kubeflow는 리눅스에만 설치 가능하기 때문에 wsl컴포넌트를 모두 설치해야 함;)
- 우선 상단에 톱니바퀴를 클릭하고 setting에 들어가면 아래와 같은 화면이 뜬다. <br/> <br/>
![제목 없음](https://user-images.githubusercontent.com/45285053/135270980-b06de25b-5fba-4c66-87a0-9454bc7d71c9.png)
 <br/>
빨간박스의 Enable Kubernetes를 선택하고 하단의 k8s가 초록색이 되어야 kubernetes클러스터가 설치된 것<br/>
- 나같은 경우에는 WSL에서 작업했는데 "kubectl get nodes" 명령어를 쳤을 때 컨트롤 플레인이 찍혀야 잘 설치된 것! <br/>

#### 2. Kubeflow 설치 
필요한 것은 크게 두가지이다. <br/>
- WSL 환경에 맞는 kfctl파일 (나는 kfctl_v1.0-0-g94c35cf_linux.tar.gz)
<br/>압축을 풀고 "sudo mv ./kfctl /usr/local/bin/" 명령어를 통해 로컬에 kfctl명령어를 설치 
- kfctl_k8s_istio파일 apply( kfctl_k8s_istio.v1.0.0.yaml)
<br/>
위 두개를 정상적으로 수행하고 나면 아래와 같이 kubeflow namespace에 정상적으로 pod들이 동작함 
<br/>
<br/>

![캡처](https://user-images.githubusercontent.com/45285053/135272633-5c7dcba6-a02e-4cac-ad6f-efd1ae979c15.PNG)

<br/>
이러고 나면 kubeflow를 사용할 준비가 된 것<br/>
<br/>
kubeflow의 경우 istio-ingressgateway를 통해서 UI에 접속할 수 있음, 해당 포트를 forwarding해서 접속할 수 있게 해야함

```python
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```
![캡처](https://user-images.githubusercontent.com/45285053/135273133-abf1e87a-8d8b-4bc1-b174-6dabb3c5ea6c.PNG)

<br/>여기까지 정상적으로 와야 kubeflow cluster를 사용할 수 있음
