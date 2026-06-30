def say_hello(name):
    print(f"Bonjour {name} !")
    print("Comment vas-tu ?")



say_hello("Jerem")

def add_print(a,b):
    print(a + b)
add_print(1,2)

def add_return(a,b):
    return a + b
add_return(5,6)

result = add_return(2,3)

print(result * 10)

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 +32

temp_celsius = 32
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"Aujourd'hui il fait {temp_celsius} degrés celsius, ce qui correspond à {temp_fahrenheit} degrés fahrenheit")

def compute():
    secret = 42
    print(secret)
compute()
