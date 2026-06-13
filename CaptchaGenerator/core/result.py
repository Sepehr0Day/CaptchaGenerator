from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ChallengeResult:
    answer: Any
    path: str
    prompt: str
    metadata: dict[str, Any] = field(default_factory=dict)
    accessibility_text: str = ""
    mime_type: str = "image/png"
