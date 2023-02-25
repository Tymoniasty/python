"""
Building on the previous example, let's also assume that you have saved $918 to fund your new
adventure. You wonder how many days you can keep one server running before your money
runs out. Of course, you hope your social network becomes popular and requires 20 servers to
keep up with the demand. How much will it cost to operate at that point?
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
How much does it cost to operate twenty servers per day?
How much does it cost to operate twenty servers per month?
How many days can I operate one server with $918?
"""
priceperhour = 0.51
daycost = priceperhour * 24
monthcost=daycost*30

print("If server cost = ", end="")
print("$", priceperhour, " per hour. ", sep="", end="")
print("Then:")
print("- daily cost for one server = $",daycost, sep="")
print("- monthly cost for one server = $", monthcost, "*", sep="")
print("\n *assuming that a month has 30 days!")

x20dailycost = daycost * 20
x20monthlycost = monthcost * 20

print("If server cost = ", end="")
print("$", priceperhour, " per hour. ", sep="", end="")
print("Then:")
print("- daily cost for 20 servers = $",x20dailycost, sep="")
print("- monthly cost for 20 servers = $", x20monthlycost, "*", sep="")
print("\n *assuming that a month has 30 days!")

savings = 918
x1days = savings / daycost
x20days = savings / (daycost * 20)

print("\n With $", savings, " ", sep="",end="")
print("savings, you can operate one server for ",x1days, "days!")
 
print("\n With $", savings, " ", sep="",end="")
print("savings, you can operate 20 servers for ",x20days, "days!")

"""
# The cost of one server per hour.
cost_per_hour = 0.51
# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
# Compute the costs for twenty servers
cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month
# Budgeting
budget = 918
operational_days = budget / cost_per_day
# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))
print('Cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))
print('Cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))
"""