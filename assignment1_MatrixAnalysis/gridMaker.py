def main():
   count = 1
   x = []
   n = 4
   for i in range (n):
      y = []
      for j in range (n):
         y.append(count)
         count += 1
      x.append(y)
   print(x)    
main()