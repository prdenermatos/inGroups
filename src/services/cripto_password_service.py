import hashlib

class CriptoPasswordService: 
    def __init__ (self, password_register): 
        self.password_register = password_register
    def encrypt(self):
        senha = str = ''.join(self.password_register)
        # print(senha, 'tipo:', type(senha) )
        salt = 'saltsaltsalt'
        hash_object = hashlib.sha256((senha + salt).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig

  


