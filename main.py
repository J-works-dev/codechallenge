
# -x
# +x
# reminder

def add(a, b):
  a = int(a)
  b = int(b)
  if type(a) is int or type(a) is float:
    pass
  else:
    print("need to put Number!!")
    return
  if type(b) is int or type(b) is float:
    print("Plus:", a, "+", b, "=", a + b)
  else:
    print("need to put Number!!")
  
def minus(a,b):
  if type(a) is int or type(a) is float:
    pass
  else:
    print("need to put Number!!")
    return
  if type(b) is int or type(b) is float:
    print("Minus:", a, "-", b, "=", a - b)
  else:
    print("need to put Number!!")

def multi(a,b):
  if type(a) is int or type(a) is float:
    pass
  else:
    print("need to put Number!!")
    return
  if type(b) is int or type(b) is float:
    print("Times:", a, "*", b, "=", a * b)
  else:
    print("need to put Number!!")

def div(a,b):
  if type(a) is int or type(a) is float:
    pass
  else:
    print("need to put Number!!")
    return
  if type(b) is int or type(b) is float:
    print("Division:", a, "/", b, "=", a / b)
  else:
    print("need to put Number!!")

def neg(a):
  if type(a) is int or type(a) is float:
    print("Negation", a,  "=", -a)
  else:
    print("need to put Number!!")

def power(a,b):
  if type(a) is int or type(a) is float:
    pass
  else:
    print("need to put Number!!")
    return
  if type(b) is int or type(b) is float:
    print("Power:", a, "^", b, "=", pow(a,b))
    print("Power:", a, "^", b, "=", a ^ b) #doesn't work
  else:
    print("need to put Number!!")

def reminder(a,b):
  if type(a) is int or type(a) is float:
    pass
  else:
    print("need to put Number!!")
    return
  if type(b) is int or type(b) is float:
    print("Reminder:", a, "%", b, "=", a % b)
  else:
    print("need to put Number!!")

add("6",3)
minus(9,6)
multi(4,5)
div(6,4)
neg(7)
power(8, 3)
reminder(11, 3)