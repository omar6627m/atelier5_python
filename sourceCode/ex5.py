class Etudiant:
    """defintion du class"""
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


# la liste d'etudiant
studentsList = [ Etudiant("Aharrar", "Omar", 20, "P13090878", 12),
             Etudiant("Hajji", "Jubair", 21, "P130908", 13),
             Etudiant(" Hajuji", "Ismail", 22, "P13090878", 5.5),
             Etudiant("Al-Wazzani", "Sufyan", 21, "P13090878", 7),
             Etudiant("Toufiq", "Mourad", 23, "P13090878", 10.5)]

# triage selon l'age 
def sortByAge(student):
    return student.age

studentsList.sort(key=sortByAge)

for student in studentsList:
    print("==========")
    print(student.nom)
    print(student.prenom)
    print(student.age)
print("=======end of list=============")

# triage selon la moyenne
def sortByAverage(student):
    return student.moyenne

studentsList.sort(key=sortByAverage)

for student in studentsList:
    print("==========")
    print(student.nom)
    print(student.prenom)
    print(student.moyenne)

print("=======end of list=============")