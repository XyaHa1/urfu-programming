from abc import ABC, abstractmethod
from typing import List


class Profession(ABC):
    def __init__(self, name, salary, level, education=None, experience=0):
        self._name: str = name
        self._salary: int = salary
        self._level: str = level
        self._educations: List[str] = education
        self._experience: int = experience

    def __str__(self):
        return f"Имя: {self._name}\nЗарплата: {self._salary}\nУровень: {self._level}\nОбразование: {self._educations}\nОпыт: {self._experience}"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            raise ValueError("Зарплата должна быть положительным числом")

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, years):
        if years >= 0:
            self._experience += years
        else:
            raise ValueError("Возраст должен быть положительным числом")

    @property
    def educations(self):
        return self._educations

    @educations.setter
    def educations(self, education):
        if education:
            self._educations.append(education)
        else:
            raise ValueError("Образование не может быть пустым")

    @abstractmethod
    def work(self):
        pass


class Programmer(Profession):
    def __init__(
            self,
            name,
            salary,
            level,
            hard_skills,
            programming_language,
            soft_skills,
            education=None,
            experience=0,
    ):
        super().__init__(name, salary, level, education, experience)
        self._hard_skills: List[str] = hard_skills
        self._programming_language: str = programming_language
        self._soft_skills: List[str] = soft_skills

    @property
    def hard_skills(self):
        return self._hard_skills

    @hard_skills.setter
    def hard_skills(self, skills):
        if isinstance(skills, list):
            self._hard_skills.extend(skills)
        elif isinstance(skills, str):
            self._hard_skills.append(skills)
        else:
            raise ValueError("Неверный тип данных")

    @property
    def soft_skills(self):
        return self._soft_skills

    def work(self):
        return "Пишет код..."

    def make_commit(self):
        return f"{self._name} сделал коммит"

    def make_pull_request(self):
        return f"{self._name} сделал pull request"


class Doctor(Profession):
    def __init__(
            self,
            name,
            salary,
            level,
            specialization,
            name_of_patients=None,
            education=None,
            experience=0,
    ):
        super().__init__(name, salary, level, education, experience)
        self._specialization: str = specialization
        self._name_of_patients = name_of_patients
        self._cnt_vaccinated = 0

    @property
    def name_of_patients(self):
        return self._name_of_patients

    @name_of_patients.setter
    def name_of_patients(self, name):
        if isinstance(name, str):
            if self._name_of_patients:
                self._name_of_patients.append(name)
            else:
                self._name_of_patients = [name]
        else:
            ValueError("Неверный тип данных")

    @property
    def specialization(self):
        return self._specialization

    @property
    def cnt_vaccinated(self):
        return self._cnt_vaccinated

    def work(self):
        return f"{self._name} лечит пациента..."

    def make_vaccinations(self, count=1):
        if count <= 0:
            print("Нельзя сделать 0 или меньше количества прививок")
            return

        for i in range(count):
            print(f"{self._name} делает прививку человеку №{i + 1}")
            self._cnt_vaccinated += 1

    def get_diagnose(self):
        return f"{self._name} ставит диагноз"


def work_acceptance(profession):
    print(profession.work())


if __name__ == "__main__":
    programmer = Programmer(
        "Пэпэ",
        100000,
        "Junior",
        ["Python", "Git"],
        "Python",
        ["Любит смотреть My Little Pony"],
        education=["Бакалавриат"],
    )

    doctor = Doctor(
        "Шнэпэ",
        300000,
        "Middle",
        "Терапевт",
        education=["Бакалавриат, Магистратура, Докторантура"],
        experience=5,
    )

    workers = [programmer, doctor]
    for worker in workers:
        work_acceptance(worker)

    print()
    doctor.make_vaccinations(5)
