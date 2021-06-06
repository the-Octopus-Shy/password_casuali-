import random
while True:
    caratteri =  '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzé§àç._:-^'ì)&%$£1234567890*'''
    print("hello what's your name?")
    nome = str(input())
    print("ok "+ nome+ " remember, that great powers come with great responsibilities so use this password generator to help people.")
    print("Ok.... now the real program begins")
    print("ok how many characters do you want in your password?")
    numero_caratteri = int(input())
    password = ""
    for x in range(numero_caratteri):
        password += random.choice(caratteri)
    print("this is your new password !!")
    print(password)
    
        
        
    
