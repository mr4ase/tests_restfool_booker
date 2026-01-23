# src\models\auth_model.py


from pydantic import BaseModel


class AuthModel(BaseModel):
    token: str
