import hashlib



def hash256():
    print ('Usahakan Gunakan Path !!!!!ingat hanya untuk edukasi!!!!!')
    rar = str(input('Masukan Rar nya yang mau di Hash :'))
    with open(rar, 'rb') as f:
    
        data = f.read()
    
    hash_object = hashlib.sha256()
    hash_object.update(data)

    
    hash = hash_object.hexdigest()

    print('Hash SHA-256 dari file RAR:', hash) 
    
def hashmd5():
    rar = str(input('Masukan Rar nya yang mau di Hash :'))
     
    with open(rar, 'rb') as f:
        data = f.read()
    
    hash_object = hashlib.md5()
    hash_object.update(data)

    hash_md5 = hash_object.hexdigest()
    
    print("Hash MD5 dari file RAR:", hash_md5)

