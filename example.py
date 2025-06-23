print ("hello world")

def greet(name="ゲスト"):
    return f"こんにちは、{name}さん"
message = greet()
print(message)

name = input("あなたの名前を入力してください:")
def print_name(name):
    return f"私の名前は{name}です"
MyNameIs = print_name(name)
print(MyNameIs)

def get_greet(name):
    return f"おはようございます{name}さん"
GoodMorning = get_greet(name)
print(GoodMorning)

a = input("引数aを入力してください:")
a = int(a)
b = input("引数bを入力してください:")
b = int(b)
def add(a,b):
    return a + b
Calc = add(a,b)
print (f"計算結果は{Calc}です")