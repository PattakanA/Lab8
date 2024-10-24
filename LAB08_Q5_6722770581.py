txt = {}
sen = input("Input a sentence: ").split()
for i in sen:
  if i.lower() in txt:
    txt[i.lower()] += 1
  else:
    txt[i.lower()] = 1
print("Output:")
for key,value in txt.items():
  if value > 1:
    print(key)
if max(txt.values()) == 1:
  print("none")