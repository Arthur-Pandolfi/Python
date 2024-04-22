idade = int(input('Digite sua idade: '))
if idade < int('9'):
    print(f'Você ira participar da classificação \033[1mMirim\033[m!')
elif idade < int('14'):
    print(f'Você ira participar da classificação \033[1mInfantil\033[m!')
elif idade < int('19'):
    print(f'Você ira participar da classificação \033[1mJunior\033[m!')
elif idade < int('20'):
    print(f'Você ira participar da classificação \033[1mSênior\033[m!')
elif idade > int('20'):
    print(f'Você ira participar da classificação \033[1mMaster\033[m!')
