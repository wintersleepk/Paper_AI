from dataclasses import dataclass, field
from typing import Any


@dataclass
class Paper:

    filename: str = ""

    title: str = ""

    authors: list = field(default_factory=list)

    pages: int = 0

    reading_time: int = 0

    full_text: str = ""

    metadata: dict = field(default_factory=dict)

    sections: list = field(default_factory=list)

    chunks: list = field(default_factory=list)

    summary: str = ""

    study_notes: str = ""

    insights: str = ""

    quiz: list = field(default_factory=list)

    vector_store: Any = None

    chat_history: list = field(default_factory=list)

    pdf_hash: str = ""

    vector_ready: bool = False