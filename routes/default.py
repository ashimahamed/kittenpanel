from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
router = APIRouter()
templates = Jinja2Templates(directory="templates/legal")

@router.get('/tos', response_class=HTMLResponse)
async def get_tos():
    """
    Show the terms of service
    """
    return templates.TemplateResponse('tos.html', {}, status_code=200)

@router.get('/pp', response_class=HTMLResponse)
async def get_pp():
    """
    Show the privacy policy
    """
    return templates.TemplateResponse('pp.html', {}, status_code=200)