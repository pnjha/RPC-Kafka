class Server:

    def __init__(self):
        self.products = {}
        self.products["laptop"] = 2
        self.products["mouse"] = 10
    
    def get_items_list(self):
        print(self.products)
        return self.products

    def buy(self,product_name):
        if product_name not in self.products:
            return 0
        print("product_name: ",product_name)
        print(self.products)
        if self.products[product_name] > 0:
            self.products[product_name] -= 1
            print(self.products)
            return 1
        print(self.products)
        return 0
