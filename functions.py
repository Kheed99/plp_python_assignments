def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        print("The discount is ", discount_percent/100*price)
        print("The discounted price is ",(price)-discount_percent/100*price)
    else:
        return price

calculate_discount(100,20)