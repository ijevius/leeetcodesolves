a = 0
if x < 0:
  a = -int(''.join(reversed(str(x)))[:-1])
else:
  a = int(str(x)[::-1])            
if a > 2**31-1 or a < -(2**31): a = 0            
return a
