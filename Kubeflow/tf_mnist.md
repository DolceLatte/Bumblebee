### Kubeflow기반 모델 학습 (Using mnist dataset)

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
