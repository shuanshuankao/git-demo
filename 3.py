a=eval(input("請輸入數字a : "))
b=eval(input("請輸入數字b : "))


if b>a:
    c=b-a
    print(f"b比a大{c}")
elif a>b:
    c=a-b
    print(f"a比b大{c}")
else :
    print("b跟a一樣大")

