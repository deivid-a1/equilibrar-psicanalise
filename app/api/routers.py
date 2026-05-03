from datetime import datetime

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
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
async def home(request: Request):
    logger.info("Página principal acessada")
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=_base_context(),
    )


# Redirect rotas legadas das variantes antigas → /
@router.get("/acolhimento", include_in_schema=False)
@router.get("/profundidade", include_in_schema=False)
@router.get("/clinico", include_in_schema=False)
async def legacy_variants_redirect():
    return RedirectResponse(url="/", status_code=301)


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
