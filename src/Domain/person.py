class Person:
    def __init__(self,id: int = 999, name: str = "John", last:str = "Doe", email: str = "noreply@mail.com", phone:str = "8180000000"):
        self._name: str = name
        self._last: str = last
        self._email: str = email
        self._phone: str = phone
        self._id:int = id

    @property
    def name(self) -> str:
        return self._name

    @property
    def last(self) -> str:
        return self._last

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @last.setter
    def last(self, value: str) -> None:
        self._last = value

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @phone.setter
    def phone(self, value: str) -> None:
        self._phone = value

    def __str__(self):
        return f"Person=[id:{self._id}, name:{self._name} {self._last}, email:{self._email}, phone:{self._phone}]"

