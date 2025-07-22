Stack=[]
def insert(item):
    Stack.append(item)
def remove():
    Stack.pop()


while True:
    while True:
        print("Stack operations:")
        print("1. Insert item")
        print("2. Remove item")
        print("3. Display Stack")
        print("4. Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            item=input("Enter item to insert: ")
            insert(item)
            print(f"Inserted {item} into Stack.")     
            break
        elif choice==2:
            remove()
            print("Removed first item from queue.")
            break
        elif choice==3:
            print("Current Stack:", Stack)
            break
        elif choice==4:
            print("Exiting...")
            break
    break    