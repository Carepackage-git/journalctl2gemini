from pydantic import BaseModel
from typing import Optional

class JournalBrief(BaseModel):
    major_errors: Optional[str] = None
    minor_errors: Optional[str] = None
    other_notes: Optional[str] = None
    status: Optional[str] = None