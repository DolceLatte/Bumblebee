## 쿠버네티스 차트로 pod 띄우기

교내 쿠버네티스 특강 TA하면서 쿠버네티스 차트가 중요한지 몰랐는데, 개발자분이 강조해주셔서 나도 한번 해봄

#### 헬름으로 배포 간편화하기
- 헬름은 쿠버네티스 패키지 매니저 서비스 
- 헬름 명령어를 사용해 어플리케이션을 설치하고 설정해보자 간단하게.. nginx부터...

```bash
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh
```

위와 같은 스크립트로 설치할 수 있다.
역시 설치가 참 애먹었다. 일단 그냥 버전이 낮은 helm을 썻다
(밑도 끝도 없이 설치가 안된다. )

차트를 생성하면 아래와 같은 구조로 디렉터리를 다운받는다
<br/>
<p>
![image](https://user-images.githubusercontent.com/45285053/161426475-6ad34d0b-b468-4700-956e-681d8d1e3606.png)
</p>
구체적인건 생략하고 values.yaml파일을 중심으로 템플릿 폴더 아래의 파일들과 결합해서 실제 쿠버네티스 파드를 띄우는 것 같다. 간단하게 리소스만 부여하고 아래와 같이 설치하면
<br/>
<p>
![image](https://user-images.githubusercontent.com/45285053/161426480-c5dba4e8-affd-4f31-b90e-23068dacf4ec.png)
</p>
아맞다 포트포워딩<br/>
<p>
![image](https://user-images.githubusercontent.com/45285053/161426481-65f941dc-a776-4b5e-9288-788096b65bfb.png)
</p>
사실 이게 중요한지 몰랐는데, 쿠버네티스 특강 때 TA를 하는데, 개발자분이 엄청 강조하시더라. 오늘은 별게 없음
