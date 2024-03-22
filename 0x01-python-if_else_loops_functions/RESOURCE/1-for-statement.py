#!/usr/bin/python3

# create a sample collection
users = {'Hans': 'active', 'Gretel': 'inactive', 'Witch': 'active'}

# before
print(f"before: {users}")

# strategy 1: iterate over the collection copy
for user, status in users.copy().items():
		if status == 'inactive':
				del users[user]
print("deleting inactive users from the collection")

# strategy 2: create a new collection
active_users = {}
for user, status in users.items():
		if status == 'active':
				active_users[user] = status

# print
print(f"After: {users}")
print(f"active_users: {active_users}")

"""
code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
"""
