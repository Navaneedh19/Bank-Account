line_1 = ["*", "*", "*"]
line_2 = ["*", "*", "*"]
line_3 = ["*", "*", "*"]

map = [line_1, line_2, line_3]
print("Hiding your treasure! X marks the spot.")
position = input()
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[number_index][letter_index] = "X"
print(f"{line_1}\n{line_2}\n{line_3}")
