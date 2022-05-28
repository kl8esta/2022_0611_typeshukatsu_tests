for num in range(1, 101):
    string = ''

    # ここから記述
    # numが(5の倍数以外の)3の倍数の場合
    if num % 3 == 0  and num % 5 != 0:
        string = "Fizz"

    # numが(3の倍数以外の)5の倍数の場合
    elif num % 5 == 0 and num % 3 != 0:
        string = "Buzz"

    # numが15の倍数(3の倍数かつ5の倍数)の場合
    elif num % 15 == 0:
        string = "FizzBuzz"

    # それ以外のnumの場合
    else:
        string = str(num)  # 数字を文字列に変換
    # ここまで記述

    print(string)
