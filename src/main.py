from functions import Dialog

Dialog.clear()
while True:
    answer = input('>>> ')
    if answer == '/help':
        Dialog.help()
    elif answer == '/clear':
        Dialog.clear()
    elif answer == '/donate':
        Dialog.donate()
    elif answer == '/exit':
        exit()
    elif answer == '/autocost':
        Dialog.autocost()
    else:
        print('Неизвестная команда')
