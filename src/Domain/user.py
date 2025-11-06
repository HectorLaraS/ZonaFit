class User:
    def __init__(self, id: int = 0, username: str = "test", password: str = "test"):
        self._id = id
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @id.setter
    def id(self, value):
        self._id = value

    @username.setter
    def username(self, value):
        self._username = value

    @password
    def password(self, value):
        self._password = value

    def __str__(self):
        return f"USER=[id:{self._id}, username:{self._username}]"