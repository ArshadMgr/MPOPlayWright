from playwright.sync_api import Page


class NewHire:
    def __init__(self, page: Page):
        self.page = page
        self.id = 0
        self.username = ""
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.password = ""
        self.phone = ""
        self.role = ""
        self.token = ""
        self.userStatus = 0

    def setId(self, id: int):
        self.id = id

    def getId(self) -> int:
        return self.id

    def setFirstName(self, firstName: str):
        self.firstName = firstName

    def getFirstName(self) -> str:
        return self.firstName

    def setLastName(self, lastName: str):
        self.lastName = lastName

    def getLastName(self) -> str:
        return self.lastName

    def setRole(self, role: str):
        self.role = role

    def getRole(self) -> str:
        return self.role

    def setEmail(self, email: str):
        self.email = email

    def getEmail(self) -> str:
        return self.email

    def setPassword(self, password: str):
        self.password = password

    def getPassword(self) -> str:
        return self.password

    def setPhone(self, phone: str):
        self.phone = phone

    def getPhone(self) -> str:
        return self.phone

    def setUserStatus(self, userStatus: int):
        self.userStatus = userStatus

    def getUserStatus(self) -> int:
        return self.userStatus

    def setToken(self, token: str):
        self.token = token

    def getToken(self) -> str:
        return self.token
