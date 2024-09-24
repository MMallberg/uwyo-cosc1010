#Marit Mallberg
#COSC 1010 lab 10
#9/24/2024
#worked with: table mates
#bugs:
#Note: I tried to accept the assignment through Canvas, but when i went to open the codespace on main, it told me that I had hit the max number of codespaces to run.
# I just decided to work from the lab worksheet in this seperate file, I hope that's okay.  

states=["Wyoming", "Colorado", "Montana"]
print(states)
print(states[0])
print(states[-1])
print(f"{states[1].upper()} is south of {states[0].upper()}")

print("Part Two------------------------------------------------------------------------")

states.append("Washington")
states.append("Oregon")
states.append("California")
print(states)

states[-2]="Maine"
print(states)

states[2]="Texas"
print(states)

del states[3]
print(states)

states.remove("Texas")
print(states)

print("Part Three----------------------------------------------------------------------")
sorted(states)
print(sorted(states))
print(states)

states.sort(reverse=True)
print(states)

states.reverse()
print(states)