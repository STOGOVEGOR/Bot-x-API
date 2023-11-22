from dataclasses import dataclass
from typing import ClassVar


@dataclass
class HTTPMethods:
    GET: ClassVar[str] = "GET"
    POST: ClassVar[str] = "POST"
