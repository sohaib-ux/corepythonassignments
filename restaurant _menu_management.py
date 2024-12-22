def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)

def check_item(menu, item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")

menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(menu, "Tacos")
remove_item(menu, "Salad")
check_item(menu, "Pizza")
print(menu)
