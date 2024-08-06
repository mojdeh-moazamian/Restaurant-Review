from pydantic import BaseModel, validator
from datetime import date

class RestaurantReview(BaseModel):
    data: date
    reviewer: str
    testo: str
    sentiment: bool
    voto: float

    @validator('voto')
    def voto_must_be_between_0_and_5(cls, v):
        if v < 0 or v > 5:
            raise ValueError('voto must be between 0 and 5')
        return v

    @validator('testo')
    def testo_length_must_be_valid(cls, v):
        if len(v) < 10 or len(v) > 500:
            raise ValueError('testo length must be between 10 and 500 characters')
        return v
