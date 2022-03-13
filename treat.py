import json
with open('colors from base16.json', 'r') as f:
    colors1 = json.load(f)
with open('color from gogh.json', 'r') as f:
    colors2 = json.load(f)['themes']
color = open('themes.json','w')
colors = []
for i in colors1:
    color1 = {}
    color1['name'] = i['name']

    color1['background'] = i["colors"]["terminal.background"]
    color1['foreground'] = i["colors"]["terminal.foreground"]
    color1['cursorColor'] = i["colors"]["terminalCursor.foreground"]
    color1['black'] = i["colors"]["terminal.ansiBlack"]
    color1['blue'] = i["colors"]["terminal.ansiBlue"]
    color1['brightBlack'] = i["colors"]["terminal.ansiBrightBlack"]
    color1['brightBlue'] = i["colors"]["terminal.ansiBrightBlue"]
    color1['brightCyan'] = i["colors"]["terminal.ansiBrightCyan"]
    color1['brightGreen'] = i["colors"]["terminal.ansiBrightGreen"]
    color1['brightPurple'] = i["colors"]["terminal.ansiBrightMagenta"]
    color1['brightRed'] = i["colors"]["terminal.ansiBrightRed"]
    color1['brightWhite'] = i["colors"]["terminal.ansiBrightWhite"]
    color1['brightYellow'] = i["colors"]["terminal.ansiBrightYellow"]
    color1['cyan'] = i["colors"]["terminal.ansiCyan"]
    color1['green'] = i["colors"]["terminal.ansiGreen"]
    color1['purple'] = i["colors"]["terminal.ansiMagenta"]
    color1['red'] = i["colors"]["terminal.ansiRed"]
    color1['white'] = i["colors"]["terminal.ansiWhite"]
    color1['yellow'] = i["colors"]["terminal.ansiYellow"]
    colors.append(color1.copy())
for i in colors2:
    colors.append(i.copy())

def rename_duplicate(list, print_result=False):
    index = []
    new_list = []
    for i in list:
        if i["name"] in index:
            i["name"] += '2'
        else:
            index.append(i["name"])
        new_list.append(i)
    if print_result:
        print("Renamed list:",new_list)
    return new_list

colors = rename_duplicate(colors)
colors.sort(key = lambda x: x["name"])
json.dump(colors,color)