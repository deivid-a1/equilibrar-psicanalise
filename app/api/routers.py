from datetime import datetime

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from loguru import logger

from app.core.site_content import get_content
from app.services.email_service import send_contact_email

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def _base_context() -> dict:
    ctx = get_content()
    ctx["current_year"] = datetime.now().year
    ctx["doctoralia_url"] = ctx["redes"]["doctoralia"]
    return ctx


@router.get("/", response_class=HTMLResponse)
async def escolha(request: Request):
    logger.info("Página-índice (escolha de variante) acessada")
    return templates.TemplateResponse(
        request=request,
        name="escolha.html",
        context={"current_year": datetime.now().year},
    )


@router.get("/acolhimento", response_class=HTMLResponse)
async def variante_acolhimento(request: Request):
    logger.info("Variante 'acolhimento' acessada")
    return templates.TemplateResponse(
        request=request,
        name="v1_acolhimento.html",
        context=_base_context(),
    )


@router.get("/profundidade", response_class=HTMLResponse)
async def variante_profundidade(request: Request):
    logger.info("Variante 'profundidade' acessada")
    return templates.TemplateResponse(
        request=request,
        name="v2_profundidade.html",
        context=_base_context(),
    )


@router.get("/clinico", response_class=HTMLResponse)
async def variante_clinico(request: Request):
    logger.info("Variante 'clinico' acessada")
    return templates.TemplateResponse(
        request=request,
        name="v3_clinico.html",
        context=_base_context(),
    )


@router.post("/contato")
async def submit_contact(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    mensagem: str = Form(...),
):
    logger.info(f"Submissão de formulário recebida de {nome}")
    success = await send_contact_email(nome, email, telefone, mensagem)
    if success:
        return JSONResponse(content={"message": "Mensagem enviada com sucesso!"}, status_code=200)
    return JSONResponse(content={"message": "Erro ao enviar a mensagem. Tente novamente."}, status_code=500)
