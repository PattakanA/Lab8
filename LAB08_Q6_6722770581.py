txt = {}
while True:
  try:
    x = input("Input (DONE = exit): ").split()
    if "DONE" in x:
      break
    else:
      txt[int(x[0])] = int(x[1])
  except:
    print("Invalid input")
print("Output:")
score = sorted(txt.values(),reverse = True) 
for i in score:
  for key, value in txt.items():
    if i == value:
      print(key,value)