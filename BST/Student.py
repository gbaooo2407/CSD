class Student:
    def __init__(self,id:str,name:str,grade:float):
        """
        Initialize a new student:
        :param id: str , MSSV
        :param name: str, ten sinh vien
        :param grade: float, Diem sinh vien
        """
        self.id = id
        self.name = name
        self.grade = grade

    def __str__(self) -> str:
        return f'Student info: id {self.id} - name:{self.name} - grade:{self.grade}'


