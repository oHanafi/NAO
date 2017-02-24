class Student(object):


    def __init__(self, name, surName, birthYear, *args, **kwargs):
        self.name = name
        self.surName = surName
        self.birthYear = birthYear

    def __init__(self, id, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.id = id


    grades = {1, 2, 3}#om compile errors te voorkomen
    mood = "happy"
    preferredLightLevel = 50

    def getGrades():
        return grades

    def getMood():
        return