import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
a = canvas.create_rectangle(0,0,50,50,fill='blue')
b = canvas.create_rectangle(50,0,100,50,fill='green')
c = canvas.create_rectangle(0,50,50,100,fill='green')
d = canvas.create_rectangle(0,100,50,150,fill='blue')

graph = {a: [b, c], b:[],d:[d], c:[d]}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
print(find_path(graph,a,d))
path = find_path(graph, a, d)
import time
for i in path:
    time.sleep(1)
    canvas.itemconfig(i, fill='red')


root.mainloop()