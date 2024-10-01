class DietPlan:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def generate_diet_plan(self):
        health_goals = self.user_profile.health_goals
        prompt = f"Create a diet plan for someone with a goal of {health_goals}.  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM for AI-generated diet plans
        diet_plan = self.llm.invoke(prompt).content
        return diet_plan
