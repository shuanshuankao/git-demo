# 1. 加入例外處理 try + except Exception as e
# 2. 重複輸入，直到 a => exit 離開 ，使用 while true

while True:
    try:
        a=input("請輸入數字a : ")
        if a=="exit":
            break

        #a=eval(input("請輸入數字a : "))
        a=eval(a)
        b=eval(input("請輸入數字b : "))

        if b>a:
            c=b-a
            print(f"b比a大{c}")
        elif a>b:
            c=a-b
            print(f"a比b大{c}")
        else :
            print("b跟a一樣大")

        # if a==b:
        #     print("a跟b一樣大")
        # elif a>b:
        #     print(f"a>b，相差{a-b}")
        # else :
        #     print(f"a<b，相差{b-a}")

        if input("是否離開?(y/n)")=="y":
            break
    except Exception as e:
        print("輸入錯誤!",e)