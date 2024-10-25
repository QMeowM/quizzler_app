"""pre-define the data type to get hints if inputting a wrong type later on"""
"""can be used in and outside of functions, and for input(: type) and output(-> type)"""

# i.e.
def greeting(name: str) -> str:
    return "Hello" + name

greeting("Ali")
greeting(897)