#Tapsiriq 6
def choose_coffee_type():
    print("Zəhmət olmasa kofe növünü seçin:")
    print("1. latte")
    print("2. cappuccino")
    print("3. espresso")
    coffee = input("Seçiminizi yazın (latte/cappuccino/espresso): ").lower()
    return coffee
coffee= choose_coffee_type()
print("Sifarisiniz:", coffee)

####################################################################################

def choose_size():
    print("Zəhmət olmasa ölçü seçin:")
    print("1. single")
    print("2. double")
    size = input("Seçiminizi yazın (single/double): ").lower()
    return size
size= choose_size()
print("Sifarisiniz:", size)


###################################################################################

def brew_coffee(coffee_type, size):
    if coffee_type is None or coffee_type not in ["latte", "cappuccino", "espresso"]:
        print("Xəta: Etibarsız kofe növü seçildi.")
        return

    if size == "double":
        coffee_amount = 50
    else:
        coffee_amount = 25

    print(f"{coffee_amount} qram qəhvə istifadə olunur.")

    if coffee_type == "latte":
        print("150 ml süd əlavə olunur.")
    elif coffee_type == "cappuccino":
        print("100 ml süd və köpük əlavə olunur.")
    else:
        print("Süd əlavə olunmur.")

    print(f"Sizin {size} ölçülü {coffee_type} ")
coffee = choose_coffee_type()
size = choose_size()
brew_coffee(coffee, size)
