# HelloWorld Experiments

Kubeflow는 컴포넌트 단위로 Machine Learning pipeline을 구축할 수 있다. <br/>
잘 모르니까 실험을 등록해서 log에 HelloWorld를 남겨보자 <br/>
+ 실험과 파이프라인은 다른 것 같다.  <br/>
+ 파이프라인의 컴포넌트를 실험으로 등록해서 확인하는 것 같음, 실제로 어떻게 쓰는지 궁금하다.<br/>

## logging Hello_world in pipeline
echo "hello world" [hello_world.py](https://github.com/kubeflow/pipelines/blob/0.1.40/samples/core/helloworld/hello_world.py) <br/>
kubeflow github에 가면 예제 코드가 많이 나와있다. 

```python
import kfp
from kfp import dsl

KUBEFLOW_HOST = "http://127.0.0.1:31380/pipeline"

def echo_op():
    return dsl.ContainerOp(
        name='echo',
        image='library/bash:4.4.23',
        command=['sh', '-c'],
        arguments=['echo "hello world"']
    )

@dsl.pipeline(
    name='My first pipeline',
    description='A hello world pipeline.'
)
def hello_world_pipeline():
    echo_task = echo_op()

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(hello_world_pipeline, __file__ + '.yaml')
    kfp.Client(host=KUBEFLOW_HOST).create_run_from_pipeline_func(
        hello_world_pipeline,
        arguments={},
        experiment_name="my first pipeline",
    )
```

dsl.ContainerOp()를 통해 컴포넌트를 구현하고 @dsl.pipeline 데코레이터를 통해 파이프라인으로 반환하게 하는 코드 <br/>
kubeflow 공식 예제에는 없는 코드가 아래인데, <br/>

```python
 kfp.Client(host=KUBEFLOW_HOST).create_run_from_pipeline_func(
        hello_world_pipeline,
        arguments={},
        experiment_name="my first pipeline",
    )
```
kfp.Client()를 통해 실행하는 과정을 거쳐야 직접 UI에 실험이 등록되는 듯 하다. 용도는 두가지가 있다고 함. <br/>
- kfp.Client.create_experiment : 파이프 라인 experiment 을 만들고, experiment  개체를 반환합니다.
- kfp.Client.run_pipeline 파이프 라인을 실행(run)하고 실행(run) 개체를 반환합니다.

어쨋든 잘 코드를 실행하고 나면 아래와 같이 실험 탭에 내가 구축한 실험이 등록되고<br/>
![실험 창](https://user-images.githubusercontent.com/45285053/135752307-bee2b0da-c284-44b4-9877-770ada6c9087.PNG)

<br/>
- 아래와 같이 세부사항을 확인하면 log에 "HelloWorld" 가 찍힌 것을 볼 수 있다.<br/>

![asdasd](https://user-images.githubusercontent.com/45285053/135752397-0e2d6fbb-ed1d-4a37-a55b-88b0f23a3254.PNG)
<br/>

