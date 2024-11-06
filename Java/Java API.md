# API
---
## String
**创建对象方法**

- String name = "java" 
- String name = new String()
- String name = new String("java") //*不推荐*
- char[] names = {'j','a','v','a'}; String name = new String (names);
- byte[] digits = {97,98,99}; String digit = new String (digits); //*输出：abc*

**提供的常用方法**

![String提供的方法](/Pictures/String-Java.png)

```
public class StringDemo(){
	String words = "我是单词"；
	System.out.printIn(words.length());
	char word = words.charAt[1];
	System.out.printIn(word);
	char[] char = words.toCharArray();
	for(int i=0;i<char.lenth;i++){
		System.out.printIn(char[i]);
	}
	String s1= new String("你好");
	String s2= new String("你好");
	System.out.printIn(s1.equals(s2)); //*true*
	String s3= new String("Nihao");
	String s4= new String("nihao");
	System.out.printIn(s3.equals(s4)); //*false*
	String s5= new String("Nihao");
	String s6= new String("nihao");
	System.out.printIn(s5.equalsIgnoreCase(s6)); //*true*
	String sentence = "Java学习之路";
	String sen = sentence.substring(0,4); //输出sen -> *Java* [0,4)
	String sen2 = sentence.substring(4); //输出sen2 -> *学习之路* 包含4
	String info = "我去真的垃圾";
	String rs = info.replace("垃圾","++"); //rs输出 *我去真的++*
	System.out.printIn(info.contains("垃圾")); //*true* 精准匹配
	System.out.printIn(info.startsWith("我")); //*false* 是否以某个字符串开头
	String star = "你好，我好，大家好";
	String[] splitStar = star.split(","));
	for(int i=0;i<splitStar.lenth;i++){
		System.out.printIn(splitStar[i]);
	}
}
```