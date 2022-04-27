import os
import sys
# import requests

print(sys.version)
print(sys.executable)

print(os.getcwd())


def greet(who_to_greet):
    greeting = f"Hello {who_to_greet}"
    return greeting


print(greet(who_to_greet='Marwen'))
print(greet(who_to_greet='Yasmine'))
