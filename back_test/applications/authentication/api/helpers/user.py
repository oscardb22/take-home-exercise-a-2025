from abc import ABC, abstractmethod
from dataclasses import dataclass

from applications.authentication.models import User


class AbstractUser(ABC):
    """docstring for UserDB"""

    @abstractmethod
    def set_new_password(self) -> None:
        """To set_new_password"""


@dataclass
class UserDB(AbstractUser):
    user: User
    password: str

    def set_new_password(self) -> None:
        """set_new_password"""
        self.user.set_password(self.password)
        self.user.save()
