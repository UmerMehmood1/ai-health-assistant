from pydantic import BaseModel
class UserProfile(BaseModel):
    name: str
    age: int
    gender: str
    height: float
    weight: float
    health_goals: str
    def get_profile_summary(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "health_goals": self.health_goals,
        } 