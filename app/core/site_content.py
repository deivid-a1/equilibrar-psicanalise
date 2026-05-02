"""
Conteúdo textual compartilhado pelas 3 variantes de página.
Fonte: DOCX "INSTRUÇÕES PARA POSICIONAMENTO PROFISSIONAL" enviado pela cliente.
"""

WHATSAPP_BASE = "https://wa.me/5577981609526?text="
DOCTORALIA = "https://www.doctoralia.com.br/z/U4Phnv"
INSTAGRAM = "https://www.instagram.com/equilibrarpsicanalise/"
LINKEDIN = "https://www.linkedin.com/in/let%C3%ADciagomesdecarvalho/"


def _wa(text: str) -> str:
    from urllib.parse import quote
    return WHATSAPP_BASE + quote(text)


HERO = {
    "eyebrow": "Equilibrar Psicanálise Clínica",
    "headline": "Você não sofre pelo que vive, mas pelo que não compreende em si — e repete.",
    "subheadline": (
        "Integro a profundidade da psicanálise às evidências da neurociência para compreender "
        "e transformar padrões que impactam a forma como cada pessoa pensa, sente e se posiciona "
        "na vida — seja no adulto, no adolescente ou na criança."
    ),
    "cta_label": "Conheça os programas terapêuticos",
    "cta_href": "#programas",
    "image": "/static/img/foto_profissional_2.webp",
    "image_alt": "Letícia Gomes de Carvalho, psicanalista clínica",
}

APRESENTACAO = {
    "title": "Quem te recebe",
    "body": (
        "Sou Letícia Gomes de Carvalho, psicanalista clínica e especialista em neurociência "
        "aplicada à produtividade e à performance humana. Meu trabalho é ajudar pessoas a "
        "compreenderem seus padrões inconscientes, reorganizarem a mente e superarem bloqueios "
        "que interferem em suas escolhas, emoções e decisões — para que possam sustentar uma "
        "vida com mais clareza, propósito e equilíbrio real."
    ),
}

TESE = {
    "frase": "Você não sofre pelo que vive, mas pelo que não compreende em si — e repete.",
    "explicacao": (
        "Muitas dores emocionais não surgem apenas dos acontecimentos externos, mas dos padrões "
        "internos que se repetem sem serem compreendidos. A terapia permite investigar essas "
        "repetições, compreender suas origens e construir novas formas de pensar, sentir e agir."
    ),
}

ABORDAGEM = {
    "eyebrow": "Abordagem",
    "title": "Psicanálise e Neurociência: compreender para transformar",
    "body_html": (
        "<p>A psicanálise oferece a profundidade do inconsciente — símbolos, sonhos, repetições e "
        "histórias que se acumulam em nós. A neurociência traz a evidência do cérebro — "
        "neuroplasticidade, redes neurais, memória e comportamento.</p>"
        "<p>Na Equilibrar, integro as duas para um trabalho clínico que une <strong>profundidade</strong> "
        "e <strong>direção</strong>: você não apenas entende o que sente, você reorganiza como pensa, "
        "decide e age.</p>"
    ),
    "image": "/static/img/psicanalise_e_neurociencia_compreender_para_transformar.webp",
    "image_alt": "Infográfico integrando Psicanálise e Neurociência: do inconsciente à neuroplasticidade",
}

COMO_FUNCIONA = {
    "title": "Como funciona o trabalho",
    "itens": [
        {
            "title": "Construção em parceria",
            "body": (
                "A terapia é uma construção em parceria. A partir da sua história de vida, o "
                "trabalho é direcionado à compreensão do que se repete em você — para que mudanças "
                "reais possam acontecer."
            ),
        },
        {
            "title": "Programas estruturados em 12 sessões",
            "body": (
                "Os atendimentos são realizados por meio de programas terapêuticos estruturados em "
                "12 sessões, pensados para oferecer continuidade, profundidade e compromisso com o "
                "processo."
            ),
        },
    ],
}

POR_QUE_NAO_AVULSAS = {
    "title": "Por que não trabalho com sessões avulsas",
    "body_html": (
        "<p>Não trabalho com sessões isoladas porque mudanças profundas não acontecem de forma "
        "pontual — elas exigem continuidade, estrutura e compromisso com o processo.</p>"
        "<p>Encontros esporádicos podem gerar alívio momentâneo, mas raramente promovem "
        "transformações consistentes. Por isso, os atendimentos são organizados em programas de "
        "12 sessões, favorecendo um acompanhamento progressivo, profundo e comprometido.</p>"
        "<p>Para viabilizar o processo de forma organizada, o programa pode ser realizado com "
        "condição diferenciada no pagamento à vista ou parcelado no cartão de crédito, garantindo "
        "a continuidade do acompanhamento.</p>"
    ),
}

PRECO = {
    "valor_cheio": "R$ 2.760",
    "valor_avista": "R$ 2.208",
    "parcelado": "12x R$ 230",
    "economia": "R$ 552",
    "forma_avista": "PIX ou transferência",
    "forma_parcelado": "sem juros no cartão de crédito",
}

