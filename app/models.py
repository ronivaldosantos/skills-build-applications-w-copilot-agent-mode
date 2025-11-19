"""OctoFit Tracker App - Data Models"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Workout:
    """Workout data model"""
    id: Optional[int] = None
    exercise: str = ""
    duration: int = 0  # in minutes
    calories: int = 0
    date: Optional[datetime] = None
    notes: str = ""
