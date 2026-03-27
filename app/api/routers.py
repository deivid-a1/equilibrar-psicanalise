from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.services.email_service import send_contact_email
from loguru import logger

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Página principal acessada")
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@router.post("/contato")
async def submit_contact(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    mensagem: str = Form(...)
):
    logger.info(f"Submissão de formulário recebida de {nome}")
    success = await send_contact_email(nome, email, telefone, mensagem)
    if success:
        return JSONResponse(content={"message": "Mensagem enviada com sucesso!"}, status_code=200)
    return JSONResponse(content={"message": "Erro ao enviar a mensagem. Tente novamente."}, status_code=500)