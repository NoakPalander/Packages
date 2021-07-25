from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Group:
    name: str
    packages: Optional[List[str]] = None
    script: Optional[str] = None
    command: Optional[str] = None
