# AGENTS.md — Equilibrar Psicanálise

Guia para agentes de IA (Claude, Codex, etc.) trabalharem neste repositório com contexto correto.

## O que é

Site institucional da **Equilibrar Psicanálise Clínica**, atendimento por Letícia Gomes de Carvalho (psicanalista clínica + neurociência aplicada). Single-page application server-rendered com FastAPI + Jinja2 + Tailwind CDN.

> **Estado atual: fase de escolha de variante.** O site está temporariamente publicando **3 variantes visuais distintas em URLs separadas** para a cliente escolher uma. Após a escolha, o sobrinho dev (Deivid) deve eliminar as duas variantes não selecionadas e consolidar.

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | FastAPI + Uvicorn (Python 3.12) |
| Templating | Jinja2 (templates em `templates/`) |
| CSS | Tailwind via CDN (config inline em `base.html`) + CSS custom em `static/css/style.css` |
| Animações | AOS 2.3.1 (CDN) |
| Fontes | Now (woff2 local em `static/fonts/`) + Lora (Google Fonts) |
| Imagens | WebP otimizado (qualidade 82) em `static/img/` |
| E-mail | SMTP Gmail (`app/services/email_service.py`) — credenciais em `.env` |

## Como rodar

```bash
source env/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Acessar:
- `/` — página-índice com 3 cards de prévia (escolha)
- `/acolhimento` — Variante 1
- `/profundidade` — Variante 2
- `/clinico` — Variante 3
- `POST /contato` — endpoint do formulário

Variáveis de ambiente em `.env` (não commitar):
```
SMTP_USER=...
SMTP_PASSWORD=...
SERVER_PORT=8000
```

## Estrutura de arquivos

```
app/
├── main.py                  # FastAPI app + StaticFiles mount
├── api/routers.py           # 4 rotas GET + POST /contato
├── core/
│   ├── config.py            # Pydantic settings (.env)
│   ├── logger.py            # loguru
│   └── site_content.py      # CONTEÚDO TEXTUAL DO SITE (única fonte de verdade)
└── services/email_service.py
templates/
├── base.html                # Layout base — header, footer, lightbox, scripts
├── _macros.html             # Macros: section_image_text, cta_button, price_block, programa_passos
├── _form_contato.html       # Formulário de contato (incluído por todas as variantes)
├── escolha.html             # Página-índice "/" com 3 cards de prévia
├── v1_acolhimento.html      # Variante 1
├── v2_profundidade.html     # Variante 2
└── v3_clinico.html          # Variante 3
static/
├── css/style.css            # Variáveis CSS, classes de tema (.theme-*), price-block, lightbox
├── fonts/
│   ├── Now-Regular.woff2
│   └── Lora-Regular.woff2
└── img/
    ├── favicon.png                                            # 32×32 derivado
    ├── logo_com_nome_psicanalise.webp                          # Header (fundo claro)
    ├── logo_com_fundo_roxo.webp                                # Footer (combina com fim do degradê)
    ├── foto_profissional_2.webp                                # Hero + Sobre mim
    ├── psicanalise_e_neurociencia_compreender_para_transformar.webp  # Abordagem
    ├── 5c_clareza_direcao.webp                                 # Programa 5C
    ├── programa_o_profundo_em_mim_compreender_para_transformar.webp  # Programa 2
    ├── crescer_sem_drama_criancas_adolescentes.webp            # Programa 3
    ├── foto_corporativa.webp                                   # NR-1 / empresas
    └── leticia_livro.webp                                      # Livro
