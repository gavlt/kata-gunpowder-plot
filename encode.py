def g(message,carrier):
 if sum(c.isalpha()for c in carrier)/5 < len(message):
  raise ValueError("message is too long for the carrier")
 c=carrier.lower();w=[h.upper()if h.isalpha()else '['for h in message];t=''.join("{:05b}".format(ord(i)-65)for i in w);r='';j=m=0
 while t[j:]:a=c[m];x=a.isalpha();r+=[a,a.upper()][x*int(t[j])];j+=x;m+=1
 return r+c[m:].upper()
