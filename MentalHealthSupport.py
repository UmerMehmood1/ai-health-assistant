class MentalHealthSupport:
    def __init__(self, user_profile, llm):
        self.user_profile = user_profile
        self.llm = llm

    def generate_mindfulness_exercises(self):
        prompt = "Generate mindfulness exercises for someone who is feeling stressed.  The response text should be in HTML so it'll represent as needed."
        
        # Use the passed LLM to generate exercises
        mindfulness_exercises = self.llm.invoke(prompt).content
        return mindfulness_exercises
