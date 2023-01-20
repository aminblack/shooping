from helper.exceptions import(
    WrongUserNameException,
    TypeUserNameException,
    WrongPassWordException,
    TypePassWordException
)

class Users:

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name},{self.username},{self.password})'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeUserNameException("username must be 'string'.")
        if not value[0].isalpha():
            raise WrongUserNameException("user name must be started by character.")
        self.__username = value

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypePassWordException("password must be 'string'.")
        if len(value) < 8:
            raise WrongPassWordException()
        if value.isnumeric():
            raise TypePassWordException()
        self.__password = value


        
class Customers(Users):

    @property
    def wallet_digital(self):
        return self.__walletdigital

    @wallet_digital.setter
    def wallet_digital(self, value):
        if not isinstance(value, int):
            raise ValueError("wallet_digital must be 'amount'")
        self.__walletdigital = Value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise ValueError("phone must be 'string'.")
        if not value.isnumeric():
            raise TypeError("password must be 'number'. ")
        if not value[0] == '0':
            raise ValueError("the first number must be '0'.")
        if len(value) < 11:
            raise ValueError("the phone number must be include '11' number")
        self.__phone = value

    def login(self, username, password):
        is_authenticated = False
        if self.username == username and self.password == password:
            is_authenticated = True
        return is_authenticated
    def register(self, username:str, password:str, phone:str, walletdigital:int)-> None:
        self.username = username
        self. password = password
        self.phone = phone
        self.walletdigital = walletdigital


    
        

    


