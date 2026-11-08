""" =========================================================
    Task — шаблон задачи.
    =========================================================
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """Модель одной задачи."""
    title: str
    description: str = ""
    status: bool = False
    author: str = "—"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    id: int | None = None

    def to_dict(self) -> dict:
        """Сериализовать задачу в dict для StorageManager."""
        pass

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Восстановить Task из dict."""
        pass
