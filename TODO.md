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
l = f.readlines()
```

1. self.walls - c'est une liste des listes
2. f.readlines() - retourne une liste des chaines des characteres
3. Tu dois utiliser une boucle "for ligne in l:"
* si tu fait ca, la variable "ligne" - est une chaine des characteres
* tu peux utiliser une boucle "for character in ligne:"
* si tu fait ca, la variable "charactere" - est une characteres "%" ou "." ou "P"
* donc, tu dois avoir qq chose comme ca:
```python
for ligne in l:
   for charactere in ligne:
      print(character)
```

2. Lancer "game.py" pour verifier si tu marche comme il faut