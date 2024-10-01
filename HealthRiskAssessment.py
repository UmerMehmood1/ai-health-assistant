class HealthRiskAssessment:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def assess_risks(self):
        prompt = "Based on the following health data, assess risks for cardiovascular disease, diabetes, and hypertension.  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM for AI-driven risk assessments
        risk_assessment = self.llm.invoke(prompt).content
        return risk_assessment
