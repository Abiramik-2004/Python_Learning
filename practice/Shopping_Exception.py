class OutOfStockErr(Exception):
    pass
products={
    "laptop":{"price":55000,"stock":3},
    "mouse":{"price":800,"stock":10}

}
cart=[]
while True:
    print("======Shopping cart ===========")
    print("1.View Products")
    print("2.Add Product")
    print("3.View product")
    choice=int(input("enter your choice"))
    try :
        if choice==1:
            for name , details in products.items():
                print(name,details["price"],details["stock"])
        elif choice==2:
            name=input("enter product name ").lower()
            if name not in products:
                print("product not found")
                continue
            quantity=int(input("enter quantity "))
            if quantity <=0:
                raise OutOfStockErr("quantity cannot be 0 or -ve")
            cart.append([name, quantity])
            products[name]["stock"]-=quantity
        else:
            if not cart:
                print("cart is empty ")
                continue
            total=0
            print("===cart===")
            for i in cart :
                name=i[0]
                quantity=i[1]
                price=products[name]["price"]
                amout=price*quantity
                total+=amout
                print(name,"x",quantity,"=",amout)
                print("toatl",total)
    except Exception as e :
        print(e)
