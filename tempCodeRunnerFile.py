gryffindor = 0
Ravenclaw = 0
HUfflepuff = 0
Slytherin = 0

print("QUIZ")

print("""Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk""")
ans = int(input("enter the ans :"))    
if ans == 1:
  gryffindor = gryffindor+1
  Ravenclaw = Ravenclaw+1
elif ans ==2:
  HUfflepuff = HUfflepuff+1
Slytherin = Slytherin+1
else:
  print("WRONG INPUT")
  
