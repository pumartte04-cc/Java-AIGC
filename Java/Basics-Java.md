# Java基础知识
---
## 类型范围

byte -> short -> int ->long ->float ->double

char->int

<font color=6495ED>小范围类型的变量可以直接赋值给大范围类型的变量</font>

<font color=6495ED>byte类型会直接变成int类型</font>

**<font color=red>例如</font>**

```
byte b1=2; byte b2=3;  
[byte b3 =b1+b2] <-是错误的 
因为此时的b1+b2为int类型  
需要强制类型转换=> byte b3=(byte)b1+b2;
```

## 数组
***常见格式***

数组类型[ ] 数组名 = new 数据类型[]{元素1，元素1···} ;

`int[] ages =new int[]{20,21,22,23}`

简化：数组类型[ ] 数组名 = {元素1，元素1···} ;

`int[] ages = {20,21,22,23}`

<font color=6495ED>数据类型[ ] 数组名 === 数据类型 数组名[ ]</font>

***内存分配***

- 方法区：放class文件的

- 栈内存：放运行的方法，main方法，定义的变量

- 堆内存：new出来的对象都存在堆内存中 （堆内存比较大）

## 方法
``` 
public static viod java(){
System.out.printIn("This is java");
}
```

 <font size=3 color=orange>**方法的参数传递机制**</font>

**-值传递-**

- 传输实参给方法的形参，传输的不是实参本身，而是实参中存储的数据的一个副本
- 基本类型的参数传输的是存储的数据，引用类型的参数传输的是存储的地址值

 <font size=3 color=orange>**重载**</font>

同一个类中，方法名称相同，形参列表必须不同

*-形参列表不同：形参的个数、类型、顺序不同，不关心形参变量的名称-*

```
public static string wyr(int age,string name){}
```
```
public static string wyr(int age,string name,boolean girl){}
```
