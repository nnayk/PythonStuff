class MagicMethod:
    def __str__(self):
        print("africa")
        return "how are?"

obj = MagicMethod()
value = str(obj)
print(obj)

#conclusion: __str__ method called when str() used on object or print used on object


