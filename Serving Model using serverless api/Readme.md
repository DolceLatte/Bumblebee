# Serving Model using serverless api

Machine Learning Serving Pipeline 구축

- train model
```python
python3 ../Machine_Learning_Pipeline/train.py
```
- deploy model
```bash
./Machine_Learning_Pipeline/google_function/depoly.sh
```
- predict example
```bash
./Machine_Learning_Pipeline/post.sh
```

#### reference
- https://brunch.co.kr/@chris-song/91
