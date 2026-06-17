# list_update_delete.py
# リストの値を変更・削除する

fruits = ["apple", "banana", "orange"]

print(fruits)

fruits[1] = "grape"
print(fruits)

fruits.remove("orange")
print(fruits)

deleted_item = fruits.pop()
print(deleted_item)
print(fruits)
