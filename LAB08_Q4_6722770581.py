x = " "
d = {}
while x != "DONE":
    x  = input("Input (DONE = exit): ")
    if x != "DONE":
        try:
            a,b = x.split(" ")
            if not a.isnumeric():
                print('Invalid input')
            elif a in d:
                print("Duplicated ID")
            else:
                d[a] = int(b)
        except:
            print("Invalid input")
sorted = sorted(d.values(), reverse=True)
for i in sorted:
  for key,value in d.items():
    if i == value:
      print(key,value)
