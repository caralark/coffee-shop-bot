# Define your functions
def coffee_bot():
  print ("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print ("Alright, that's a " + size + " " + drink_type +"!")
  name = input('Can i get your name, please? \n')
  print('Thanks, ' + name + " Your drink will be ready shortly.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n ')
  if res == 'a':
    return "small"
  elif res == 'b':
    return "medium"
  elif res == 'c':
    return "large"
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res= input('what type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n ')
  if res == 'a':
    return iced_coffee()
  elif res == 'b':
    return mocha_opt()
  elif res == 'c':
    return order_latte()
  else: 
    print_message()
    return get_drink_type()
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n')
  if res == 'a':
    return "latte"
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()
        
def iced_coffee():
  res = input('would you like that iced? \n[a] yes \n[b] no \n')
  if res == 'a':
    return 'iced coffee'
  elif res == 'b':
    return 'brewed coffee'
  else:
    print_message()
    return iced_coffee()

def mocha_opt():
  res = input('would you like your mocha: \n[a] hot \n[b] iced \n[c] frozen \n')
  if res == 'a':
    return "mocha"
  elif res == 'b':
    return "iced mocha"
  elif res == 'c':
    return "frozen mocha"
  else:
    print_message()
    return mocha_opt()
# Call coffee_bot()!
coffee_bot()
