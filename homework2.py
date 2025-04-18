#Tapsiriq 2
def greeting():
    name = input("Adını daxil et: ")
    
    print(f"Salam, {name}! Xoş gəldin.")

greeting()

##########################################################################

def sum_numbers(a, b):
    return a + b

result = sum_numbers(5, 7)
print(result)

########################################################################

def calculate_average(values):
    return sum(values) / len(values)

numbers = [10, 20, 30, 40, 50]

result = calculate_average(numbers)
print(result)

