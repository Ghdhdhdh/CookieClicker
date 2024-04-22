
import os.path
import menus.help as help
import menus.shops as shop
import json
import time
import threading
if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        save = json.load(f)
else:
    with open("save.txt", 'w') as f:
        print("Hiya! I see your new here. Here is a tutorial.")
        print(help.help())
        save = {"cookies": 0, "items": {}}
        save["items"]["grandma"] = 0
        json.dump(save, f)
        
save_count = 0
def main():
    global save_count
    global save
    global close
    while True:
        try:    
            save_count += 1
            userIn = input("")
            if userIn.lower() == "help":
                print(help.help())
            if userIn == "":
                save["cookies"] += 1
            if userIn == "shop":
                save = shop.shops(save)
            if save_count == 10:
                save_count = 0
                with open("save.txt", "w") as f:
                    json.dump(save, f)
                    print("Saved!")
        except (KeyboardInterrupt, EOFError):
            with open("save.txt", "w") as f:
                json.dump(save, f)
                print("Saved!")
                print("You can close the window now.")
        print(f"Cookies: {save['cookies']}")
def cookieAdder():
    while True:
        total_cookies = 0
        total_cookies += (int(save["items"]["grandma"])*2)
        save["cookies"] += total_cookies
        time.sleep(1)

x = threading.Thread(target=main)
y = threading.Thread(target=cookieAdder)


x.start()
y.start()
