from cryptography.fernet import Fernet

path_to_key = input("Enter the path to the key for encryption and decryption:")
path_to_file = input("Enter the path to the file you want to encrypt and decrypt:")
enorde = input("\n=======\n[E/D]:")
with open(path_to_key, "r") as f:
    key = f.read()

if enorde.lower() == "e":
    with open(path_to_file, "r") as file:
        data = file.read()
    byte_data = data.encode()
    cryptor = Fernet(key)
    encrypted = cryptor.encrypt(byte_data)
    with open("encrypted_item.enc", "wb") as enc:
        enc.write(encrypted)

elif enorde.lower() == "d":
    with open(path_to_file, "rb") as file:
        data = file.read()
    cryptor = Fernet(key)
    decrypted = cryptor.decrypt(data)
    with open("decrypted_item.enc", "wb") as enc:
        enc.write(decrypted)

else:
    print("Something went wrong.")