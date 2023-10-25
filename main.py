import pywhatkit as kt
while True:
    print('Здравейте как мога да Ви помогна днес?')
    find = input("Какво да търся?): ")

    if find.lower() == 'чао':
        print('Довиждане')
        break
    kt.search(find)
