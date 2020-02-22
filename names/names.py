import time

# Rationale for this explained below
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return

        elif self.value is None:
            self.value = value
        
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        
        if self.right:
            self.right.for_each(cb)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# This solution is likely O(n^2) in worst case because you have two nested for loops
#for name_1 in names_1:
 #   for name_2 in names_2:
  #      if name_1 == name_2:
   #         duplicates.append(name_1)


# My Solution Starts Here

# Let's use a binary tree because: 
# 1) search/lookup is O(log (n))
# 2) strings can be greater or lesser than other strings (or equal) "apple" > "Apple" 

names_list = BinarySearchTree(names_1[0]) 

for name in names_1[1:]: 
    names_list.insert(name) #Worst case is O(n), best is O(log(n))

for name2 in names_2: #O(n)
    if names_list.contains(name2): #Worst case is O(n), but best is O(logn)
        duplicates.append(name2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


"""
# Wrote a little test of the outputs to make sure things weren't off
old_names_way = set('Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier'.split(", "))

new_names_way = set('Ahmad Watts, Franklin Cooper, Jaydin Sawyer, Sanai Harrison, Jaden Hawkins, Cloe Norris, Pablo Berg, Giancarlo Warren, Camryn Doyle, Aleah Valentine, Grace Bridges, Daphne Hamilton, Irvin Krause, Justine Soto, Josie Cole, Winston Austin, Ashlee Randall, Leon Cochran, Kale Sawyer, Alvaro Robbins, Malcolm Tucker, Jadyn Mays, Josie Dawson, Clay Wilkinson, Logan Morrow, Salma Meza, Trace Gates, Hayley Morgan, Dulce Hines, Abel Newman, Nathalie Little, Zara Suarez, Leia Foley, William Maldonado, Marley Rivers, Addison Clarke, Kameron Osborne, Aydan Calderon, Ali Collier, Marisol Morris, Peyton Lloyd, Eden Howe, Victoria Roach, Dashawn Green, Carley Gallegos, Selah Hansen, Hallie Vazquez, Piper Hamilton, Lennon Hunt, Andre Carrillo, Devyn Aguirre, River Johnson, Maliyah Serrano, Diego Chaney, Davion Arias, Nelson Acevedo, Malcolm Nelson, Raven Christensen, Luciana Ford, Amiah Hobbs, Megan Porter, Carsen Tyler, Jordin Schneider, Ralph Roth'.split(", "))
print (len(new_names_way))
print (len(old_names_way))
print (new_names_way == old_names_way) #NB: I had to split on ", " space because the order is different in either list
"""

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
