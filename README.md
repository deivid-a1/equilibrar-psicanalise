# Equilibrar Psicanálise — Site

Site institucional da clínica **Equilibrar Psicanálise** (Letícia Gomes de Carvalho — psicanalista clínica, Registro SBPT 00352025).

> **Estado atual:** o site publica **3 variantes visuais** em URLs separadas para a cliente escolher uma. Após a decisão, as outras duas serão removidas.

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
| `/` | Página-índice com 3 cards de prévia (visualizar e escolher variante) |
| `/acolhimento` | Variante 1 — calor terapêutico, Lora itálico, foto retangular |
| `/profundidade` | Variante 2 — cinemático, Now em escala dramática, degradê até roxo escuro |
| `/clinico` | Variante 3 — estruturado/profissional, grade rígida, tons frios |
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
  base.html            # Layout base + lightbox + scripts compartilhados
  _macros.html         # Macros Jinja (CTA, preço, passos, seção img+texto)
  _form_contato.html   # Formulário compartilhado
  escolha.html         # Página-índice com 3 cards de prévia
  v1_acolhimento.html
  v2_profundidade.html
  v3_clinico.html
static/
  css/style.css        # Variáveis, temas (.theme-*), price-block
  fonts/               # Now + Lora
  img/                 # Imagens WebP otimizadas
```

## Diretrizes da cliente (visíveis em todas as variantes)

- Imagem e texto em paralelo, sempre que possível
- Bloco de preço com valor cheio riscado, valor à vista em destaque e selo de economia
- Botões claros que escurecem no hover
- Degradê vertical da página (claro → escuro)
- Imagens dos programas clicáveis para ampliar (lightbox)
- Mobile-friendly

Para mais detalhes técnicos e arquiteturais, ver [AGENTS.md](AGENTS.md).

## Próximos passos

1. Apresentar `/` para a cliente
2. Cliente escolhe variante
3. Remover as duas variantes não escolhidas e a página-índice
4. Promover a vencedora para `/`
