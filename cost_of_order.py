#PROBLEM
# The coffee shop in the library sells coffee for $10.50 a pound plus the cost of shipping.  
# Each order ships for $0.86 per pound plus $1.50 fixed cost for overhead.  
# Write a function that calculates the cost of an order given the number of pounds ordered.

#precondition
# cannot order less than one pound(ie a fraction or decimal)
# order must be a positive integer

#postcontion
# total cost for order

#ALGORITHM
#find total cost of one pound 
    #add shiping cost per pound, overhead cost and selling price
# multiply it by number of pounds ordered



def costing(pounds: int)->float:
    #trying to put a condition to make sure argument is positive, greater than 0 and an integer
    # succeeded in doing all but one--> making sure the input is an integer, adding- and int -to the condition did'nt change it
    
    if pounds > 0 :
        a_pound = 0.86 + 1.50 + 10.50
        cost = pounds * a_pound
    else:
        return 'Sorry, wrong figure.'
    return cost

print(costing(2.57))