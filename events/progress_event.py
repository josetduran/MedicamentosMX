from dataclasses import dataclass


@dataclass
class ProgressEvent:
    actual: int
    total: int
    medicamento: str