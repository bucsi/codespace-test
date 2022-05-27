név = ["Leclerc", "Verstappen", "Sainz", "Perez", "Norris", "Magnussen", "Russel", "Hamilton",
       "Ocon", "Gasly", "Hulkenberg", "Alonso", "Zhou", "Bottas", "Albon", "Stroll", "Ricciardo", "Latifi"]
ido = []
kor = []
seb = []

for i in range(0, len(név), 1):
    ido.append(float(input()))
    kor.append(int(input()))
    seb.append(float(input()))
    print(név[i])

atlagkor = sum(kor)//len(kor)
print(atlagkor)
