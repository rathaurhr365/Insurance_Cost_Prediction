from pydantic import BaseModel,Field
from typing import Literal

class InsuranceInput(BaseModel):
    age: int = Field(ge=18, le=100)
    sex: Literal["male", "female"]
    bmi: float = Field(gt=0)
    children: int = Field(ge=0, le=20)
    region: Literal["southwest", "southeast", "northwest", "northeast"]
    smoker: Literal["yes", "no"]