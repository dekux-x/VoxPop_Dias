from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.repository import CommentsRepository

app = FastAPI()
templates = Jinja2Templates(directory="templates")
repository = CommentsRepository()
@app.get("/")
def main_page(
        request: Request,
        page: int = 1,
        limit: int = 6
):
    comments = repository.get_all()
    if len(comments) >= limit:
        comments[(page-1)*limit:]
    comments.reverse()
    return templates.TemplateResponse("VoxPop.html",{
        "request": request,
        "comments": comments
    })
@app.post("/")
def post_comment(
        request = Request,
        category: str = Form(...),
        comment: str = Form(...),
):
    repository.save({
        "content": comment,
        "category": category
    })
    return RedirectResponse("/", status_code = 303)
