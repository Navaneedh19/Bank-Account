def reformats_text(text, width):
    words = text.split()
    formatted_text = ""
    line = ""

    for word in words:
        if len(line) + len(word)+1 > width:
            num_spaces = width - len(line)
            line = line.ljust(width - num_spaces)
            formatted_text += line +'\n'
            line = ''

        line += word + " "

    if line:
        num_spaces = width - len(line) 
        line = line.ljust(width - num_spaces)
        formatted_text += line

    return formatted_text

text_body = "Apples grown from seed tend to be very different from those of their parents, and the resultant fruit frequently lacks desired characteristics. For commercial purposes, including botanical evaluation, apple cultivars are propagated by clonal grafting onto rootstocks. Apple trees grown without rootstocks tend to be larger and much slower to fruit after planting. Rootstocks are used to control the speed of growth and the size of the resulting tree, allowing for easier harvesting."
line_width = 30

formatted_text = reformats_text(text=text_body, width=line_width)
print(formatted_text)

