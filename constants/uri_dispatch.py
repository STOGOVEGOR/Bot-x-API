from dataclasses import dataclass
from typing import ClassVar


@dataclass
class URIDispatch:
    REGISTER: ClassVar[str] = "users"
    LOGIN: ClassVar[str] = "users/login"
