from datetime import date


class Person:
    def __init__(self, name, surname, sex, bday):
        self.name = name
        self.surname = surname
        self.sex = sex

        if isinstance(bday, date):
            self.bday: date = bday
        else:
            raise ValueError("bday must be date type")

    def __eq__(self, other: "Person") -> bool:
        if type(other) != Person:
            return False
        if self.name != other.name:
            return False
        elif self.surname != other.surname:
            return False
        elif self.sex != other.sex:
            return False
        elif self.bday != other.bday:
            return False

        return True

    def __str__(self):
        return f"{self.name} {self.surname}, {self.sex}, {self.full_ages()} years"

    def full_ages(self) -> str:
        return date.today().year - self.bday.year

    def __repr__(self):
        return (
            f"Person('{self.name}', '{self.surname}', '{self.sex}', {repr(self.bday)})"
        )


class Student(Person):
    def __init__(self, name, surname, sex, bday, group, skill):
        super().__init__(name, surname, sex, bday)
        self.group = group
        self.skill = skill

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.group} group, {self.skill} skill"

    def __eq__(self, other: "Person") -> bool:
        if type(other) != Student:
            return False
        if self.name != other.name:
            return False
        elif self.surname != other.surname:
            return False
        elif self.sex != other.sex:
            return False
        elif self.bday != other.bday:
            return False
        elif self.group != other.group:
            return False
        elif self.skill != other.skill:
            return False

        return True

    def __repr__(self):
        return f"Student('{self.name}', '{self.surname}', '{self.sex}', {repr(self.bday)}, {self.group}, {self.skill})"


class Group:
    def __init__(self, students) -> None:
        self.students = list(students)

    def __repr__(self) -> str:
        student_list = [f"Student({s})" for s in self.students]
        return f"Group({student_list})"

    def __eq__(self, __value: object) -> bool:
        if type(self) == type(__value):
            return True
        return False

    def sort_by_age(self, reverse=False):
        self.students = list(self.students)
        flag = True

        while flag == True:
            flag = False
            for i in range(len(self.students) - 1):
                b = self.students[i]

                if (
                    date.today().year - self.students[i + 1].bday.year
                    < date.today().year - self.students[i].bday.year
                ):
                    self.students[i] = self.students[i + 1]
                    self.students[i + 1] = b
                    flag = True

        if reverse == True:
            self.students.reverse()

    def sort_by_skill(self, reverse=False):
        self.students = list(self.students)
        flag = True

        while flag == True:
            flag = False
            for i in range(len(self.students) - 1):
                b = self.students[i]
                if self.students[i + 1].skill < self.students[i].skill:
                    self.students[i] = self.students[i + 1]
                    self.students[i + 1] = b
                    flag = True

        if reverse == True:
            self.students.reverse()

    def sort_by_age_and_skill(self, reverse=False):
        self.students = list(self.students)
        flag = True

        while flag == True:
            flag = False
            for i in range(len(self.students) - 1):
                b = self.students[i]

                if (
                    date.today().year - self.students[i + 1].bday.year
                    < date.today().year - self.students[i].bday.year
                ):
                    self.students[i] = self.students[i + 1]
                    self.students[i + 1] = b
                    flag = True
                elif (
                    date.today().year - self.students[i + 1].bday.year
                    == date.today().year - self.students[i].bday.year
                ):
                    a = self.students[i]
                    if self.students[i + 1].skill < self.students[i].skill:
                        self.students[i] = self.students[i + 1]
                        self.students[i + 1] = a
                        flag = True

        if reverse == True:
            self.students.reverse()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
