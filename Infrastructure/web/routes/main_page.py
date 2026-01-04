from fastapi import APIRouter, HTTPException
from pathlib import Path
from fastapi.responses import FileResponse, HTMLResponse

router = APIRouter()
@router.get("/")
async def main_page():
    html_file = Path("Infrastructure/web/pages/index.html")
    if not html_file.exists():
        return HTMLResponse(content="<h1>HTML файл не найден</h1>", status_code=404)
    return FileResponse(html_file)