
inp1 = input("Input sequence1: ").split()
inp2 = input("Input sequence2: ").split()
seq1 = set()
seq2 = set()
for x,y in zip(inp1,inp2):
  if x.isnumeric():
    seq1.add(x)
  if y.isnumeric():
    seq2.add(y)
if len(seq1&seq2) != 0:
  print("Output: True")
else:
  print("Output: False")