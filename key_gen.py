from cryptography.fernet import Fernet
with open("key.key" , "wb") as file :
    file.write(Fernet.generate_key())