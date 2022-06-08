def removePalindromicSub(string):
    steps = 0
    while len(string) > 0:
        if check_palindromic(string):
            steps += 1
            string = ''
        else:
            for i in range(len(string)):
                if check_palindromic(string[:len(string) - i]):
                    # print(string[:len(string)-i])
                    steps += 1
                    string = string[len(string) - i:]
                    print(string)
                    break
    return steps

def check_palindromic(string):
    if string == string[::-1]:
        return True
    else:return False

def check_input(string):
    for latter in string:
        if latter in 'ab':
            pass
        else:return False
    return True

def check_exit(string):
    if string == 'Q' or string == 'q':
        return False
    else: return True


if __name__ == '__main__':
    """
    Все на самом деле еще проще. Строка состоит только из последовательности двух символов, 
    значит либо символ сразу полиндром, либо сначала выбираем все "а", потом все "b". Т.е.
    минимальное количество всегда 2, если слово изначально не полиндром.
    """
    
    run = True
    
    while run:
        string = input()
        if check_input(string):
            steps = removePalindromicSub(string)
            print(steps)

        else:
            print('Ошибка, слово может состоять только из "a" или "b"')
            print('Чтобы выйти нажмите Q,    Чтобы продожить введите любой символ')
            exit = input()
            run = check_exit(exit)