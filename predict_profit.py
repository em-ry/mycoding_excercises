#problem
# Predict the profit to be made with after sale given a proposed price 2.0 and 3.0.

#precondition
# The proposed price has to be 2.0 or 3.0

#postcondition
# return profit made

#ALGORITHM
#calculate gross amount
#calculate total transaction cost
    # $0.50 per purchase
#calculate profit from refunds
    #refund rate = 5%
#calculate profit without refund    
#calculate total profit
#return total profit



def calculate_profit(app_price:float)->float:
    #if not isinstance(app_price,2 or 3): 
    if app_price != 2.0 and app_price != 3.0:
    #if 2.0 > app_price > 3.0:
    #if app_price < 2 and app_price > 3:

    # can't get my conditions to work properly
    # i have finally fixed it by using the -- and -- ,what i still don't understand is why the other conditions did not work.
        return 'Sorry, price not accounted for.'
        
    elif app_price == 2.0:
            tot1 = app_price * 1000
            trans_cost = 0.5 * 1000
            refund_prof = 0.05 * tot1
            prof = tot1 - trans_cost
            tot_prof = prof + refund_prof
            return tot_prof


    elif app_price == 3.0:
            tot2 = app_price * 700
            trans_cost = 0.5 * 700
            refund_prof = 0.05 * tot2
            prof = tot2 - trans_cost
            tot_prof = prof + refund_prof
            return tot_prof

        
test = float(input('app price: '))

if type(calculate_profit(test)) == str:
    print(calculate_profit(test))
else:    
    print('Your profit is: ',calculate_profit(test))