PROGRAMAS = [
    {
        "id": "5c",
        "nome": "Programa 5C",
        "subtitulo": "Clareza & Direção",
        "slogan": "Se você continua vivendo as mesmas dores, o problema não é a vida — é o que se repete em você.",
        "publico": (
            "Para quem sente que está repetindo ciclos, adiando decisões e vivendo com a sensação "
            "de que poderia avançar, mas não consegue."
        ),
        "descricao": (
            "Plano exclusivo de 12 sessões para identificar bloqueios, compreender padrões e "
            "desenvolver mais clareza para tomar decisões com direção e consistência."
        ),
        "passos": [
            ("Compreender", "Investigar a fundo suas histórias, padrões e emoções."),
            ("Consciência", "Ampliar o olhar e reconhecer o que precisa ser transformado."),
            ("Conexão", "Reconectar-se com sua essência, valores e verdade interior."),
            ("Coragem", "Dar passos reais, ultrapassar limites e sair do que te prende."),
            ("Conquistar", "Alcançar clareza, direção e resultados alinhados com quem você realmente é."),
        ],
        "image": "/static/img/5c_clareza_direcao.webp",
        "cta_label": "Quero clareza e direção",
        "cta_href": _wa("Olá Letícia, gostaria de saber mais sobre o Programa 5C — Clareza & Direção."),
    },
    {
        "id": "profundo",
        "nome": "O Profundo em Mim",
        "subtitulo": "Compreender para transformar",
        "slogan": "Você não precisa recomeçar — precisa continuar avançando.",
        "publico": (
            "Para quem já iniciou uma jornada de autoconhecimento, mas sente que ainda existe algo "
            "mais profundo a compreender."
        ),
        "descricao": (
            "Programa de 12 sessões voltado para pessoas que desejam ampliar a consciência sobre si, "
            "reconhecer seus talentos, compreender angústias existenciais e transformar padrões que "
            "ainda limitam sua vida."
        ),
        "passos": [
            ("Mergulhar", "Explorar as camadas da sua mente e emoções para compreender suas raízes."),
            ("Compreender", "Dar sentido às suas vivências, dores e padrões que se repetem."),
            ("Curar", "Ressignificar feridas e liberar o que já não faz mais sentido."),
            ("Conectar", "Reconectar-se com sua essência, valores e o que realmente importa."),
            ("Construir", "Transformar insights em escolhas conscientes e alinhadas com quem você é."),
            ("Criar", "Viver com mais leveza, clareza e propósito, criando uma nova história."),
        ],
        "image": "/static/img/programa_o_profundo_em_mim_compreender_para_transformar.webp",
        "cta_label": "Quero aprofundar meu processo",
        "cta_href": _wa("Olá Letícia, gostaria de saber mais sobre o Programa O Profundo em Mim."),
    },
    {
        "id": "crescer",
        "nome": "Crescer sem Drama",
        "subtitulo": "Crianças e Adolescentes",
        "slogan": "Quando o adolescente se organiza por dentro, o comportamento se ajusta por consequência.",
        "publico": (
            "Para crianças e adolescentes que enfrentam dificuldades emocionais, comportamentais ou "
            "sociais — medo, insegurança, timidez, ansiedade, baixa autoestima, dificuldades "
            "escolares ou conflitos familiares."
        ),
        "descricao": (
            "Programa de 12 sessões com foco no acompanhamento da criança ou adolescente, com "
            "orientação aos responsáveis quando necessário, para favorecer um desenvolvimento "
            "emocional mais saudável."
        ),
        "passos": [
            ("Compreender", "Ajudar a entender suas emoções, pensamentos e comportamentos."),
            ("Acolher", "Um espaço seguro e acolhedor para expressar, ser ouvido e se sentir compreendido."),
            ("Fortalecer", "Desenvolver autoestima, autoconfiança e habilidades para lidar com desafios."),
            ("Desenvolver", "Estimular o potencial, a criatividade e escolhas conscientes."),
            ("Envolver", "A família é parte essencial do processo de crescimento saudável e consciente."),
            ("Transformar", "Conflitos viram aprendizados; desafios viram oportunidades de crescimento."),
        ],
        "image": "/static/img/crescer_sem_drama_criancas_adolescentes.webp",
        "cta_label": "Quero saber mais sobre o programa",
        "cta_href": _wa("Olá Letícia, gostaria de saber mais sobre o Programa Crescer sem Drama (crianças e adolescentes)."),
    },
]

PROCESSO_COLABORATIVO = {
    "title": "Processo Colaborativo e Cuidado Personalizado",
    "body": (
        "A terapia é um processo construído em parceria. Por isso, o trabalho é conduzido de forma "
        "individualizada, com base na sua história de vida, visando compreender os padrões que se "
        "repetem e construir mudanças reais."
    ),
}

