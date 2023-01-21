import rarfile

def crack_rar():
    In_rar= str(input('Rar Nya Kawan:'))
    In_text= str(input('List text nya kawan:'))

    rar = rarfile.RarFile(In_rar)
    with open(In_text, 'r') as f:
        passwords = f.readlines()
    passwords = [x.strip() for x in passwords]
    
    for password in passwords:
        try:
            rar.extractall(pwd=password)
            print('Password ditemukan:', password)
            break
        except:
            pass
    
    print('Tidak ada password yang cocok, seperti hatimu yang ndak cocok sama aku')