```

## Onde está o quê

| Quero alterar… | Editar… |
|---|---|
| Texto de qualquer seção | `app/core/site_content.py` (centraliza tudo) |
| Headline, subhead, CTAs | `app/core/site_content.py` |
| Valor dos programas | `app/core/site_content.py` → `PRECO` |
| Lista de passos do programa 5C | `app/core/site_content.py` → `PROGRAMAS[0]['passos']` |
| Layout do hero da variante X | `templates/v{X}_*.html` |
| Logo no header | `templates/base.html` (linha do `<img>` no header) |
| Cores do degradê de uma variante | `static/css/style.css` → `.theme-acolhimento` / `.theme-profundidade` / `.theme-clinico` |
| Header/footer compartilhado | `templates/base.html` |
| Estilo visual de bloco de preço | `static/css/style.css` → `.price-block` + macro `price_block` em `_macros.html` |
| Lightbox (modal de zoom) | `templates/base.html` (HTML + JS no final) |
| Adicionar nova rota | `app/api/routers.py` |

## Convenções e padrões

### Conteúdo
- **Toda string textual** mostrada ao usuário **vive em `app/core/site_content.py`**. Nunca hardcode texto em template.
- A função `get_content()` retorna o dict completo; `_base_context()` em `routers.py` adiciona `current_year` e `doctoralia_url`.
- Links de WhatsApp pré-formatados via helper `_wa(text)` em `site_content.py` — preserva URL-encoding correto.

### Imagens
- Sempre **WebP qualidade 82** (suficiente para infográficos; foto humana pode demandar qualidade maior se ficar perceptível).
- Toda `<img>` tem `alt` descritivo e `loading="lazy"` (exceto hero).
- Imagens com texto/diagrama denso (infográficos dos programas, abordagem) **devem ter o atributo `data-lightbox`** envolvendo um `<button>` para abrir em zoom no modal.
- A foto profissional da Letícia **NÃO usa crop circular** — preferência da cliente. Usar formato retangular vertical (`object-cover` em container com `rounded-[2rem]` ou similar).

### Tipografia
- **Now** (sans-serif): headlines, CTAs, eyebrows. Fonte da marca.
- **Lora** (serif): corpos de texto, citações, destaques emocionais.
- Cada variante tem proporção própria entre as duas (ver "Variantes" abaixo).

### Cores oficiais (Social Guide)

| Token Tailwind | Hex | Uso típico |
|---|---|---|
| `brand-branco` | `#FFFFFF` | Cards, fundo neutro |
| `brand-bege` | `#F4EBE1` | Topo do degradê (cor "acolhedora") |
| `brand-amarelo` | `#FEF217` | **Apenas em destaques** (selo de economia, palavras-chave) |
| `brand-lilas_claro` | `#C9B8DC` | Transição do degradê |
| `brand-lilas` | `#A38DC4` | **Botões em repouso**, cards leves |
| `brand-roxo_apagado` | `#775C97` | Texto secundário, intermediário do degradê |
| `brand-roxo` | `#4D3166` | Texto primário, **botões no hover**, fim do degradê |
| `brand-azul_claro` | `#CEDFE9` | Topo do degradê na variante /clinico |

> **Nota da cliente**: as imagens (infográficos profissionais entregues pela agência) usam tons mais etéreos que fogem um pouco da paleta. **Não tente fielmente combinar cores da paleta com cores da imagem** — manter a paleta para UI e deixar as imagens preservarem seu look.

### Padrão de botões (regra forte)
**Repouso = claro; hover = escurece.** Inverso do padrão tradicional.

```html
<a class="bg-brand-lilas text-brand-roxo
          hover:bg-brand-roxo hover:text-white
          transition-colors duration-300
          focus-visible:ring-2 focus-visible:ring-brand-roxo">
  Texto
</a>
```

Macro `cta_button` em `_macros.html` aplica isso. Use a macro sempre que possível. Exceção: WhatsApp flutuante (verde por convenção universal).

### Padrão de preço (regra forte)
A cliente exige que **a economia esteja sempre visível**. Sempre usar a macro `price_block(preco)` que renderiza:

```
De ~~R$ 2.760~~          (riscado, cinza)
R$ 2.208 à vista         (destaque grande, roxo)
no PIX ou transferência
─────────────
ou 12x R$ 230 sem juros no cartão de crédito
[selo amarelo] ✓ Você economiza R$ 552
```

Nunca remover o riscado nem o selo de economia.

### Padrão visual: imagem + texto em paralelo
Sempre que possível, layout de duas colunas (imagem | texto) que vira coluna única em mobile via `flex-col md:flex-row`. Para isso, usar a macro `section_image_text(...)` ou replicar manualmente quando a seção exigir customização.

### Botão de "ampliar imagem" (lightbox)
Imagens densas (infográficos) ficam dentro de um `<button data-lightbox data-lightbox-caption="Texto">`. O JS no `base.html` captura o clique e abre o modal `#lightbox` em fullscreen. Acessibilidade: ESC fecha, foco volta para o trigger, role="dialog" aria-modal="true".

