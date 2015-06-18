#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# get quantity of students, tasks and number of group
tasks = int(input())
students = int(input())
number = int(input())
length = 180 + 75 * tasks
height = 20 * (students + 1)

# make table
img = Image.new('RGB', (length + 40, height + 40), (255, 255, 255))
imgDrawer = ImageDraw.Draw(img)
imgDrawer.rectangle((20, 20, length + 20, height + 20), fill = "#FFFFFF", outline = "#000000")
imgDrawer.rectangle((0, 0, 20, 20), fill = "#000000", outline = "#000000")
imgDrawer.rectangle((length + 20, 0, length + 40, 20), fill = "#000000", outline = "#000000")
imgDrawer.rectangle((0, height + 20, 20, height + 40), fill = "#000000", outline = "#000000")
imgDrawer.rectangle((length + 20, height + 20, length + 40, height + 40), fill = "#000000", outline = "#000000")
for i in range(200, length + 20, 75):
	imgDrawer.line((i, 20, i, length + 20), fill = "#000000", width = 1)
for i in range(40, height + 20, 20):
	imgDrawer.line((20, i, length + 20, i), fill = "#000000", width = 1)
for i in range(tasks):
	imgDrawer.text((200 + 75 * i + 37, 25), str(i + 1), fill = "black")

# draw lines for number of group
for i in range(number):
	imgDrawer.line((20 + 180 // (number + 1) * (i + 1), 20, 20 + 180 // (number + 1) * (i + 1), 40), fill = "#000000", width = 1)

# write names
surnames = []
with open('groups.txt', 'r') as f_read:
	for line in f_read:
		surnames.append(line.decode(encoding = "utf8")[:-1])
for i in range(students):
	imgDrawer.text((30, 20 * (i + 2) + 5), surnames[(students + 1) * (number - 1) + i + 1], font = ImageFont.truetype("DejaVuSans.ttf", 12), fill = (0,0,0))

# save image
img.save("pil-example.png")
