### Kubeflow기반 모델 학습 (Using mnist dataset)
- mnist 데이터 다운로드 컨테이너와 케라스기반의 모델학습 컨테이너 파이프라인 구축
- mnist 데이터 다운로드 결과를 다음 컨테이너의 입력으로 전송

코드 출처
https://github.com/chris-chris/kubeflow-tutorial/blob/master/lesson9_tf_mnist/tf_mnist.py

```python

def download_mnist():
    pass

def train_mnist():
    pass
    
def tf_mnist_pipeline():
    download_op = func_to_container_op(download_mnist, base_image="tensorflow/tensorflow")
    train_mnist_op = func_to_container_op(train_mnist, base_image="tensorflow/tensorflow")
    train_mnist_op(download_op().output)


if __name__ == '__main__':
    import kfp.compiler as compiler
    compiler.Compiler().compile(tf_mnist_pipeline, __file__ + '.zip')
    kfp.Client(host=KUBEFLOW_HOST).create_run_from_pipeline_func(
        tf_mnist_pipeline,
        arguments={},
        experiment_name=EXPERIMENT_NAME)
```

![1](https://user-images.githubusercontent.com/45285053/156910277-a4652154-f933-4efd-99b0-3e2062c2bda8.PNG)
- 위와 같이 학습 DAG를 얻을 수 있음
- Log에 결과가 찍히는게 참 신기하다..

학습된 모델은 output 아티펙트로 minio에 저장됨 
- 접속을 위해서는 gateway를 열어야 함, 비번은 아래와 같이 pod에서 찾을 수 있음
![미니오 접속 키](https://user-images.githubusercontent.com/45285053/156910299-10879d23-b95f-4d2a-917e-7a38c0f1bf28.PNG)
![비번](https://user-images.githubusercontent.com/45285053/156910300-50c612a9-ae63-4da5-af97-f234ada6261e.PNG)

- 아래에서 완성된 모델 다운 가능
![모델 완성본](https://user-images.githubusercontent.com/45285053/156910301-bc9905dc-9573-4bbe-9015-5488c1bd990a.PNG)




