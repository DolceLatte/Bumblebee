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
- 리턴 타입의 하위 타입을 반환할 수 있다. (nCopys?)
- 입력 매개변수에 따라 매번 다른 클래스 객체를 반환할 수 있다. (Enum?)
- 반환순간에 abstract class를 반환가능? ㅁㄹ 이건 (service provider framework)
	
단점도 있음  
- 계승이 일어날 때, 문제가 생김 (계승이 별로임 그러니까 무시하자)
- 이름이 애매해서 먼지 모름

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

### 2. 생성자의 매개변수가 많으면 빌더 패턴을 고려하라

인자가 많으면 생성하기 힘듬  

해결법  
1. 자바빈 패턴 (setter) -> 객체 콜이 여러줄에 이어짐 이게 결국 객체를 const로 못 만든다는 말임  

2. 그래서 빌더!
- builder 클래스를 inner 클래스로 해서 생성자를 대신 부르게 함 static member class
- 인자의 개수에 영향을 덜 받음
- 무슨 인자인지 알기 쉬움 : 가변 인자를 다루기 쉬움
 
장점 또 있음
- 하나의 빌더로 여러 객체를 만들 수 있다. 
Abstract Factory pattern과 빌더 패턴  

Abstract Factory pattern으로 구현된 빌더를 메소드의 인자로 던져서 내부 구현 및 계층구조는 무시하도록 하는 것?  
이게 되려면 builder를 계층구조로 설계해야 한다.  

```java

public abstract class A{
    private final double p;
    private final double a;
   

    // 추상 클래스는 추상 Builder를 가진다. 서브 클래스에서 이를 구체 Builder로 구현한다.
    abstract static class Builder< T extends Builder<T>>{

        //필수 인자
        private final double p;
        //필수가 아닌 인자
        private double a = 0;
       
        protected Builder(double p) {
            this.p = p;
        }

        public T a(double a) {
            this.a = a;
            return self();
        }

        abstract Product build();
        // 하위 클래스는 이 메서드를 overriding하여 this를 반환하도록 해야 한다.
        protected abstract T self();
    }

    Product(Builder<?> builder){
        this.p = builder.p;
        this.a = builder.a;   
    }

    public String toString() {
        return "hello world";
    }
}

public class B extends A {
    private final int o;

    public static class Builder extends A.Builder<Builder> {
        private int o = 0;
	
	//상위 계층의 빌더 
        public Builder(double p) {
            super(p);
        }

        public Builder o(int o) {
            this.o = o;
            return self();
        }

        @Override
        public LocalProduct build() {
            return new B(this);
        }

        @Override
        protected Builder self() {
            return this;
        }
    }

    private B(Builder builder) {
        super(builder);
        o = builder.o;

    }
}


```
--> 어쨋든 하위 클래스에서 build와 self를 정의 해서 쓰면 되는 것 같음

단점도 있음  
- 빌더를 만드는 비용이 있고, 코드가 장황함
- 그래도 무시할 수준





