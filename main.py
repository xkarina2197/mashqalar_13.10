# 5-misol
son = 20

while son >= 1:
    print(son, end=" ")
    son -= 1


# 12-misol
text = "programming"
print(text)
print(text[::-1])


# 20-misol
animals = ("mushuk", "it", "ot", "quyon")
print(animals)
print()

for i in animals:
    print(i)

# 27-misol
phone = {
    "brend": "Samsung",
    "model": "A55",
    "xotira": "256GB"
}

for key, value in phone.items():
    print(f"{key}: {value}")


# 36-misol
def katta_son(a, b):
    return max(a, b)

a = katta_son(45, 87)
print(f"katta son: {a}")

# 37-misol
def mahsulot_narxi(narx):
    if narx > 100000:
        return "qimmat"
    else:
        return "oddiy narx"

a = mahsulot_narxi(150000)
print(f"mahsulot: {a}")
