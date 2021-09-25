class football3:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
 
players = []
 
for i in [["неймар", 51], ["роналдо", 1], ["месси", 71], ["игнатенко", 45], ["суарес", 35], ["гризман", 20], ["бейл", 34], ["тымчик", 24], ["боль", 3], ["шабанов", 13], ["миколенко", 16]]:
    players.append(football3(i[0], i[1]))