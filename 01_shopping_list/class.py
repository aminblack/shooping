class Users:

    all_username = []
    all_password = []

    def __init__(self, name: str, username: str, password: str, amount: int = 0) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.walletdigital = amount
        Users.all_username.append(self.username)
        Users.all_password.append(self.password)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name},{self.username},{self.password},{self.walletdigital})'

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("name must be 'character'.")
        self.__name = value
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("username must be 'string'.")
        if not value[0].isalpha():
            raise ValueError("user name must be started by character.")
        self.__username = value

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("password must be 'string'.")
        if len(value) < 8:
            raise ValueError("password must be mor than 8 'character'.")
        if value.isnumeric():
            raise ValueError("password must be 'number' and 'character'. ")
        self.__password = value

    @property
    def wallet_digital(self):
        return self.__walletdigital

    @wallet_digital.setter
    def wallet_digital(self, value):
        if not isinstance(value, int):
            raise ValueError("wallet_digital must be 'amount'")
        self.__walletdigital = Value

        


        

    


