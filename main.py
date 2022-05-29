class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, new_name):
        self.name = new_name
        return print("The student's new name is ",self.name)

    def change_age(self, new_age):
        self.age = new_age
        return print("The student's new age is ",self.age)
    
    def add_track(self, new_track):
        self.tracks = self.tracks.append(new_track)
        return print("The student's track are ",self.tracks)

    def get_score(self):
        return print("The student's score is",self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
