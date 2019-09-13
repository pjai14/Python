def lists():
    thislist = ["apple", "banana", "cherry","Mango", "Orange"]
    print("This list contains fruits: "+ str(thislist))
    a=int(input("Select the one of the following operations \n 1. Length of the list \n 2. Add a fruit to the list\n 3. Remove a fruit from the list\n 4. Add an element to a specified position\n 5. Clear the list"))
    if a==1:
    	print("The length of the list is: " + str(len(thislist)))
    if a==2:
    	b=input("Enter the fruit you want to add to the list: ")
    	thislist.append(b)
    	print("Item added!")
    	print("Your updated list is: "+ str(thislist))
    if a==3:
    	b=input("Enter the fruit you want to remove from the list: ")
    	thislist.remove(b)
    	print("Item removed!")
    	print("Your updated list is: "+ str(thislist))
    if a==4:
    	b=int(input("Enter the position: "))
    	c=input("Enter the fruit: ")
    	thislist.insert(b,c)
    	print("Item added to the specified position")
    	print("Your updated list is: "+ str(thislist))
    if a==5:
    	b=input("Are you sure you want to claer the list? [Y/N]")
    	if b=='Y':
    		thislist.clear()
    		print("Your list has been cleared")  
    	else:
    	   print(thislist)

def tuples1():
    thistuple = ("Carrrot", "cauliflower", "Onions")
    print("This tuple contains Vegetables: "+ str(thistuple))
    a=int(input("Select the one of the following operations \n 1. Length of the tuple \n 2. Change the tuple value\n 3. Delete the tuple\n 4. Join 2 tuples\n "))
    if a==1:
    	print("The length of the tuple is: " + str(len(thistuple)))
    if a==2:
    	y=list(thistuple)
    	b=int(input("Enter the index of the veggie you want to change: "))
    	c=input("Enter the vegetable name: ")
    	y[b]=c
    	thistuple=tuple(y)
    	print("Your updated tuple is: " +str(thistuple))
    if a==3:
        del thistuple
        print("Your tupple has been deleted")
    if a==4:
        thattuple=('pumpkin','Green peas')
        tuple1=thistuple+thattuple
        print("Here is another tuple"+ str(thattuple))
        print("Joining the two tuples gives you:  "+ str(tuple1))

def sets1():
    sets={'Black','white','yellow','blue'}
    print("this set contains colors: " + str(sets))
    a=int(input("Select the one of the following operations \n 1.Add item to the set\n 2. Update the set\n 3. Length of the set\n 4. Remove an item from the set\n 5. Union of two sets\n"))
    if a==1:
        b=input("Enter the color you want to add to the set")
        sets.add(b)
        print("Your updated set is:  " + str(sets))
    if a==2:
        sets2={"grey","purple","violet"}
        print("Your first set is: "+ str(sets))
        print("Your second set is: "+ str(set2))
        sets.update(sets2)
        print("Updation of two sets is: "+str(sets))
    if a==3:
        print("the length of the set is: " + str(len(sets)))
    if a==4:
        b=input("Enter the color you want to remove from the list: ")
        sets.remove(b)
        print("Your updated list is: " + str(sets))
    if a==5:
        sets2={"grey","purple","violet"}
        print("Your first set is: "+ str(sets))
        print("Your second set is: "+ str(set2))
        sets.union(sets2)
        print("Union of two sets is: "+str(sets))

def dict1():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print("this dictionary contains: "+ str(thisdict))
    a=int(input("Select the one of the following operations \n 1.Value of a key \n 2. Change value of a specific key\n 3. Add a new attribute\n 4. Pop()"))
    if a==1:
        b=input("Enter the key: ")
        x = thisdict[b]
        print("the value is: "+ str(x))
    if a==2:
        b=input("Enter the key: ")
        c=input("Enter the value: ")
        thisdict[b]=c
        print("The values now are: "+ str(thisdict))
    if a==3:
        b=input("Enter the key: ")
        c=input("Enter the value: ")
        thisdict[b]=c
        print("The values now are: "+ str(thisdict))
    if a==4:
        b=input("Enter the key you want to pop(): ")
        thisdict.pop(b)
        print(thisdict)
lists()
tuples1()
sets1()
dict1()











