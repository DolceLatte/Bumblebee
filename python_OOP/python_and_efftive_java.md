# 어쩌다 보니 생긴 종이장

## 이펙티브 자바 공부하다가 파이썬은 어떨까 하고 만든 페이지
목차는 뒤죽박죽  
### 1. 생성자 대신 정적 팩토리 메소드를 사용해라

생성자 대신 정적 팩토리 메소드를 사용하는 것은 장점이 많음. <br/>

자바는 서브 타입의 개념이 있음, 머 이런게 있다보니 생성자로 타입을 다룰 때 Object인지... 아닌지... 그니까 인스턴스 수준에서 제어할 수 있어야 한다? 이런게 동기인듯 <br/>

만약 새롭게 인스턴스를 만들 필요없다면 기초자료형을 Boxing을 통해서 싱글톤처럼 하는게 중요할 수 있다. <br/>

만약에 코딩을 한다면...<br/>

```java
public static Boolean valueOf(boolean b){
		return b ? Boolean.TRUE : Boolean.FALSE;
	}
```

SFM의 장점 
- 이름을 가질 수 있다.
- 매번 인스턴스를 안 만들어도 된다. 
- 

#### 만약에 파이썬은?
일단 파이썬은 타입이고 뭐고 없음, 동적타입 언어지만.. 그래도 형변환을 암묵적으로 하지는 않는다.  

일급 객체여서 모든 인스턴스가 객체로 다루어지는 듯함  

그럼 위와 같은 정적 팩토리 메소드가 필요할까? -> 인스턴스 수준의 제어는 항상 필요함 

코딩하면... https://wikidocs.net/69361

```python
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):         # Foo 클래스 객체에 _instance 속성이 없다면
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
        return cls._instance                      # Foo._instance를 리턴

    def __init__(self):
        print("__init__ is called\n")

s1 = Singleton()

```
__new__와 같은 메소드로 객체수준의 제어를 할 수 있다고 한다. 신기하네 방어적 프로그래밍을 할 때 쓴다고 함  

이렇게 쓰고 나니 SFM이랑 싱글톤이랑 구분이 안간다.  

팩토리 메소드 패턴에서는 객체를 생성하기 위한 인터페이스를 정의하는데, 어떤 클래스의 인스턴스를 만들지는 서브 클래스에서 결정하게 만든다. 팩토리 메소드 패턴을 이용하면 클래스의 인스턴스를 만드는 일을 서브 클래스에게 맡기는 것이 된다.  
출처: https://js2prince.tistory.com/entry/싱글톤-패턴-팩토리-패턴 [개발은 전투다]  

라고 써있는데... 이런걸 보면 좀 확장된 개념인가 싶다 활용하기 나름 인듯  



