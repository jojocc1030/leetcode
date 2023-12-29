### Data Structure for Java


<img src="images\Snipaste_2023-12-29_10-36-34.png"  style="zoom: 80%;" />

#### 1. String
```java
String s = "hello";
s += " world";
s += 5;
int sLength = s.length();
String substr = s.substring(1, 5);
char c = s.charAt(2);
if (s.indexOf("hello") != -1) {
    System.out.println("\"hello\" in s");
}
for (int i = 0; i < s.length(); i++) {
    char letter = s.charAt(i);
    System.out.println(letter);
}

```
***String*** 和 ***char[ ]*** 之间的转换：
```java

/**String 转 char[]*/
String str = "Hello, World!";
char[] charArray = str.toCharArray();  //整个string转换
char c = str.charAt(0); //转换指定字母

/** char[] 转 String */
char[] charArray = {'H', 'e', 'l', 'l', 'o'};
String str1 = new String(charArray);
String str2 = String.valueOf(charArray);
String str3 = Arrays.toString(charArray);

```

#### 2. LOOPs

Loop：
```java
int[] array = {1, 2, 3};
for (int i : array) {
    System.out.println(i);
}
```
 Notice the type declaration of the iterating variable, as well as the usage of **:** instead of **in**.

We can also use this syntax on certain other types, such as **Lists and Sets**.

#### 3. List & Set & Map
<img src="images\Snipaste_2023-12-29_11-35-00.png"/>

<img src="images\Snipaste_2023-12-29_11-37-18.png"/>

<img src = "images\Snipaste_2023-12-29_11-40-39.png"/>

#### 4. Class
```java
public class Point {
    public int x;
    public int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public Point() {
        this(0, 0);
    }
    public double distanceTo(Point other) {
        return Math.sqrt(
            Math.pow(this.x - other.x, 2) +
            Math.pow(this.y - other.y, 2)
        )
    }
    public void translate(int dx, int dy) {
        this.x += dx;
        this.y += dy;
    }
}


```

#### 5. Exception
```java
public static int minIndex(int[] numbers) {
    if (numbers.length == 0) {
        throw new Exception("There are no elements in the array!");
    }
    int m = numbers[0];
    int idx = 0;

    ...

    return m;
}
```

#### 6. This, Instance, Static

Instance:
<img src= "images\Snipaste_2023-12-29_12-03-03.png"/>

Static:
<img src = "images\Snipaste_2023-12-29_12-04-19.png">

**Instance**和**static**的区别：

<img src = "images\Snipaste_2023-12-29_11-58-25.png"/>
