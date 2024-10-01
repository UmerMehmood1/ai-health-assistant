from fastapi.staticfiles import StaticFiles
from DietPlan import DietPlan
from FitnessPlan import FitnessPlan
from HealthInsights import HealthInsights
from SymptomChecker import SymptomChecker
from UserProfile import UserProfile 
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from langchain_cohere import ChatCohere
import uvicorn
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

# FastAPI instance
app = FastAPI()

# Templates directory for rendering HTML files
templates = Jinja2Templates(directory="templates")

# Initialize LLM (like OpenAI or Langchain LLM)
llm = ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"))
app.mount("/static", StaticFiles(directory="static"), name="static")

# Instantiate UserProfile as a variable
user = UserProfile(
    name="Jane Doe",
    age=28,
    gender="Male",
    height=165.0,
    weight=60.0,
    health_goals="Muscle gain"
)

# Home Page
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

# Daily Suggestions Route
@app.get("/daily_suggestions")
async def daily_suggestions(request: Request):
    health_insights = HealthInsights(user, llm)
    suggestions = health_insights.generate_daily_suggestions()
    return templates.TemplateResponse("suggestions.html", {"request": request, "suggestions": suggestions})

# Diet Plan Route
@app.get("/diet_plan")
async def diet_plan(request: Request):
    diet = DietPlan(user, llm)
    plan = diet.generate_diet_plan()
    return templates.TemplateResponse("diet_plan.html", {"request": request, "plan": plan})

# Fitness Plan Route
@app.get("/fitness_plan")
async def fitness_plan(request: Request):
    fitness = FitnessPlan(user, llm)
    plan = fitness.generate_workout_plan()
    return templates.TemplateResponse("fitness_plan.html", {"request": request, "plan": plan})

# Symptom Checker Route
@app.post("/symptom_checker")
async def symptom_checker(request: Request, symptoms: str = Form(...)):
    checker = SymptomChecker(user, llm)
    diagnosis = checker.check_symptoms(symptoms)
    return templates.TemplateResponse("diagnosis.html", {"request": request, "diagnosis": diagnosis})

# Run the FastAPI server using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)