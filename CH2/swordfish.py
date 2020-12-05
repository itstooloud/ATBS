while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('hey joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')