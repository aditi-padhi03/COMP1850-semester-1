# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]



newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

# write the list comprehension equivalent to the `for` loop
new_values = [(2*i) if i % 2 == 0 else i for i in values]
# We cant use "newval.append()" inside a list comprehension because it adds a value to the list but returns "None"
# Also you don't need append() because the list comprehension builds the new list automatically.
print(new_values)
