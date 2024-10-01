class SymptomChecker:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def check_symptoms(self, symptoms):
        prompt = f"The user reported the following symptoms: {symptoms}. What could be the cause and suggestions?  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM for symptom analysis
        diagnosis = self.llm.invoke(prompt).content
        return diagnosis
