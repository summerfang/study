from optionprice import Option

# Initialize an option (European call in this case)
some_option = Option(european=True, kind='call', s0=100, k=120, t=45, sigma=0.01, r=0.05, dv=0)

# Calculate option price
price = some_option.getPrice()  # Default method is B-S-M

print(price)
