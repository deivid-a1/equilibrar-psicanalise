# AGENTS.md — Equilibrar Psicanálise

Guia para agentes de IA (Claude, Codex, etc.) trabalharem neste repositório com contexto correto.

## O que é

Site institucional da **Equilibrar Psicanálise Clínica**, atendimento por Letícia Gomes de Carvalho (psicanalista clínica + neurociência aplicada). Single-page application server-rendered com FastAPI + Jinja2 + Tailwind CDN.

> **Estado atual: variante consolidada.** Após apresentação de 3 propostas visuais, a cliente escolheu a variante **"Acolhimento"**. As outras (`v2_profundidade`, `v3_clinico`, `escolha`) foram removidas. A rota `/` agora serve diretamente `index.html`. Rotas legadas (`/acolhimento`, `/profundidade`, `/clinico`) redirecionam 301 para `/`.

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | FastAPI + Uvicorn (Python 3.12) |
| Templating | Jinja2 (templates em `templates/`) |
| CSS | Tailwind via CDN (config inline em `base.html`) + CSS custom em `static/css/style.css` |
| Animações | AOS 2.3.1 (CDN) |
| Fontes | Now (woff2 local em `static/fonts/`) + Lora (Google Fonts) |
| Imagens | WebP otimizado (qualidade 82-88) em `static/img/` |
| E-mail | SMTP Gmail (`app/services/email_service.py`) — credenciais em `.env` |

## Como rodar

```bash
source env/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Acessar:
- `/` — site principal
- `POST /contato` — endpoint do formulário
- `/acolhimento`, `/profundidade`, `/clinico` — redirecionam 301 para `/`

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
├── api/routers.py           # Rota / + redirects das antigas + POST /contato
├── core/
│   ├── config.py            # Pydantic settings (.env)
│   ├── logger.py            # loguru
│   └── site_content.py      # ★ CONTEÚDO TEXTUAL DO SITE (única fonte de verdade)
└── services/email_service.py
templates/
├── base.html                # Layout base — header, footer, lightbox, scripts
├── _macros.html             # Macros: section_image_text, cta_button, price_block, programa_passos
├── _form_contato.html       # Formulário de contato (incluído pelo index)
└── index.html               # Variante única (Acolhimento) — antiga v1
static/
├── css/style.css            # Variáveis CSS, .theme-acolhimento, .price-block, scroll-padding-top
├── fonts/
│   ├── Now-Regular.woff2
│   └── Lora-Regular.woff2
└── img/
    ├── favicon.png                                                 # 32×32 derivado
    ├── logo_com_nome_psicanalise.webp                              # Logo principal — usada no HEADER e FOOTER
    ├── logo_com_fundo_roxo.webp                                    # (mantida no repo, não usada atualmente)
    ├── foto_primeira_pagina.webp                                   # ★ Hero da home — Letícia (sobreposta com flip horizontal)
    ├── foto_profissional_2.webp                                    # ★ Sobre mim — Letícia (com flip horizontal)
    ├── psicanalise_e_neurociencia_compreender_para_transformar.webp  # Abordagem
    ├── 5c_clareza_direcao.webp                                     # Programa 5C
    ├── programa_o_profundo_em_mim_compreender_para_transformar.webp  # Programa 2
    ├── crescer_sem_drama_criancas_adolescentes.webp                # Programa 3
    ├── foto_corporativa.webp                                       # NR-1 / empresas
    └── leticia_livro.webp                                          # Livro
```

## Onde está o quê

| Quero alterar… | Editar… |
|---|---|
| Texto de qualquer seção | `app/core/site_content.py` (centraliza tudo) |
| Headline, subhead, CTAs | `app/core/site_content.py` |
| CTA secundário do hero ("Agende sessão gratuita") | `app/core/site_content.py` → `HERO['cta_secundario_*']` |
| Valor dos programas | `app/core/site_content.py` → `PRECO` |
| Lista de passos do programa 5C | `app/core/site_content.py` → `PROGRAMAS[0]['passos']` |
| Texto da formação acadêmica | `app/core/site_content.py` → `SOBRE['body_html']` |
| Layout do hero | `templates/index.html` |
| Logo no header e footer | `templates/base.html` (mesma imagem, tamanhos diferentes) |
| Cores do degradê | `static/css/style.css` → `.theme-acolhimento` |
| Header/footer compartilhado | `templates/base.html` |
| Estilo do bloco de preço | `static/css/style.css` → `.price-block` + macro `price_block` em `_macros.html` |
| Lightbox (modal de zoom) | `templates/base.html` (HTML + JS no final) |
| Scroll-padding para âncoras | `static/css/style.css` → `html { scroll-padding-top }` |
| Adicionar nova rota | `app/api/routers.py` |

## Convenções e padrões

