# 어쩌다 보니 생긴 종이장

## 이펙티브 자바 공부하다가 파이썬은 어떨까 하고 만든 페이지
#### 사실 교과목
목차는 뒤죽박죽 

### equals를 재정의하려거든 hashCode도 재정의하라

equals()를 재정의한 클래스 모두에서 hashCode()도 재정의해야 한다고 함  
-> 즉, 같은 객체는 반드시 같은 hashcode를 가져야한다는 말  
그렇다고 실행할 때 마다 같아야하는 것은 아님.  
hashCode()가 똑바로 정의되지 못하면, hash를 다루는 자료구조에서 성능저하가 있음  

#### hashCode() 메서드를 구현하는 요령
```java
//Type.hashCode(f)
public int hashCode() {
    int result = field1.hashCode();
    result = 31 * result + field2.hashCode();
    result = 31 * result + field3.hashCode();

    return result;
}
```
### 파이썬의 equals 비교
파이썬에는 is와 ==이 있음 이중 is 연산자는 identity를 비교 
즉, 같은 객체라면 true를 반환  
==의 경우 동등성을 비교, 클래스 내부의 __eq__의 내용을 기반으로 두 객체의 동등성을 비교함  
마찬가지로  __hash__를 구현하지 않으면 자료구조 내부에서 비효율적인 연산을 수행할 수 있음  

```python
import hashlib
# 혹은
hash()
```
위의 함수들을 활용해서 해시를 구현하자

### clone 재정의는 주의해서 진행하라

