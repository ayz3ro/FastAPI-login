from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from backend.app.api.routes import auth

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )

app.include_router(auth.router, prefix="/auth", tags=["Auth"])


@app.get("/", response_class=HTMLResponse)
async def serve_login_page():
    with open("frontend/index.html", "r") as file:
        return file.read()

@app.get("/dashboard", response_class=HTMLResponse)
async def serve_dashboard_page():
    with open("frontend/pages/dashboard/dashboard.html", "r") as file:
        return file.read()