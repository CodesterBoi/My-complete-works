from tabulate import tabulate

data = {
        "Product Name": ["Coffee Powder", "Sugar", "Rice", "Tea Bags"],
        "Retail Price": [6, 10, 15, 3],
        "Selling Price": [10, 12, 17, 5],
        "Vendor Details": ["Scott", "Dustin", "James", "Bridge"],
        "Quantity": [10, 15, 15, 10]
        }

InventoryDetails = tabulate(data,headers = "keys",tablefmt = "github")

class Inventory:
    def __init__(self, ProductName = '', RetailPrice = 0, SellingPrice = 0, VendorDetails = 'NA', Quantity = 0):
        self.ProductName = ProductName
        self.RetailPrice = RetailPrice
        self.SellingPrice = SellingPrice
        self.VendorDetails = VendorDetails
        self.Quantity = Quantity

    def add_new(self):
        data["ProductName"].append(self.ProductName)
        data["RetailPrice"].append(self.RetailPrice)
        data["SellingPrice"].append(self.SellingPrice)
        data["VendorDetails"].append(self.VendorDetails)
        data["Quantity"].append(self.Quantity)

    def remove(self,ProductName,Quantity):
        self.ProductName = ProductName
        ProductName_Index = data['ProductName'].index(self.ProductName)
        del data['ProductName'][ProductName_Index]
        del data['RetailPrice'][ProductName_Index]
        del data['SellingPrice'][ProductName_Index]
        del data['VendorDetails'][ProductName_Index]
        del data['Quantity'][ProductName_Index]

    def update(self,ProductName,Quantity):
        self.ProductName = ProductName
        self.Quantity = Quantity
        ProductName_Index = data['ProductName'].index(self.ProductName)
        data['Quantity'][ProductName.index] = data['Quantity'][ProductName_Index] - self.Quantity

    def add_stock(self,ProductName,Quantity):
        self.ProductName = ProductName
        self.Quantity = Quantity
        ProductName_Index = data['ProductName'].index(self.ProductName)
        data['Quantity'][ProductName_Index] = data['Quantity'][ProductName_Index] + self.Quantity

    def get_productname_list(self):
        global productname_list
        productname_list = data['ProductName']
        return productname_list

print("Welcome to your Inventory Management System.")
print("Inventory details are:")
print(InventoryDetails)
print("A/a - Add a new product.")
print("R/r - Remove current product.")
print("S/s - Sell a product.")
print("U/u - Add stock.")
print("Q/q - Quit.")

v = 0

while (v != "Q" or v != "q"):
    v = input("What would you like to do: ")

    if (v == "Q" or v == "q"):
        break

    elif (v == "A" or v == "a"):
        p_name = input("Enter the product name: ")
        p_retail_price = input("Enter the retail price: ")
        p_selling_price = input("Enter the selling price: ")
        p_vendor_details = input("Enter the vendor details: ")
        p_quantity = input("Enter the product quantity: ")

        inventoryObj = Inventory(p_name, p_retail_price, p_selling_price, p_vendor_details, p_quantity)
        inventoryObj.add_new()
        print("New product added successfully. New details are: ','")
        updated_inventory_details = tabulate(data,headers = "keys", tablefmt = "github")
        print(updated_inventory_details)

    elif (v == "S" or v == "s"):
        inventoryObj1 = Inventory()
        p_name  = input("Enter the product name:")
        
        if(p_name in inventoryObj1.get_productname_list()):            
            p_quantity = int(input("Enter the quantity that you want to sell:"))
            inventoryObj1.update(p_name,p_quantity)
            print("Product quantity updated successfully. The new details are:")
            InventoryDetails = tabulate(data,headers = "keys",tablefmt = "github")
            print(InventoryDetails)            
            
        else:
            print("{0} is not present in Product name list".format(p_name))

    elif(v == "R" or v == "r"):
        inventoryObj1 = Inventory()
        p_name= input("Enter the product name: ")
        if(p_name in inventoryObj1.get_productname_list()):
            inventoryObj1.remove(p_name)
            print("Product has been removed successfully.new inventory details are:")
            InventoryDetails = tabulate(data,headers = "keys",tablefmt = "github")
            print(InventoryDetails)
        else:
            print("{0} is not present in Product name list".format(p_name))

    elif(v == "U" or v == "u"):
        p_name= input("Enter the product name: ")
        inventoryObj1 = Inventory()         
        if(p_name in inventoryObj1.get_productname_list()):             
            p_quantity = int(input("enter the quantity that u want to add"))
            inventoryObj1.add_stock(p_name,p_quantity)
            print("Product's stock has been added successfully. New inventory details are:")
            InventoryDetails = tabulate(data,headers = "keys",tablefmt = "github")
            print(InventoryDetails)             
        else:
            print("{0} is not present in Product name list".format(p_name))

    else:
        print("Invalid input. Plz enter valid input.")

print("Thanks for utilising this Inventory Management System. I bid you an enjoyable rest of the day.")
