from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: int
    content: str
    created_at: datetime
