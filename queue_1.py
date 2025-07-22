queue=[]

def insert(item):
    queue.append(item)

def remove():
    queue.pop(0)
    

while True:
    while True:
        print("Queue operations:")
        print("1. Insert item")
        print("2. Remove item")
        print("3. Display queue")
        print("4. Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            item=input("Enter item to insert: ")
            insert(item)
            print(f"Inserted {item} into queue.")     
            break
        elif choice==2:
            remove()
            print("Removed first item from queue.")
            break
        elif choice==3:
            print("Current queue:", queue)
            break
        elif choice==4:
            print("Exiting...")
            break
    break    