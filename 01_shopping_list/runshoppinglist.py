from helper.exceptions import(
    WrongUserNameException,
    TypeUserNameException,
    WrongPassWordException,
    TypePassWordException
)
from auth import Customers

user = Customers()
try:
    username = input("enter username: ")
    password = input("enter password: ")
    phone = input("enter your phone: ")
    walletdigital = input("enter your amount: ")
    user.register(username, password, phone, walletdigital)
except WrongPassWordException as e:
    print(e)
except TypePassWordException as b:
    print(b)
# user1.login(username, password)
# if user1.login(username, password) == True:
#     print("ok")
