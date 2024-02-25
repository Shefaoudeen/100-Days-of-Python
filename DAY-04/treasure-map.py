line1 = ["❌", "❌", "❌"]
line2 = ["❌", "❌", "❌"]
line3 = ["❌", "❌", "❌"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot")
position = input().lower()

if position[0] == 'a':
    map[int(position[1])-1][0] = "🎁"
elif position[0] == 'b':
    map[int(position[1])-1][1] = "🎁"
else:
    map[int(position[1])-1][2] = "🎁"

print(f"{line1}\n{line2}\n{line3}")


'''
  #AKKA SOLUTION

letter = position[0].lower()
abc = ['a','b','c']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "🎁"

'''
