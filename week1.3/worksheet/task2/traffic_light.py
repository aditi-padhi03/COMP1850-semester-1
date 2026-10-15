"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(40)  # read an integer number of steps (>0)

state = "red"
state_2 = "red_amber"
state_3 = "green"
state_4 = "amber"

# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime < 4:
    print(f"Time {systime:03} State {state}")
    systime += 1

while systime < 7:
    print(f"Time {systime:03} State {state_2}")
    systime += 1

while systime < 12:
    print(f"Time {systime:03} State {state_3}")
    systime += 1

while systime < 15:
    print(f"Time {systime:03} State {state_4}")
    systime += 1

while systime < 19:
    print(f"Time {systime:03} State {state}")
    systime += 1

while systime < 22:
    print(f"Time {systime:03} State {state_2}")
    systime += 1

while systime < 27:
    print(f"Time {systime:03} State {state_3}")
    systime += 1

while systime < 30:
    print(f"Time {systime:03} State {state_4}")
    systime += 1

while systime < 34:
    print(f"Time {systime:03} State {state}")
    systime += 1

while systime < 37:
    print(f"Time {systime:03} State {state_2}")
    systime += 1

while systime <= 40:
    print(f"Time {systime:03} State {state_3}")
    systime += 1




    
    

# At the end of each step you should output the time and state using the statement on line 14