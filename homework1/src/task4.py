#Task4.py

#Calculate Discount
def calculate_discount(price,discount):

    #Check if int or float if so calaute discount
    if isinstance(price,(int,float)) and isinstance(discount,(int,float)):
        discountprice = price - (price * discount / 100)
        return discountprice
    #Else raise a value error
    else:
        raise ValueError("Please enter a numeric either float or int for price discount")

