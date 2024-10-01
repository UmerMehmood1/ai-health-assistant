class HealthReports:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def generate_health_report(self):
        # Use collected data and analyze progress
        prompt = f"Generate a weekly health report for {self.user_profile.name}, tracking diet, workout, and health progress.  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM to generate report
        health_report = self.llm.invoke(prompt).content
        return health_report
