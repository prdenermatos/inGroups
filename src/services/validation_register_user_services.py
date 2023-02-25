from flask import session, flash
class ValidationRegisterUserServices:
    def __init__ (self, password, password_confirme ):
   
        self.password = password
        self.password_confirme = password_confirme
    
    def validate_confirmation_password(self) -> bool:
        return self.password == self.password_confirme
    
    # def validate_fields_registration(self):
    #     log_error_list = []
    #     if (self.name == ''): 
    #         log_error_list.append('O campo nome é obrigatório!')
    #     if (self.email == ''): 
    #         log_error_list.append('O campo E-mail é obrigatório!')
    #     if (self.telephone == ''):
    #         log_error_list.append('O campo Telefone é obrigatório!')
    #     if (self.password == ''):
    #         log_error_list.append('O campo senha é obrigatório!')
    #     if (self.password_confirme == ''):
    #         log_error_list.append('É necessário confirmar a Senha!')
    #     return log_error_list
    

class AuthGuardUser:
    def __init__(self, email: str, password_decrypt: str) -> None:
        self.email = email
        self.password_decrypt = password_decrypt
    

class AccessControl:
    def avaliable():        
        if 'user_logger' not in session or session['user_logger'] == None:
            flash('Para acessar o sistema é necessário fazer o login!')
            return False
        else:
            return True


    


    

