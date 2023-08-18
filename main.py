from cryptography.fernet import Fernet
 
path_to_key = input("Enter the path to the key for encryption and decryption:")
path_to_file = input("Enter the path to the file you want to ecrypt and decrypt:")
enorde = input("\n=======\n[E/D]:")
with open(path_to_key , "r") as f :
    key = f.read()
if enorde == "e" or "E" :
    with open(path_to_file , "r") as file:
        data= file.read()
    byte_data= data.encode()
    cryptor = Fernet(key)
    encrypted = cryptor.encrypt(byte_data)
    with open("ecrypted_item.enc" , "wb") as enc :
        enc.write(encrypted)
elif enorde == "d" or "D"  :
    with open(path_to_file , "r") as file:
        data= file.read()
    byte_data= data.encode()
    cryptor = Fernet(key)
    encrypted = cryptor.encrypt(byte_data)
    with open("decrypted_item.enc" , "wb") as enc :
        enc.write(encrypted)
else :
    pass