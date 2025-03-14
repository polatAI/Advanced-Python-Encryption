import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

hedef_klasor = "C:\\Users\\pc\\Desktop\\youtube\\sifrelendi"
password = b"mypassword"


def encrypt_file(file_path):

    with open(file_path, "rb") as f:
        data = f.read()


    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)


    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))


    sifreli_dosya = file_path + ".enc"
    salt_dosya = file_path + ".salt"


    with open(sifreli_dosya, "wb") as f:
        f.write(cipher.iv)
        f.write(ciphered_data)

    with open(salt_dosya, "wb") as f:
        f.write(salt)


    os.remove(file_path)
    print(f"{file_path} şifrelendi!")


def decrypt_file(file_path):

    salt_dosya = file_path.replace(".enc", ".salt")
    orginal_dosya = file_path.replace(".enc", "")


    if not os.path.exists(salt_dosya):
        print(f"{file_path} için salt dosyası bulunamadı!")
        return
    
    with open(salt_dosya, "rb") as f:
        salt = f.read()


    key = PBKDF2(password, salt, dkLen=32)

    with open(file_path, "rb") as f:
        iv = f.read(16)
        ciphered_data = f.read()



    cipher = AES.new(key , AES.MODE_CBC, iv=iv)
    orginal_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)

    with open(orginal_dosya, "wb") as f:
        f.write(orginal_data)


    os.remove(file_path)
    os.remove(salt_dosya)
    print(f"{orginal_dosya} başarıyla çözüldü!")



def process_folder(encrypt=True):

    for dosya in os.listdir(hedef_klasor):
        tam_yol = os.path.join(hedef_klasor, dosya)


        if os.path.isfile(tam_yol):

            if encrypt and not dosya.endswith(".enc"):
                encrypt_file(tam_yol)

            elif not encrypt and dosya.endswith(".enc"):
                decrypt_file(tam_yol)




if any( f.endswith(".enc") for f in os.listdir(hedef_klasor)):
    process_folder(encrypt=False)

else:
    process_folder(encrypt=True)


