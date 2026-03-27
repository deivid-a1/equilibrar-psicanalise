import aiosmtplib
from email.message import EmailMessage
from app.core.config import settings
from loguru import logger

async def send_contact_email(name: str, email: str, phone: str, message: str) -> bool:
    logger.debug(f"Processo de envio de email iniciado para {name}")
    msg = EmailMessage()
    msg["From"] = settings.smtp_user
    msg["To"] = settings.contact_email
    msg["Subject"] = f"Novo Contato Site: {name}"
    msg.set_content(
        f"Nome: {name}\n"
        f"E-mail: {email}\n"
        f"Telefone: {phone}\n\n"
        f"Mensagem:\n{message}"
    )

    try:
        await aiosmtplib.send(
            msg,
            hostname=settings.smtp_server,
            port=settings.smtp_port,
            use_tls=True,
            username=settings.smtp_user,
            password=settings.smtp_password,
            timeout=10.0
        )
        logger.info(f"Email enviado com sucesso para {name}")
        return True
    except Exception as e:
        logger.error(f"Falha ao enviar email para {name}: {str(e)}")
        return False