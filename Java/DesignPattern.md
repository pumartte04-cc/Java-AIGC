# 设计模式
---
##单例设计模式
**作用**

确保一个类只有一个对象

**写法**

- 把类的构造器私有
- 定义一个类变量记住类的一个对象
- 定义一个类方法，返回对象

**实现方式**

- 饿汉式单例模式  
```
在获取对象之前就已经将对象创建好了（提前创建好对象）
```

- 懒汉式单例模式  
```
在获取对象之后才开始创建对象（不提前创建对象）
```

###懒汉式单例模式
**写法**

- 把类的构造器私有
- 定义一个类变量用于存储对象
- 定义一个类方法，保证返回的是同一个对象

```
public class Singleton{
	private static Singleton s;
	private Singleton(){}
	public static Singleton getInstance(){
		if(s == null){s = new Singlenton();}
		return b
	}
}
```