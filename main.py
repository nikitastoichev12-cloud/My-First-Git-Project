
from functions import calc, change_text, sum_numbers




print(calc(10, 5, "sub"))


print(calc(a=10, b=5, operation="sum"))


args1 = {"a": 20, "b": 10, "operation": "sub"}
print(calc(**args1))




print(change_text("Hello"))

print(change_text(text="Hello world", upper=False))

args2 = {"text": "Python test", "upper": True}
print(change_text(**args2))




print(sum_numbers("1,2,3"))

print(sum_numbers(numbers="10,20,30", separator=","))

args3 = {"numbers": "5,5,5", "separator": ","}
print(sum_numbers(**args3))