### Conteúdo
- **Toda string textual** mostrada ao usuário **vive em `app/core/site_content.py`**. Nunca hardcode texto em template.
- A função `get_content()` retorna o dict completo; `_base_context()` em `routers.py` adiciona `current_year` e `doctoralia_url`.
- Links de WhatsApp pré-formatados via helper `_wa(text)` em `site_content.py` — preserva URL-encoding correto.

### Imagens
- Sempre **WebP qualidade 82** para infográficos; **88** para fotos de pessoa (preserva detalhes do rosto).
- Toda `<img>` tem `alt` descritivo e `loading="lazy"` (exceto hero).
- Imagens com texto/diagrama denso (infográficos dos programas, abordagem) **devem ter o atributo `data-lightbox`** envolvendo um `<button>` para abrir em zoom no modal.
- A foto profissional da Letícia **NÃO usa crop circular** — preferência da cliente. Usar formato retangular vertical (`object-cover` em container com `rounded-[2rem]`).
- **As fotos da Letícia já estão com flip horizontal aplicado** (re-export, não CSS). Não inverter de novo.

### Tipografia
- **Now** (sans-serif): nav, eyebrows, CTAs, número de etapas. Fonte da marca.
- **Lora** (serif): corpos de texto, citações, headlines emocionais. A classe `.tese-quote` aplica Lora itálico para a frase-tese e títulos principais.

### Cores oficiais (Social Guide)

| Token Tailwind | Hex | Uso típico |
|---|---|---|
| `brand-branco` | `#FFFFFF` | Cards, fundo neutro |
| `brand-bege` | `#F4EBE1` | Topo do degradê (cor "acolhedora") |
| `brand-amarelo` | `#FEF217` | **Apenas no selo de economia** (vibrante demais para botões) |
| `brand-amarelo_suave` | `#FBE89C` | CTA secundário "Agende sessão gratuita" e destaques pastel |
| `brand-lilas_claro` | `#C9B8DC` | Transição do degradê |
| `brand-lilas` | `#A38DC4` | **Botões em repouso**, cards leves |
| `brand-roxo_apagado` | `#775C97` | Texto secundário |
| `brand-roxo` | `#4D3166` | Texto primário, **botões no hover** |
| `brand-azul_claro` | `#CEDFE9` | Disponível na paleta (não usado na variante atual) |

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

### Padrão do CTA secundário "Agende sessão gratuita"
No hero, **abaixo** do CTA principal, há um botão sólido em **amarelo suave** (`brand-amarelo_suave` = `#FBE89C`) introduzido pela frase **"Quer me conhecer antes? A primeira conversa é gratuita."** A frase serve de chamada do botão (não fica órfã).

Estilo:
- Fundo `bg-brand-amarelo_suave`, texto `text-brand-roxo`, borda fina `border-brand-roxo/30`
- Estrela à esquerda (cor `text-brand-roxo_apagado`, sutil)
- Hover: fundo roxo escuro, texto amarelo suave (mantém padrão claro→escuro)
- Aponta para WhatsApp pré-formatado (`HERO['cta_secundario_href']`)

**Nunca** usar `brand-amarelo` (vibrante) nesse botão — a cliente disse que fica agressivo. Usar sempre `brand-amarelo_suave`.

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
Sempre que possível, layout de duas colunas (imagem | texto) que vira coluna única em mobile via `flex-col md:flex-row`.

### Botão de "ampliar imagem" (lightbox)
Imagens densas (infográficos) ficam dentro de um `<button data-lightbox data-lightbox-caption="Texto">`. O JS no `base.html` captura o clique e abre o modal `#lightbox` em fullscreen. Acessibilidade: ESC fecha, foco volta para o trigger, role="dialog" aria-modal="true".

### Header com shrink-on-scroll (regra forte)
O header é fixo e tem **dois estados visuais**:

1. **Expandido** (estado inicial, `scrollY <= 80`): logo grande e bem legível
   - Inner: 7rem mobile / 8rem md / 9rem lg (112/128/144px)
   - Logo: max-height 6.5/7.5/8.5rem · max-width 320/380/450px
2. **Encolhido** (após rolar mais que 80px): logo enxuta, mais espaço para conteúdo
   - Inner: 4.5rem mobile / 5rem md (72/80px)
   - Logo: max-height 4/4.5rem · max-width 200/220px

Implementação:
- CSS: classes `.site-header`, `.site-header-inner`, `.site-logo` em `style.css` com `transition: max-height 0.35s ease, max-width 0.35s ease`
- JS: listener de scroll em `base.html` adiciona/remove `is-scrolled` no `#siteHeader`
- `<main>` tem `padding-top` fixo (`.site-main { padding-top }`) correspondente ao tamanho expandido
- A logo usa `max-width` além de `max-height` para garantir que NÃO invada o nav (a imagem é horizontal com aspect ~2.94:1)