### Acessibilidade
- Cada infográfico **deve ter** sua lista de passos repetida em texto via macro `programa_passos(passos)` (WCAG 1.1.1 — equivalente textual).
- Todos `<svg>` decorativos têm `aria-hidden="true"`. SVGs informativos (redes sociais) têm `role="img"` e `aria-label`.
- Animações AOS desabilitam automaticamente com `prefers-reduced-motion`.
- Botões com `cursor-zoom-in` e estado de foco visível (`focus-visible:ring-*`).

### Mobile
- Tudo testa em viewport 375px (iPhone SE).
- `background-attachment: fixed` cai para `scroll` em mobile (`@media max-width: 768px` no style.css) — bug iOS conhecido.
- Imagens de programa em `programa-img` (object-contain) para nunca estourar viewport.
- Botões com altura mínima 44px (área de toque).

## As 3 variantes

| Variante | URL | Personalidade | Degradê | Tipografia dominante | Cards |
|---|---|---|---|---|---|
| **1 — Acolhimento** | `/acolhimento` | Calor terapêutico, íntimo, feminino | `#F4EBE1` → `#C9B8DC` → `#A38DC4` (não chega ao escuro) | **Lora itálico** em headlines, Now em CTAs/eyebrows | `rounded-[2rem]`, sombras suaves, `.soft-card` |
| **2 — Profundidade** | `/profundidade` | Cinemático, denso, contemplativo | `#F4EBE1` → `#A38DC4` → `#4D3166` (completo até roxo escuro) | **Now** em escala dramática (text-6xl/7xl), Lora em corpos longos | `rounded-2xl`, transparência sobre degradê, `.deep-card` / `.reading-card` |
| **3 — Clínico Moderno** | `/clinico` | Institucional, científico, organizado | `#FFFFFF` → `#CEDFE9` → `#A38DC4` → `#775C97` (cores frias) | **Now** comedido em headlines, Lora pontual | `rounded-xl`/`rounded-lg`, borda fina, `.grid-card` |

A página-índice (`/` → `escolha.html`) mostra os 3 lado a lado com mockup visual distinto. Após a cliente escolher, manter apenas a variante vencedora.

## Decisões e contexto da cliente (não esquecer)

1. **Sessões**: Letícia **NÃO atende avulso**. Programas de 12 sessões, R$ 2.760 cheio / R$ 2.208 PIX / 12x R$ 230 sem juros. Economia de R$ 552 deve estar visível.
2. **Programa 5C**: usar nomes da imagem oficial (Compreender / Consciência / Conexão / Coragem / Conquistar) — não os do DOCX velho (Cognição/Comportamento/Construção). Mantém o mnemônico "todos com C".
3. **Card "Processo Colaborativo e Cuidado Personalizado"**: NÃO é um programa. Aparece como faixa após o grid de programas, não dentro dele.
4. **Foto da Letícia**: formato retangular, sem crop circular (cliente não gostou).
5. **Imagens dos programas (infográficos)**: clicáveis para ampliar (lightbox).
6. **NR-1**: tem prazo legal — empresas precisam se adequar; o site usa esse argumento sem sensacionalismo.
7. **Livro**: "Por que Você Sempre Deixa para Depois" (Editora Livro, 22/11/2025), 21 mulheres autoras. Letícia assina capítulos 3 e 4.
8. **Registro profissional**: SBPT 00352025. Sempre exibir no footer e em "Sobre".

## Coisas que NÃO fazer

- Não voltar com o crop circular na foto profissional.
- Não inventar texto novo: tudo vem do DOCX/site_content.py.
- Não remover o lightbox dos infográficos.
- Não inverter o padrão de botões (lilás claro → roxo escuro no hover, nunca o contrário).
- Não esquecer o selo "Você economiza R$ 552" nos cards de preço.
- Não converter PNGs originais que já tenham WebP equivalente (já foi feito; originais foram removidos).
- Não criar arquivos legados como `index.html` (o antigo foi removido após o rework).

## Próximos passos esperados

1. Cliente escolhe uma das 3 variantes.
2. Eliminar as 2 não escolhidas: deletar templates `v{X}_*.html` correspondentes e remover rotas em `routers.py`.
3. Renomear a vencedora para `index.html` (ou manter o nome) e fazer `/` apontar diretamente para ela.
4. Deletar `templates/escolha.html`.
5. Considerar migrar Tailwind do CDN para build local (Tailwind CLI) para produção — economiza ~300KB no first paint.
6. Configurar HTTPS (já há `equilibrar-key.pem` e `equilibrar-psicanalise.pem` no projeto).
