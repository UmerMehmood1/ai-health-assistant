class Telemedicine:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def suggest_doctors(self):
        prompt = "Suggest doctors for the following health conditions.  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM for doctor suggestions
        doctor_suggestions = self.llm.invoke(prompt).content
        return doctor_suggestions
