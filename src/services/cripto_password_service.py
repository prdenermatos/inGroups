from hashlib import md5

class CriptoPasswordService: 
    def __init__ (self, password_register): 
        self.password_register = password_register.encode("utf8")
    def encrypt(self):
        cripto = md5(self.password_register).hexdigest()
        hashed = self.password_register[0]
        password_cripto = f'{hashed}{cripto}{hashed}'
        return password_cripto 

    def decrypt(self, password_insert, password_cripto_find_db ) -> bool:
        cripto = md5(password_insert.encode("utf8"))
        hashed = password_insert[0]
        password_avaliable = f'{hashed}{cripto}{hashed}'
        return password_avaliable == password_cripto_find_db


