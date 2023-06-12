from random import choice

class Human:
    GENOM_COUNT = 46
    
    def __init__(self, name: str, status: str = "") -> None:
        self.name = name
        self.status = status
        
    def description(self):
        return f'{self.status} {self.name}'
    
    def say(self, msg: str):
        print(f'{self.status} {self.name}: {msg}')
    
    @classmethod
    def change_genom_count(cls):
        cls.GENOM_COUNT += 1
        
    @staticmethod
    def create_new_name() -> str:
        return choice(("Ilias", "Ruslan","Vika"))
    
# me = Human(name="Ilias", status="Prof.")

# me.say("Всем привет")

def test_classmethod():
    print(f"Genom count before all {Human.GENOM_COUNT}")
    Human.change_genom_count() # OK

    print(f"Genom count after first change: {Human.GENOM_COUNT}")

    me.change_genom_count()    # OK

    print(f"Genom count after all {Human.GENOM_COUNT}")



class Student:
    count = 0
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        Student.count += 1
    
    def get_name(self) -> str:
        return self._name
    
    def get_age(self) -> int:
        return self._age
    
    def set_age(self, age: int) -> int:
        if age > self._age:
            self._age = age
        else:
            raise ValueError("Age can not be decreased")
    
    def bio(self):
        print(f"{self._name}, {self._age}")
        
def test_students():
    ruslan = Student("Ruslan", 18)
    ruslan.bio()
    ruslan.set_age(20)
    ruslan.bio()
test_students()