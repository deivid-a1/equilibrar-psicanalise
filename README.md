# Equilibrar Psicanálise — Site

Site institucional da clínica **Equilibrar Psicanálise** (Letícia Gomes de Carvalho — psicanalista clínica, Registro SBPT 00352025).

## Stack

- **FastAPI** + **Uvicorn** (Python 3.12)
- **Jinja2** templates
- **TailwindCSS** via CDN + CSS custom
- **AOS** para animações de scroll
- Fontes **Now** + **Lora**
- E-mail SMTP (Gmail) para o formulário de contato

## Rotas

| URL | Descrição |
|---|---|
| `/` | Site principal |
| `/acolhimento`, `/profundidade`, `/clinico` | Redirecionam 301 para `/` (variantes antigas usadas durante a fase de escolha) |
| `POST /contato` | Endpoint do formulário (envia e-mail via SMTP) |

## Como rodar localmente

```bash
# 1. Ativar virtualenv
source env/bin/activate

# 2. Instalar dependências (se primeira vez)
pip install -r requirements.txt

# 3. Configurar .env (não commitar)
cat > .env <<EOF
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-app-password
SERVER_PORT=8000
EOF

# 4. Rodar
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Acessar `http://127.0.0.1:8000/`.

## Estrutura

```
app/
  main.py              # FastAPI + StaticFiles
  api/routers.py       # Rotas
  core/
    config.py          # Pydantic settings
    site_content.py    # ★ Conteúdo textual centralizado
    logger.py
  services/email_service.py
templates/
  base.html            # Layout + lightbox + scripts compartilhados
  _macros.html         # Macros Jinja (CTA, preço, passos, seção img+texto)
  _form_contato.html   # Formulário compartilhado
  index.html           # Single-page principal
static/
  css/style.css        # Variáveis, tema, price-block, scroll-padding
  fonts/               # Now + Lora
  img/                 # Imagens WebP otimizadas
```

## Diretrizes da cliente

- Imagem e texto em paralelo, sempre que possível
- Bloco de preço com valor cheio riscado, valor à vista em destaque e selo de economia
- Botões claros que escurecem no hover
- Degradê vertical da página (claro → escuro)
- Imagens dos programas clicáveis para ampliar (lightbox)
- CTA secundário "Agende uma sessão gratuita" no hero
- Mobile-friendly

Para mais detalhes técnicos e arquiteturais, ver [AGENTS.md](AGENTS.md).
