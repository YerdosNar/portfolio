from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"cwd": "~"})


@app.get("/AboutMe")
def aboutme(request: Request):
    return templates.TemplateResponse(request, "aboutme.html", {"cwd": "~/AboutMe"})


@app.get("/Projects")
def projects(request: Request):
    return templates.TemplateResponse(request, "projects.html", {"cwd": "~/Projects"})


@app.get("/ContactMe")
def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"cwd": "~/Contact"})
