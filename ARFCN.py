print('Нажмите Ctrl+C для завершения программы')
def fun():
    while True:
        try:
            inp = input()
        except KeyboardInterrupt:
            print("   ОПЕРАЦИЯ ПРЕРВАНА ПОЛЬЗОВАТЕЛЕМ")
            # прервать while после операции отмены пользователем
            exit (0)
            break
        try:
            inp=int(inp)
        except ValueError:
            print("ЦЕЛЬСЯ ЛУЧШЕ! Внимательно ЦИФЕРКИ ВВОДИ!")
        else:
            #print('Исключений не произошло ')
            return inp
            break
# тестовый принт для отладки def
#print(fun())

standart_gsm = {
    1: 'EGSM',
    2: 'DCS',
    3: 'PCS',
}

#gsm = int(input('выбор стандарта GSM : '))
#print(standart_gsm[gsm])

while True:
    print('Выбирите стандарт : GSM 1 - EGSM , 2 - DCS, 3 - : PCS')
    gsm = fun()
    if (1<=gsm <=3):
        print("Выбран GSM стандарт - ",standart_gsm[gsm])
        break


while True:   
    if gsm == 1:
        print("range(975,1024)")
        i = fun()
        if (975<=i <=1024):
            print("EGSM ARFCN", i)
            print("TX: ", 890 + (i-1024) * 0.2 , "MHz")
            print("RX: ", 935 + (i-1024) * 0.2 , "MHz")
            exit(0)
            break
    
    if gsm == 2:
        print("range(512,886)")
        i = fun()
        if (512<=i<=886):
            print("DCS ARFCN", i)
            print("TX: ", 890 + (i-1024) * 0.2 , "MHz")
            print("RX: ", 935 + (i-1024) * 0.2 , "MHz")
            exit(0)
            break

    if gsm == 3:
        print('range(512,886)')
        i = fun()
        if (512<=i <=886):
            print("PCS ARFCN", i)
            print("TX: ", 890 + (i-1024) * 0.2 , "MHz")
            print("RX: ", 935 + (i-1024) * 0.2 , "MHz")
            exit(0)
            break

