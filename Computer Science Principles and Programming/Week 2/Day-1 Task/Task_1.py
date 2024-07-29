int_val = 1
print("Initial integer variable:", int_val)
int_val = 2 # Changed the int value to 2
print("Changed integer value:",int_val)

float_val = 1.1
print("Initial float value:", float_val)
float_val = 2.2 # Changed the float value to 2.2
print("Changed float value:", float_val)

string_val = "MS"
print("Initial string value:", string_val)
string_val = "MSIT" # Changed the string value to MSIT
print("Changed string value:", string_val)

a = 100
b = 0
print("Before swap:", "a =", a ,"b =" ,b)
a, b = b, a # Swapping the numbers
print("After swap:", "a =" , a, "b =" ,b)