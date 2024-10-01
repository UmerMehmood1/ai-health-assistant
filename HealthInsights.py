class HealthInsights:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def generate_daily_suggestions(self):
        # Use Langchain for natural language generation of insights
        health_data = self.user_profile.get_profile_summary()
        prompt = f"Generate personalized daily health advice for a {health_data['age']} year old {health_data['gender']}. The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM to generate advice
        suggestion = self.llm.invoke(prompt).content
        return suggestion
