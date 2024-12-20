# Advanced JAVA
---
**！(整理的都是自己不太熟悉的，不全)**

## final关键字
- 可以修饰类、方法、变量
- 修饰类：该类被称为最终类，特点是不能被继承了
- 修饰方法：被称为最终方法，不能被重写
- 修饰变量：该变量只能被赋值一次

```
final修饰基本类型的变量，变量存储的数据不能被改变。
final修饰引用类型的变量，变量存储的地址不能发生改变，但地址所指向对象的内容是可以被改变的。
```

## 常量
- 使用 static final修饰的成员变量被称为常量
- 通常用于记录系统的配置信息
- 命名规范：大写英文字母，多个字母用下划线连接 （SCHOOL_NAME）

## 抽象
- 抽象类中不一定有抽象方法，有抽象方法的类一定是抽象类
- 抽象方法不能有方法体 （无{}）
- 类该有的成员（成员变量、方法、构造器）抽象类都可以有
- 抽象类不能创建对象，仅作为一种特殊的父类，让子类继承并实现
- 一个类继承（extends）抽象类，必须重写完抽象类的全部抽象方法，否则这个类也必须定义成抽象类


## 接口
```
public interface 接口名{
	//成员变量 （默认为常量）
	//成员方法（默认为抽象方法）
}
```

- 接口不能创建对象，只能用来实现（implements）
- 一个类可以实现多个接口，必须重写完全部接口里的全部抽象方法
- 接口可以多继承（一个接口继承多个接口）
- JDK8之后新增的几个功能方法：
  - 默认方法:必须使用default修饰，默认会被public修饰。其实就是一个实例方法，可以用实现类的对象来访问
  - 私有方法：必须使用private修饰（JDK9之后），需要用接口中实例方法访问，实现类的对象不可以直接访问
  - 静态方法:必须用static修饰。用接口直接调用

### 接口的注意事项
1. 一个接口继承多个接口，如果多个接口中存在方法签名冲突，则此时不支持多继承。
2. 一个类实现多个接口，如果多个接口中存在方法签名冲突，则此时不支持多实现。
3. 一个类继承了父类，又同时实现了接口，父类中和接口中有同名的默认方法，实现类会优先用父类的。
4. 一个类实现了多个接口，多个接口中存在同名的默认方法，可以不冲突，这个类重写该方法即可。
