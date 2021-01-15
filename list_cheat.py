

#EX FOR CUBES WORKS FOR SQUARES CHANGE 3 TO 2

#lizt = [k**3 for k in range(11)]
#print(lizt)
##################################################################################
# EX OF STEPS FOR TRUE PALINDROM

#def isPalindrome(string):
	#left_pos = 0
	#right_pos = len(string) - 1
	
	#while right_pos >= left_pos:
		#if not string[left_pos] == string[right_pos]:
			#return False
		#left_pos += 1
		#right_pos -= 1
	#return True
#rint(isPalindrome('racecar')) 


# LONG DADDY WAY palindrome 

#my_str = 'aIbohPhoBiA'
# make it suitable for caseless comparison
#my_str = my_str.casefold()
# reverse the string
#rev_str = reversed(my_str)
# check if the string is equal to its reverse
#if list(my_str) == list(rev_str):
   #print("The string is a palindrome.")
#else:
   #print("The string is not a palindrome.")
#################################################################################
# Ex Inheritance You can create a child-parent relationship between two classes 
# by using inheritance. What this allows you to do is have overriding methods, 
# but also inherit traits from the parent class. 
# Think of it as an actual parent and child, the child will inherit the parent's genes, 
# as will the classes in OOP

#class Animal():
    #acceleration = 9.8
    
    #def __init__(self,name,species,legs=4):
        #self.name = name
        #self.species = species
        #self.legs = legs
    #def makeSound(self):
        #print("Some Generic Sound")
        
#class Dog(Animal):
    #speed = 15
    
    #def __init__(self,name,species,color,legs=4):
        #Animal.__init__(self,name,species,legs)
        #self.color = color
        
    #def printInfo(self):
        #print("This Dog is {} and his name is {}".format(self.color,self.name))
        
    #def makeSound(self):
        #print("Bark")
        
#dog = Dog("Max","Canine","Black")

#dog.printInfo()
#dog.acceleration
#dog.speed
#dog.makeSound()
#################################################################################
# Ex of adding or subtracting from base

#     def addNums(num):
#     #set base case here
#     if num <= 1:
#         print("addNums(1) = 1")
#         return num
#     else:
#         print("addNums({}) = {} + addNums({})".format(num,num,num-1))
#         return num + addNums(num-1)
    
# addNums(5)

# Ex celcius to fahranhite
# def ctof(c):
#     f = (9/5)*C + 32
#     return(f)
################################################################################
# Ex NODE Linked list
# class LinkedListNode():
#     def __init__(self,value):
#         self.value = value
#         self.next = None
        
#     def traversedList(self):
#         node = self
#         while node != None:
#             print(node.value)
#             node = node.next
            
# node1 = LinkedListNode("Mon")
# node2 = LinkedListNode("Tues")
# node3 = LinkedListNode("Wed")
# node4 = LinkedListNode("Thurs")
# node5 = LinkedListNode("Fri")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# node1.traversedList()
###############################################################################################
# EX RANDOM NUMBER GENERATOR (LICENCE CRACKING *COUGH *COUGH)

# Step 1: Split everything into it's own group
# Step 2: From left to right merge two groups together
# Step 3: While merging, place each item in the correct position within the merged group
# Step 4: Continue steps 3-4 until one group is left

# from random import randint
# # used to generate a random list of 10 numbers from 0 to 100
# nums = [randint(0, 20) for i in range(5)]
# # write merge sort

# def mergeSort(alist):
#     print("Splitting: ", alist)
#     # Step 1: Divide and conquer - Divide the list into equal halves
#     if len(alist) > 1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]
        
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
        
#         # Index Pointers for our list
#         i = 0
#         j = 0
#         k = 0
        
#         #Step 2 - Compare the lefthalf and righthalf
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 alist[k] = lefthalf[i]
#                 i = i + 1
#             else:
#                 alist[k] = righthalf[j]
#                 j = j + 1
#             k = k + 1
#             # Step 3 - Check both halves and sort in a one -off situation for the halves
#         while i < len(lefthalf):
#             alist[k] = lefthalf[i]
#             i = i + 1
#             k = k + 1
#         while j < len(righthalf):
#             alist[k] = righthalf[j]
#             j = j + 1
#             k = k + 1
#     print("Merging: ", alist) # step 4
#     return alist
    
# mergeSort(nums)    