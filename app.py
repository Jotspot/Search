from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

def search_index(query: str, limit: int = 100):
    conn = sqlite3.connect("papers.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Title, URL
        FROM papers
        WHERE Title LIKE ? OR URL LIKE ?
        LIMIT ?
    """, (f"%{query}%", f"%{query}%", limit))

    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/", response_class=HTMLResponse)
async def search(request: Request, q: str = ""):
    results = search_index(q) if q else []
    return templates.TemplateResponse("search.html", {
        "request": request,
        "query": q,
        "results": results
    })