EMPRESAS = {
    "headline": "Ignorar os riscos psicossociais hoje não é apenas uma falha de gestão — é um prejuízo anunciado.",
    "body_html": (
        "<p>Com as alterações da NR-1, as empresas precisam se adequar à gestão dos riscos "
        "psicossociais no ambiente de trabalho. Essa exigência envolve fatores como sobrecarga "
        "emocional, pressão por resultados, conflitos, estresse, desorganização interna, "
        "absenteísmo e adoecimento psíquico.</p>"
        "<p>Meu trabalho auxilia empresas na identificação e gestão desses riscos, integrando "
        "psicanálise e neurociência para promover ambientes mais saudáveis, produtivos e "
        "juridicamente mais seguros.</p>"
        "<p>O resultado é claro: <strong>menos afastamentos, menos conflitos, mais produtividade e "
        "maior segurança</strong> para a empresa.</p>"
    ),
    "image": "/static/img/foto_corporativa.webp",
    "image_alt": "Atendimento corporativo — gestão de riscos psicossociais NR-1",
    "cta_label": "Agende uma reunião de diagnóstico",
    "cta_href": _wa("Olá Letícia, gostaria de conversar sobre consultoria NR-1 para a minha empresa."),
}

LIVRO = {
    "title": "Autora Publicada",
    "body_html": (
        "<p>Sou coautora do livro <em>Por que Você Sempre Deixa para Depois</em> "
        "(Editora Livro, 2025), publicado em 22 de novembro de 2025, ao lado de outras 21 mulheres.</p>"
        "<p>Assino dois capítulos que dialogam diretamente com a base do meu trabalho clínico:</p>"
        "<ul class='list-disc pl-5 space-y-2'>"
        "<li><strong>Capítulo 3 — \"Ecos do Passado: A Prisão das Histórias Não Escolhidas\"</strong>: "
        "como experiências da infância continuam atuando na vida adulta, influenciando escolhas, "
        "comportamentos e mantendo ciclos de procrastinação e sofrimento.</li>"
        "<li><strong>Capítulo 4 — \"É doloroso, mas é o que eu conheço. E não consigo sair disso.\"</strong>: "
        "por que permanecemos em situações que nos fazem sofrer, mesmo sabendo que não nos fazem "
        "bem — analisando o processo sob a ótica da psicanálise e da neurociência.</li>"
        "</ul>"
        "<p>O livro reúne histórias e reflexões profundas de outras mulheres, cada uma trazendo "
        "perspectivas únicas. A leitura completa amplia o olhar — e convida a um autoconhecimento "
        "ainda mais profundo.</p>"
    ),
    "image": "/static/img/leticia_livro.webp",
    "image_alt": "Livro 'Por que Você Sempre Deixa para Depois' com capítulos de Letícia Gomes de Carvalho",
    "cta_label": "Adquira o livro AQUI!",
    "cta_href": _wa("Olá Letícia, gostaria de adquirir o seu livro!"),
}

SOBRE = {
    "title": "Sobre mim",
    "body_html": (
        "<p>Sempre tive uma escuta naturalmente acolhedora, mas foi a minha própria trajetória de "
        "dor e autoconhecimento que revelou, com clareza, o meu propósito: ajudar outras pessoas a "
        "compreenderem e transformarem seus sofrimentos.</p>"
        "<p>Hoje, como psicanalista, ofereço um espaço seguro, ético e humanizado, conduzindo "
        "processos terapêuticos voltados à identificação e transformação de padrões inconscientes "
        "que impactam emoções, comportamentos e decisões.</p>"
        "<p>Atuo como Psicanalista Clínica e sou proprietária da Equilibrar Psicanálise — "
        "<strong>Registro SBPT 00352025</strong>.</p>"
        "<p>Minha formação inclui graduação em Ciências Sociais pela UMESP, formação em Psicanálise "
        "Clínica pelo IUPC-SP, pós-graduação em Neurociências pela PUC-PR e formação continuada em "
        "Terapia Cognitivo-Comportamental, Neurociência na Prática Clínica e Hipnose Terapêutica.</p>"
    ),
    "image": "/static/img/foto_profissional_2.webp",
    "image_alt": "Letícia Gomes de Carvalho",
}

CHAMADA_FINAL = {
    "title": "Você não precisa continuar repetindo os mesmos ciclos",
    "body": (
        "A terapia pode ser o espaço onde aquilo que se repete começa, finalmente, a ser "
        "compreendido e transformado."
    ),
    "cta_label": "Iniciar meu processo terapêutico",
    "cta_href": "#contato",
}

REDES = {
    "doctoralia": DOCTORALIA,
    "instagram": INSTAGRAM,
    "linkedin": LINKEDIN,
    "whatsapp": _wa("Olá Letícia, vim pelo seu site!"),
}


def get_content() -> dict:
    """Retorna o dicionário completo de conteúdo do site, consumido pelas 3 variantes."""
    return {
        "hero": HERO,
        "apresentacao": APRESENTACAO,
        "tese": TESE,
        "abordagem": ABORDAGEM,
        "como_funciona": COMO_FUNCIONA,
        "por_que_nao_avulsas": POR_QUE_NAO_AVULSAS,
        "preco": PRECO,
        "programas": PROGRAMAS,
        "processo_colaborativo": PROCESSO_COLABORATIVO,
        "empresas": EMPRESAS,
        "livro": LIVRO,
        "sobre": SOBRE,
        "chamada_final": CHAMADA_FINAL,
        "redes": REDES,
    }
