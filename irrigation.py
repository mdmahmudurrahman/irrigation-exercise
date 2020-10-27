import datetime as DT

def irrigation():
    # Override you radiation value here
    radiation = 100
    if exceed(radiation):
        return print("Irrigation Started.")

    return print("Not started")

def exceed(radiation_value):
  if radiation_value > 92.3 : 
    if check_time():
      return True
    else: 
      return False 
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