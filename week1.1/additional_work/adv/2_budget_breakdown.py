"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""
try:
    travel_cost_input = int(input("Travel cost in pounds: "))
    food_cost_input = int(input("Food cost in pounds: "))
    accommodation_cost_input = int(input("Accommodation cost in pounds: "))
    total = travel_cost_input+food_cost_input+accommodation_cost_input
    average = total/3
    print(f"Your travel cost is {travel_cost_input} pounds, food cost is {food_cost_input} pounds, accomodation cost is {accommodation_cost_input} pounds. Hence your total cost is {total:.2f} pounds, and average cost is {average:.2f} pounds.")
except: 
    print("This is not a number.")
# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places
