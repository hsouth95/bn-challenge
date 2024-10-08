from pydantic import BaseModel

class Member(BaseModel):
  name: str
  bio: str
  locations: list[str] = []

class Job(BaseModel):
  title: str
  location: str