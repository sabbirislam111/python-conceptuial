class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Item:
    def __init__(self, item_name, price, discription, quantity):
        self.item_name = item_name
        self.price = price
        self.discription = discription
        self.quantity = quantity

class shopingBasket:
  
    user_list = []
    user_order_data = {}
    itemDB = {}

    def get_user_list(self):
        return self.user_list

    def create_account(self):
        name = input("Enter your Name: ")
        isNameExist = False
        for user in self.get_user_list():
            if user.username == name:
                isNameExist = True
                print("Accout is already registered !!!")
                break
        if isNameExist == False:
            password = input("Enter your Password: ")
            self.new_user = User(name, password)
            self.user_list.append(self.new_user)
            print("Accout create successfully.")
        
    def add_item_to_cart(self):
        username = input("Enter your Name: ")
        if username in self.user_order_data.keys():
            item_id = input("Enter your Item ID :")
            item_quantity = input("Enter item quantity : ")
            flag = 0
            for i in self.itemDB:
                if i["itemId"] == item_id and i["quantity"] <= item_quantity:
                    print("Item is  available")
                    flag = 1
                if flag == 0:
                    print("Item not available")



        
           
a = shopingBasket()
a.create_account()
print(a.get_user_list())
