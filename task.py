"""Модель одной задачи."""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    description: str = ""
    status: bool = False
    author: str = "—"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    id: int | None = None

    def to_dict(self) -> dict:
        """Преобразовать задачу в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "author": self.author,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Создать задачу из словаря."""
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            status=bool(data.get("status", False)),
            author=data.get("author", "—"),
            created_at=data.get("created_at", datetime.now().isoformat(timespec="seconds")),
        )
