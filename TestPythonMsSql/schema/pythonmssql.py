from typing import Optional
from pydantic import BaseModel


class Pythonmssql(BaseModel):
    id: Optional[int]

    name: str
