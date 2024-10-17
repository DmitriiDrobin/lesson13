n = int(input("Введите число с первого камня: "))
flag = True
while flag:
    pass_ = ''
    for m in range(1, n):
        for k in range(1, n):
            a = m + k
            if m == k:
                continue
            elif m > k:
                continue
            elif a > n:
                flag = False
                continue
            elif n % a == 0:
                pass_ = pass_ + str(m) + str(k)
    print(f"Ваш пароль для входа = {pass_}")
    break
