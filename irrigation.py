import datetime as DT

def irrigation():
    # Override you radiation value here
    radiation = 100
    if(is_exceeded(radiation) and check_time()):
        return print("Irrigation Started.")

    return print("Not started")

def is_exceeded(radiation_value):
  if radiation_value > 92.3 : 
    return True
  else:
    return False

def check_time():
  current_time = DT.datetime.now() 
  today8am = current_time.replace(hour=8, minute=0, second=0, microsecond=0)

  if current_time > today8am :
    return True
  else:
    return False

irrigation()