**Nunca** mexer nas classes Tailwind `h-X` da logo do header diretamente — usar as classes utilitárias `.site-logo` e os media queries em `style.css`.

**Cache-busting**: a URL da logo no template usa `?v=N` para invalidar cache do navegador quando a imagem é re-exportada. Incrementar `v` quando trocar o arquivo `logo_com_nome_psicanalise.webp`.

**Imagem da logo**: a imagem foi cortada (auto-crop) para remover o whitespace transparente em volta do conteúdo. Tamanho final: 1168x397 (aspect 2.94:1). NÃO re-exportar com whitespace ou o tamanho aparente vai ficar pequeno de novo. Se precisar re-cortar, usar PIL com threshold de alpha — ver script no histórico do AGENTS.md.

### Scroll para âncoras
- `html { scroll-padding-top: 6rem }` (7rem em md+) — corresponde ao header **encolhido**, pois o usuário só clica no menu após rolar (header já está pequeno).
- Cada `<section id="...">` tem `scroll-margin-top: 6rem` como reforço.

### Acessibilidade
- Cada infográfico **deve ter** sua lista de passos repetida em texto via macro `programa_passos(passos)` (WCAG 1.1.1 — equivalente textual).
- Todos `<svg>` decorativos têm `aria-hidden="true"`. SVGs informativos (redes sociais) têm `role="img"` e `aria-label`.
- Animações AOS desabilitam automaticamente com `prefers-reduced-motion`.
- Botões com `cursor-zoom-in` e estado de foco visível (`focus-visible:ring-*`).

### Mobile
- Tudo testa em viewport 375px (iPhone SE).
- `background-attachment: fixed` cai para `scroll` em mobile (`@media max-width: 768px` no style.css) — bug iOS conhecido.
- Imagens de programa com `object-contain` para nunca estourar viewport.
- Botões com altura mínima 44px (área de toque).

## Decisões e contexto da cliente (não esquecer)

1. **Sessões**: Letícia **NÃO atende avulso**. Programas de 12 sessões, R$ 2.760 cheio / R$ 2.208 PIX / 12x R$ 230 sem juros. Economia de R$ 552 deve estar visível.
2. **Sessão gratuita inicial**: O hero tem CTA secundário "Agende uma sessão gratuita" — primeira conversa para conhecer Letícia e os programas.
3. **Programa 5C**: usar nomes da imagem oficial (Compreender / Consciência / Conexão / Coragem / Conquistar) — não os do DOCX antigo.
4. **Card "Processo Colaborativo e Cuidado Personalizado"**: NÃO é um programa. Aparece como faixa após o grid de programas, não dentro dele.
5. **Foto da Letícia**: formato retangular, sem crop circular (cliente não gostou). E **espelhada horizontalmente** (re-export já aplicado) — selfies costumam vir invertidas.
6. **Imagens dos programas (infográficos)**: clicáveis para ampliar (lightbox).
7. **Logo**: usar a mesma `logo_com_nome_psicanalise.webp` no header e no footer (cliente não quer a versão com fundo roxo no footer).
8. **NR-1**: tem prazo legal — empresas precisam se adequar; o site usa esse argumento sem sensacionalismo.
9. **Livro**: "Por que Você Sempre Deixa para Depois" (Editora Livro, 22/11/2025), 21 mulheres autoras. Letícia assina capítulos 3 e 4.
10. **Registro profissional**: SBPT 00352025. Sempre exibir no footer e em "Sobre".
11. **Formação atualizada**: graduação Ciências Sociais UMESP / formação e especialização em Psicanálise Clínica IUPC-SP / especialização em Neurociência Aplicada: Produtividade e Performance Humana PUC-PR / formação continuada em TCC e Neurociências na Prática Clínica.

## Coisas que NÃO fazer

- Não voltar com o crop circular na foto profissional.
- Não inverter as fotos de novo (já estão com flip aplicado).
- Não inventar texto novo: tudo vem do DOCX/site_content.py.
- Não remover o lightbox dos infográficos.
- Não inverter o padrão de botões (lilás claro → roxo escuro no hover, nunca o contrário).
- Não esquecer o selo "Você economiza R$ 552" nos cards de preço.
- Não remover o CTA secundário "Agende sessão gratuita" do hero.
- Não trocar a logo do footer pela versão com fundo roxo (cliente preferiu unificar).
- Não converter PNGs originais que já tenham WebP equivalente.

## Próximos passos sugeridos

1. Migrar Tailwind do CDN para build local (Tailwind CLI) — economiza ~300KB no first paint em produção.
2. Configurar HTTPS (já há `equilibrar-key.pem` e `equilibrar-psicanalise.pem` no projeto, gitignored).
3. Adicionar Open Graph tags e meta description SEO mais ricos.
4. Considerar gerar sitemap.xml e robots.txt.
5. Avaliar se `foto_corporativa.webp` (NR-1) precisa também de flip — verificar com a cliente.
