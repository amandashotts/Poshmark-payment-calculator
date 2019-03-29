poshfee = 0

def poshmarkfees(myprice):
  # How much money they rip out of my soul:
  if myprice < 15:
    poshfee = 2.95
  if myprice >= 15:
    poshfee = 0.2 * myprice
  profit = myprice - poshfee
  post_shipping = poshfee + 6.79
  consumer_price = myprice + 6.79
  print('If I list my item for: $' + str(myprice) +':')
  print('Poshmark will eat up $' + str(poshfee) + ' of my money in fees.')
  print('That will leave me with $' + str(profit) + ' in profit.')
  print()
  print('After fees and shipping, I will have a starting bid of $' + str(post_shipping) + ' to work with.' )
  print('From a buyer standpoint, it seems like my total price is actually: $' + str(consumer_price) + '.')
  print()


def get_avg(*price):
  # Arguments are as many average prices that are posted for the same item:
  total_prices = sum(price) 
  avg_price = total_prices / len(price)
  print('The average going price for this item is: $' + str(avg_price) + '.')


poshmarkfees(3)
get_avg(4,6)

"""
Okay above this line 
"""

