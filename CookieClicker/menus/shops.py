def shops(sa):
    while True:
        print("What you have:")
        print("Cookies: " + str(sa["cookies"]))
        for key, value in sa["items"].items():
            print(f"{key}: {value}, price:{int(sa['items']['grandma']) * 0.28 + 10}")
        userIn = input("What would you like to buy? ")
        if userIn.lower() == "grandma":
            if sa["cookies"] >= 10 + (int(sa["items"]["grandma"])*0.28):
                sa["cookies"] -= 10
                sa["items"]["grandma"] += 1
            else:
                print("You don't have enough cookies!")
        if userIn.lower() == "close":
            return sa
            break
        
        