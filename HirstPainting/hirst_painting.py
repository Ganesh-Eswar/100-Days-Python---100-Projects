import colorgram

color = colorgram.extract('dot_paint.jpg',100)

color_list = []

for cl in color:
    r, g, b = cl.rgb.r, cl.rgb.g, cl.rgb.b
    if not (r > 240 and g > 240 and b > 240):
        color_list.append((r, g, b))

print(color_list)
