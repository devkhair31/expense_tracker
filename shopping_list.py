print("==Welcome shopping list manager====")
shopping_list=[]
while True:
    item_name=input("Enter Your Item: ")
    if item_name=="done":
        break
    shopping_list.append(item_name)

print("Shopping List")
for item in shopping_list:
        print(item)

print(f"Total Item number is: {len(shopping_list)}")

print("==Thank You====")