class FitnessPlan:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def generate_workout_plan(self):
        health_goals = self.user_profile.health_goals
        prompt = f"Create a workout plan for someone with a goal of {health_goals}.  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM to generate workout plans
        workout_plan = self.llm.invoke(prompt).content
        return workout_plan
