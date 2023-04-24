# contoh 1
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# contoh 2
names = ["Riolan", "David", "Febri"]
greetings = list(map(lambda x: f"Hello, {x}!", names))
print(greetings)
