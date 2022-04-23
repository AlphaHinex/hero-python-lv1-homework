## 2022.02.19

[爱心]各位同学们，本节课的重点知识来袭，请注意查收~！
⚠本节课英文单词为：
family 家庭 sister 姐姐
purse 钱包
append 添加 insert 插入
remove  移除  去除
孩子们可以利用晨读/晚读时间再次复习记忆
为英语学习打下夯实基础。
⚠本节课所学编程知识：
❕列表的使用 list = [ ] 存储元素及列表元素的获取
通过下标获取元素 ，下标是从0开始的
❕列表的添加和插入方法 list.append（） list.insert() pop() remove()

## 2022.03.05

[爱心]各位同学们，本节课的重点知识来袭，请注意查收~！
⚠本节课英文单词为：
flower (花)        meaning (含义)
country（国家）China（中国）
capital（首都） pattern（图案）

孩子们可以利用晨读/晚读时间再次复习记忆
为英语学习打下夯实基础。
⚠本节课所学编程知识：
❕列表存储花对象并访问属性
❕列表存储对象以及列表中对对象属性的获取（通过下标获取）
❕列表存储Enemy对象以及Enemy对象属性的获取
❕列表中对象方法的调用

## 2022.03.12

无

## 2022.03.26

各位同学们，本节课的重点知识来袭，请注意查收~！
⚠本节课英文单词为：
len 长度 （length长度）
for  对于，为了
fruit 水果
number  数字
孩子们可以利用晨读/晚读时间再次复习记忆
为英语学习打下夯实基础。
⚠本节课所学编程知识：
❕创建生成组件的方法随机产生敌飞机
❕len( ) 方法 获取列表的长度
完善componentEnter生成敌飞机
❕for in 循环遍历列表元素的方法

## 2022.04.02

无

### 方法

1. 如何定义一个方法

使用 def 关键字 + 方法名 + ( + 逗号间隔的参数 + ) + :

如 `def action(name, type):`

方法可以直接定义，也可以定义在类中

### 类

1. 如何定义一个类

使用 class 关键字 + 类名 + () + :

如 `class Dog():`

2. 如何使用类创建一个实例

使用 类名 + ()，括号内，传入 `__init__` 方法中定义的参数（除 self）

3. 类中使用的 self 代表什么

代表类被实例化后的对象，类中的每个方法，都可以获取到 self 对象

4. 如何在类中定义属性

通过 self + . + 属性名 定义，如 `self.name = 'hero'`

5. 如何访问一个类的属性

先将类实例化，通过实例化后的对象 + . + 属性名 进行访问，如：

```python
class Dog():
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior
    def action(self):
        print('action')

d = Dog('二哈','拆家')

print(d.name)
```

6. 如何调用一个类的方法

先将类实例化，通过实例化后的对象 + . + 方法名 + ( + 参数 + ) 进行调用，如：

```python
# 使用上例中的类定义
d.action()
```

7. 能否直接通过类名进行属性或方法的调用

不能！必须先实例化！

8. 类中定义的其他方法，如何访问类的属性

需要通过 `self` 对象进行类属性的访问，如：

```python
class Dog():
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior
    def action(self):
        print(self.behavior)
```

### 循环

两种循环方式：

```python
while True:
    doSomething()
```

```python
for a in list:
    doSomethingWith(a)
```

`for ... in ...` 循环中，
`in` 关键字后面必须是可遍历的对象，如队列；
`in` 关键字前面，是每次循环取出的一个对象，对象的变量名可随便取
使用 `for ... in ...` 遍历时，循环体内一般是需要对遍历出的对象进行操作的

## 2022.04.16

pygame.time.delay 在 mac 下无法正常运行问题：

https://stackoverflow.com/questions/64190529/pygame-display-update-doesnt-work-well

可在 update 后，先执行 `pygame.event.pump()`，再执行其他内容

## 2022.04.23

[爱心]各位同学们，本节课的重点知识来袭，请注意查收~！
⚠本节课英文单词为：
temperature 温度
dragon 龙 

孩子们可以利用晨读/晚读时间再次复习记忆
为英语学习打下夯实基础。
⚠本节课所学编程知识：
❕局部变量和全局变量的使用
❕类属性 类属性在飞机大战中使用
使用方式：类名.类属性名