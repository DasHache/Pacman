# To do

### 2016.07.05

##### 1.

Regarde le fichier layout.py, ligne #11

```python
self.walls = [[0,0],[0,1],[0,3],[1,0],[2,0],[3,3]]
```
Tu dois remplacer cette liste par les donnees que t'as lu depuis le fichier "small.lay"
(voir la ligne #7 du meme fichier layout.py)
```
lines = f.readlines()
```

Explications:
1. Tu as:
```python
self.walls     # <--- c'est une liste des listes
f.readlines()  # <--- retourne une liste des chaines des characteres
```
2. Tu dois lire ligne par ligne depuis ton fichier:
```python
for y in len(lines):  # <--- pour obtenir une ligne tu peux utiliser une boucle "for"
    ligne = l[y]   # <--- la variable "ligne" va etre une chaine des characteres
```

3. Tu dois lire charactere par charactere depuis ta ligne:
```python
for x in len(ligne):  # <--- pour obtenir une charactere tu peux utiliser une boucle "for"
    charactere = ligne[x] # <--- la variable "charactere" va etre une characteres "%" ou "." ou "P"
```
4. Donc, tu dois avoir qq chose comme ca:
```python
for y in len(lines):
    ligne = len[y]
    for x in len(ligne):
        charactere = ligne[x]
        print(character)
```

Maintenant, tu dois remplacer le print par quelque chose plus utile.
Par example, si tu te souviens, une liste a une methode qui s'appele "append".
Cette methode rajoute un element dans ta liste. Comme ca:
```python
self.walls.append([x,y])
```

2. Lancer "game.py" pour verifier si tu marche comme il faut