from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from adapters.codeforces import analyze_user
from roadmap.generator import generate_roadmap
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ribock API", description="Competitive Programming Roadmap Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    handle: str
    goal: str  # high_school | job_interview | zco_inoi_ioi | acm_icpc

@app.get("/")
def home():
    return {"message": "Welcome to Ribock API"}

@app.post("/generate-roadmap")
def generate(data: AnalyzeRequest):
    try:
        user_data = analyze_user(data.handle)
        roadmap = generate_roadmap(user_data, data.goal)
        return JSONResponse(content={
            "handle": data.handle,
            "goal": data.goal,
            "userProfile": user_data,
            "roadmap": roadmap
        })
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
