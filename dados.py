# -*- coding: utf-8 -*-
"""Dados do roteiro Uruguai e Argentina (26/12/2026 a 02/01/2027).

Tudo o que aparece no site sai deste arquivo. Para mudar um horário,
trocar um restaurante ou tirar um "n/c", edite aqui e rode de novo:

    python3 gerar_site.py

Convenções
- "n/c" em qualquer texto vira um selo "não confirmado" no site.
- mapas: lista de (rótulo, busca no Google Maps).
- tipo de parada: rua, cultura, comida, cafe, doce, mov, feira, festa, pausa.
"""

VIAGEM = {
    "titulo": "Roteiro Uruguai e Argentina",
    "inicio": "2026-12-26",
    "fim": "2027-01-02",
    "viajantes": 6,
    "atualizado": "29/09/2026",
    "resumo": (
        "Sete noites: três em Montevidéu (26 a 28/12) e quatro em Buenos Aires "
        "(29/12 a 01/01), com voo de volta em 02/01. Cada dia reúne blocos que se "
        "fazem a pé; o Uber entra só para ligar um bloco ao outro."
    ),
}

# Por que os passeios estão nesta ordem (calendário de fim de ano)
ORDEM = [
    ("Dom 27/12", "É o único dia da Feria de Tristán Narvaja, por isso ele mistura feira, Av. 18 de Julio e Ciudad Vieja."),
    ("Seg 28/12", "É o único dia útil pleno em Montevidéu: nela ficam o Palacio Legislativo (só seg–sex) e a maioria dos museus."),
    ("Qua 30/12", "É o único dia de Buenos Aires com museus abertos e sem feriado: Recoleta, MALBA (meia entrada às quartas) e Museo Evita."),
    ("Qui 31/12 e Sex 01/01", "Museus, teatros e reservas fechados no padrão dos últimos anos. São dias ao ar livre, com o Réveillon. As exceções de 01/01 (Ecoparque e Salón 1923) ainda dependem de confirmação."),
    ("Domingos", "A Feria de San Telmo é só aos domingos e não cai na estadia; San Telmo entra pelo Mercado e pela rua Defensa."),
]

PREMISSAS = [
    "Chegada a Montevidéu na tarde ou noite de 26/12, com hotel no Centro/Ciudad Vieja ou em Pocitos.",
    "Travessia em 29/12 pela Buquebus direta, com saída de manhã (o horário de dezembro ainda não foi publicado).",
    "Voo de volta em 02/01 no fim da tarde ou à noite, saindo de Ezeiza.",
    "Seis adultos, sem restrição de mobilidade, com ritmo de 5 a 7 horas de caminhada por dia.",
]

NOTA_ESTIMATIVAS = (
    "Distâncias e tempos a pé são estimativas feitas a partir de mapas. Vários locais ainda não "
    "divulgaram o horário de fim de ano: onde aparece n/c, a informação não foi confirmada e "
    "precisa ser conferida em dezembro."
)

# ---------------------------------------------------------------------------
# Roteiro dia a dia
# cidade: "mvd", "ba" ou "rio" (dia da travessia)
# cena: nome da ilustração em cenas.py
# ---------------------------------------------------------------------------
DIAS = [
    {
        "id": "d26", "data": "2026-12-26", "semana": "Sáb", "cidade": "mvd", "cena": "rambla", "cor": "laranja", "foto": "letras",
        "legenda": "Letreiro Montevideo, em Pocitos",
        "titulo": "Chegada a Montevidéu",
        "lugar": "Pocitos e Rambla",
        "nota": "O dia é leve de propósito.",
        "paradas": [
            {"hora": "Tarde ou noite", "tipo": "mov", "titulo": "Transfer do aeroporto de Carrasco",
             "texto": "20 km, 25 a 40 min. Para seis pessoas, dois Ubers ou Cabifys.",
             "mapas": [("Aeroporto de Carrasco", "Aeropuerto Internacional de Carrasco, Montevideo")]},
            {"hora": "Fim de tarde", "tipo": "rua", "titulo": "Rambla de Pocitos e o letreiro “Montevideo”",
             "texto": "Na Plaza Gomensoro, tudo plano.",
             "mapas": [("Letreiro Montevideo", "Letras de Montevideo, Plaza Gomensoro, Pocitos, Montevideo")]},
            {"hora": "Depois", "tipo": "doce", "titulo": "Sorvete na Las Delicias",
             "texto": "21 de Setiembre 2729, Pocitos. Se estiver lotada, a La Cigale também tem unidade em Pocitos.",
             "mapas": [("Las Delicias", "Heladería Las Delicias, 21 de Setiembre 2729, Montevideo")]},
            {"hora": "Jantar", "tipo": "comida", "titulo": "Jantar em Punta Carretas: La Perdiz", "reserva": True,
             "texto": "Grelhados na Guipúzcoa 350, a 10 min de Uber de Pocitos; reserva só por telefone. Se chegarem "
                      "tarde e cansados, um chivito (o sanduíche nacional, com bife, presunto, queijo e ovo) na "
                      "Chivitería Marcos, em Pocitos, resolve. Chegando cedo, a noite de hoje é a única em que o Baar "
                      "Fun Fun (tango ao vivo, com reserva) abre durante a estadia.",
             "mapas": [("La Perdiz", "La Perdiz Restaurant, Guipúzcoa 350, Montevideo"),
                       ("Chivitería Marcos", "Chivitería Marcos Pocitos Montevideo")]},
        ],
    },
    {
        "id": "d27", "data": "2026-12-27", "semana": "Dom", "cidade": "mvd", "cena": "salvo", "cor": "azul", "foto": "plaza-independencia",
        "legenda": "Plaza Independencia e Palacio Salvo",
        "titulo": "Cordón, 18 de Julio e Ciudad Vieja",
        "lugar": "Feira, avenida e cidade velha",
        "nota": "Único domingo da viagem: dia da Feria de Tristán Narvaja.",
        "aviso": ("O jantar deste dia precisa ser redefinido",
                  "A La Pulpería não serve jantar aos domingos (só almoço, 12h–16h) e o Baar Fun Fun fecha aos "
                  "domingos. Vejam as opções na última parada e na página Reservas."),
        "paradas": [
            {"hora": "9h", "tipo": "feira", "titulo": "Feria de Tristán Narvaja", "foto": "tristan-narvaja",
             "texto": "No Cordón, só aos domingos; chegue cedo. Reserve 1h30 a 2h.",
             "mapas": [("Feria de Tristán Narvaja", "Feria de Tristán Narvaja, Cordón, Montevideo")]},
            {"hora": "11h30", "tipo": "rua", "extra": ["doce"], "titulo": "A pé pela Av. 18 de Julio até a Plaza Independencia",
             "texto": "Cerca de 1,7 km, 20 a 25 min, passando pela Plaza Cagancha e pelo Centro de Fotografía. "
                      "Sorvete no caminho, na La Cigale (18 de Julio 1179; horário de domingo n/c).",
             "mapas": [("Plaza Cagancha", "Plaza Cagancha, Montevideo"),
                       ("La Cigale", "La Cigale, Av. 18 de Julio 1179, Montevideo")]},
            {"hora": "13h", "tipo": "rua", "titulo": "Plaza Independencia, Puerta de la Ciudadela e Palacio Salvo", "foto": "salvo",
             "texto": "Palacio Salvo por fora ou com visita. Depois a Peatonal Sarandí até o porto.",
             "mapas": [("Plaza Independencia", "Plaza Independencia, Montevideo"),
                       ("Palacio Salvo", "Palacio Salvo, Montevideo")]},
            {"hora": "13h30", "tipo": "comida", "titulo": "Almoço no Mercado del Puerto", "foto": "mercado-puerto",
             "texto": "Aberto aos domingos, das 10h às 17h. Parrilla em El Palenque, Cabaña Verónica, La Chacra ou El Peregrino.",
             "mapas": [("Mercado del Puerto", "Mercado del Puerto, Montevideo")]},
            {"hora": "15h", "tipo": "cultura", "titulo": "Museo del Carnaval", "foto": "candombe",
             "texto": "Ao lado do mercado. Confirmar o horário de domingo.",
             "mapas": [("Museo del Carnaval", "Museo del Carnaval, Rambla 25 de Agosto de 1825 218, Montevideo")]},
            {"hora": "16h", "tipo": "cultura", "titulo": "Visita guiada ao Teatro Solís", "foto": "solis",
             "texto": "Sábado e domingo às 15h e 16h. Fica a cerca de 15 min a pé do museu.",
             "mapas": [("Teatro Solís", "Teatro Solís, Montevideo")],
             "links": [("Horários do Solís", "https://www.teatrosolis.org.uy/categoria/Horarios-119")]},
            {"hora": "17h", "tipo": "cafe", "titulo": "Café histórico no El Facal",
             "texto": "18 de Julio esq. Yi, a cerca de 15 min a pé do Solís. O Baar Fun Fun e o Café Brasilero fecham "
                      "aos domingos.",
             "mapas": [("El Facal", "El Facal, 18 de Julio y Yi, Montevideo")]},
            {"hora": "Noite", "tipo": "comida", "extra": ["mov"], "titulo": "Jantar em Punta Carretas (a definir)",
             "texto": "A Ciudad Vieja esvazia depois das 18h: voltem de Uber. A La Pulpería (Lagunillas 448) só serve "
                      "jantar de terça a sexta; no domingo abre só no almoço, das 12h às 16h, e não aceita reserva. "
                      "Opções: jantar hoje na García Parrilla (aberta todos os dias) e escolher outra casa para segunda, "
                      "ou trocar o almoço do Mercado del Puerto por um almoço na La Pulpería.",
             "mapas": [("La Pulpería", "La Pulpería, Lagunillas 448, Montevideo"),
                       ("García Parrilla", "Garcia Parrilla, Guipuzcoa 331, Montevideo")],
             "links": [("Site da La Pulpería", "https://lapulperia.com.uy")]},
        ],
    },
    {
        "id": "d28", "data": "2026-12-28", "semana": "Seg", "cidade": "mvd", "cena": "faro", "cor": "rosa", "foto": "faro",
        "legenda": "Farol de Punta Carretas",
        "titulo": "Aguada, Ciudad Vieja e pôr do sol na Rambla",
        "lugar": "Legislativo, museus e Punta Carretas",
        "nota": "Único dia útil pleno em Montevidéu.",
        "paradas": [
            {"hora": "10h30", "tipo": "cultura", "extra": ["mov"], "titulo": "Palacio Legislativo", "foto": "legislativo",
             "texto": "Uber de 10 min até a Av. de las Leyes, na Aguada. Visita guiada às 11h (e às 16h), de segunda a "
                      "sexta, em espanhol, português ou inglês, com 30 a 45 min. Não precisa agendar: paga-se na hora, "
                      "US$ 3 ou UYU 140, só em dinheiro. Levem documento.",
             "mapas": [("Palacio Legislativo", "Palacio Legislativo, Montevideo")],
             "links": [("Descubrí Montevideo", "https://www.descubrimontevideo.uy/palacio-legislativo")]},
            {"hora": "12h", "tipo": "comida", "titulo": "Mercado Agrícola (MAM)",
             "texto": "A cerca de 10 min a pé do Legislativo, para um almoço leve.",
             "mapas": [("MAM", "Mercado Agrícola de Montevideo, José L. Terra 2220")]},
            {"hora": "13h30", "tipo": "cultura", "extra": ["doce"], "titulo": "Ciudad Vieja: escolham três ou quatro",
             "texto": "Uber de volta. Plaza Matriz e Cabildo (até 17h45), Museo Torres García (até 18h), Museo del Gaucho "
                      "y de la Moneda (até 18h, tours de hora em hora), MAPI (grátis às segundas) ou Museo Andes 1972 "
                      "(até 17h). Entre um museu e outro, sorvete na Piwo Helados (Sarandí 340).",
             "mapas": [("Plaza Matriz", "Plaza Matriz, Montevideo"),
                       ("Museo Andes 1972", "Museo Andes 1972, Rincón 619, Montevideo"),
                       ("Piwo Helados", "Piwo Helados, Sarandí 340, Montevideo")]},
            {"hora": "16h30", "tipo": "cafe", "titulo": "Café histórico na Ciudad Vieja",
             "texto": "Café Brasilero (Ituzaingó 1447, desde 1877; seg–sex até 19h). O Baar Fun Fun fecha às segundas.",
             "mapas": [("Café Brasilero", "Café Brasilero, Ituzaingó 1447, Montevideo")]},
            {"hora": "17h30", "tipo": "rua", "extra": ["mov"], "titulo": "Faro de Punta Carretas e pôr do sol",
             "texto": "Uber até Punta Carretas para o Faro (horário n/c), a Rambla e o pôr do sol. "
                      "O Punta Carretas Shopping fica aberto até 21h.",
             "mapas": [("Faro de Punta Carretas", "Faro de Punta Carretas, Montevideo")]},
            {"hora": "Jantar", "tipo": "comida", "extra": ["doce"], "titulo": "Jantar na Garcia Parrilla", "reserva": True,
             "texto": "Guipuzcoa 331; aberta todos os dias, reservar. A La Pulpería fecha às segundas, por isso ficou no "
                      "domingo. Sobremesa: Los Trovadores (Gabriel Pereira 3202; doces de leite), se o trajeto permitir.",
             "mapas": [("Garcia Parrilla", "Garcia Parrilla, Guipuzcoa 331, Montevideo"),
                       ("Los Trovadores", "Los Trovadores, Gabriel Pereira 3202, Montevideo")]},
        ],
    },
    {
        "id": "d29", "data": "2026-12-29", "semana": "Ter", "cidade": "rio", "cena": "travessia", "cor": "celeste", "foto": "buquebus",
        "legenda": "Ferry da Buquebus no Rio da Prata",
        "titulo": "Travessia e primeira tarde em Buenos Aires",
        "lugar": "Rio da Prata, Plaza de Mayo e Puerto Madero",
        "nota": "O Museo Casa Rosada fecha às terças.",
        "paradas": [
            {"hora": "Manhã", "tipo": "mov", "titulo": "Terminal da Buquebus, porto de Montevidéu",
             "texto": "Check-out e chegada ao terminal de 1h30 a 2h antes do embarque. A imigração é feita ali. "
                      "A travessia direta leva 2h15 a 2h30.",
             "mapas": [("Terminal Buquebus Montevidéu", "Terminal Buquebus, Rambla 25 de Agosto de 1825, Montevideo")]},
            {"hora": "Início da tarde", "tipo": "mov", "titulo": "Chegada a Puerto Madero",
             "texto": "Terminal na Av. Antártida Argentina 821. Hotel de Uber e almoço leve por perto.",
             "mapas": [("Terminal Buquebus Buenos Aires", "Terminal Buquebus, Av. Antártida Argentina 821, Buenos Aires")]},
            {"hora": "Tarde", "tipo": "rua", "titulo": "Bloco A a pé: Plaza de Mayo", "foto": "casa-rosada",
             "texto": "Plaza de Mayo, Casa Rosada (fachada), Catedral Metropolitana, Cabildo e Av. de Mayo.",
             "mapas": [("Plaza de Mayo", "Plaza de Mayo, Buenos Aires")]},
            {"hora": "Merenda", "tipo": "cafe", "titulo": "Café Tortoni", "foto": "tortoni",
             "texto": "Av. de Mayo 825, de 1858. O clássico é chocolate quente com churros; pode ter fila. "
                      "Alternativa perto da Plaza de Mayo: Green Eat (Florida 102), cafeteria citada em vídeo de viagem.",
             "mapas": [("Café Tortoni", "Café Tortoni, Av. de Mayo 825, Buenos Aires"),
                       ("Green Eat", "Green Eat, Florida 102, Buenos Aires")]},
            {"hora": "Noite", "tipo": "comida", "extra": ["rua", "doce"], "titulo": "Puerto Madero e a Puente de la Mujer", "foto": "puente-mujer",
             "texto": "Jantar por lá: El Mercado ou Cabaña Las Lilas, com reserva. Opção mais barata: pizza na Güerrín "
                      "(Av. Corrientes 1368) e sorvete na Cadore (Av. Corrientes 1695), três quadras adiante.",
             "mapas": [("Puente de la Mujer", "Puente de la Mujer, Puerto Madero, Buenos Aires"),
                       ("Güerrín", "Pizzería Güerrín, Av. Corrientes 1368, Buenos Aires"),
                       ("Cadore", "Heladería Cadore, Av. Corrientes 1695, Buenos Aires")]},
        ],
        "aviso": ("Se escolherem a saída das 20h",
                  "A terça ganha um dia inteiro em Montevidéu (Museo Andes 1972, Palacio Taranco, Teatro Solís) e a "
                  "chegada a Buenos Aires fica para as 22h45. Nesse caso, o bloco A de Buenos Aires passa para a "
                  "tarde de 31/12 e para 01/01, quando a Plaza de Mayo e a Av. de Mayo ainda podem ser vistas por fora."),
    },
    {
        "id": "d30", "data": "2026-12-30", "semana": "Qua", "cidade": "ba", "cena": "recoleta", "cor": "verde", "foto": "floralis",
        "legenda": "Floralis Genérica, a flor de aço de 23 m da Recoleta",
        "titulo": "Recoleta e Palermo",
        "lugar": "Dia forte de museus",
        "nota": "Único dia de Buenos Aires com museus abertos e sem feriado.",
        "aviso": ("Jantar de hoje: reservem já",
                  "Em 29/09, o Don Julio já não tinha jantar para 6 pessoas em 30/12 (havia almoço para 6 e jantar para "
                  "2 a 4). O Fogón Asado da Uriarte tinha só 2 vagas no jantar; a unidade da Gorriti 3780 tinha 22. "
                  "Links e contatos na página Reservas."),
        "paradas": [
            {"hora": "9h", "tipo": "cultura", "titulo": "Cementerio de la Recoleta", "foto": "recoleta",
             "texto": "Abre às 9h; estrangeiro paga; visita guiada gratuita em espanhol.",
             "mapas": [("Cementerio de la Recoleta", "Cementerio de la Recoleta, Junín 1760, Buenos Aires")]},
            {"hora": "10h30", "tipo": "cultura", "titulo": "Floralis Genérica e Museo Nacional de Bellas Artes",
             "texto": "Av. del Libertador 1473; grátis; abre às 11h. A cerca de 10 min a pé do cemitério.",
             "mapas": [("Floralis Genérica", "Floralis Genérica, Buenos Aires"),
                       ("Bellas Artes", "Museo Nacional de Bellas Artes, Av. del Libertador 1473, Buenos Aires")]},
            {"hora": "12h30", "tipo": "comida", "extra": ["cultura", "doce"], "titulo": "Centro Cultural Recoleta e almoço na La Biela",
             "texto": "O Centro Cultural abre às 12h30 nas quartas. La Biela fica na Av. Quintana 596. "
                      "Sorvete na Persicco ou na Un’Altra Volta, ambas na Av. Quintana.",
             "mapas": [("La Biela", "La Biela, Av. Quintana 596, Buenos Aires"),
                       ("Persicco Quintana", "Persicco, Av. Quintana 595, Buenos Aires")]},
            {"hora": "14h30", "tipo": "cultura", "titulo": "Escolham um: El Ateneo ou Arte Decorativo", "foto": "ateneo",
             "texto": "El Ateneo Grand Splendid (Av. Santa Fe 1860), a cerca de 15 min a pé, ou o Museo Nacional de Arte "
                      "Decorativo, no Palacio Errázuriz (Av. del Libertador 1902; qua–dom das 13h às 19h, grátis, visita "
                      "guiada às 16h segundo um guia de turismo; confirmar).",
             "mapas": [("El Ateneo", "El Ateneo Grand Splendid, Av. Santa Fe 1860, Buenos Aires"),
                       ("Arte Decorativo", "Museo Nacional de Arte Decorativo, Av. del Libertador 1902, Buenos Aires")]},
            {"hora": "16h", "tipo": "cultura", "extra": ["mov"], "titulo": "MALBA e Museo Evita",
             "texto": "Uber ou subte D até o MALBA (Av. Figueroa Alcorta 3415; às quartas, meia entrada). Depois o Museo "
                      "Evita (Lafinur 2988; até 19h), a cerca de 12 min a pé. Se apertar, cortem o Ateneo ou o Centro Cultural.",
             "mapas": [("MALBA", "MALBA, Av. Figueroa Alcorta 3415, Buenos Aires"),
                       ("Museo Evita", "Museo Evita, Lafinur 2988, Buenos Aires")]},
            {"hora": "Noite", "tipo": "comida", "extra": ["feira", "doce"], "titulo": "Palermo Soho: compras e jantar de carne", "foto": "asado", "reserva": True,
             "texto": "Marcas argentinas nas ruas Honduras, Armenia e Gurruchaga. Escolham uma reserva: Don Julio "
                      "(Guatemala 4699), Fogón Asado (Uriarte 1423, menu de 9 etapas pré-pago) ou La Cabrera "
                      "(José A. Cabrera 5099, happy hour às 18h30). Depois, sorvete na Tufic (Guatemala 4597).",
             "mapas": [("Don Julio", "Don Julio parrilla, Guatemala 4699, Buenos Aires"),
                       ("Fogón Asado", "Fogón Asado, Uriarte 1423, Buenos Aires"),
                       ("La Cabrera", "La Cabrera, José Antonio Cabrera 5099, Buenos Aires"),
                       ("Tufic", "Tufic helados, Guatemala 4597, Buenos Aires")]},
        ],
    },
    {
        "id": "d31", "data": "2026-12-31", "semana": "Qui", "cidade": "ba", "cena": "caminito", "cor": "vermelho", "foto": "caminito",
        "legenda": "Caminito: casas pintadas com sobras de tinta dos barcos",
        "titulo": "La Boca, San Telmo e Réveillon",
        "lugar": "Caminito, Defensa e Puerto Madero",
        "nota": "Museus e teatros ficam fechados no padrão dos últimos anos: é dia de rua.",
        "paradas": [
            {"hora": "9h30", "tipo": "rua", "extra": ["mov"], "titulo": "La Boca e Caminito",
             "texto": "Uber de cerca de 15 min. Trecho de 150 m; 1 a 2 h. Vão de manhã, porque as lojas fecham por volta "
                      "das 17h–18h, e não se afastem do trecho turístico. Alternativa para quem prefere compras: Calle "
                      "Murillo (couro), em Villa Crespo.",
             "mapas": [("Caminito", "Caminito, La Boca, Buenos Aires"),
                       ("Calle Murillo", "Murillo 600, Villa Crespo, Buenos Aires")]},
            {"hora": "12h", "tipo": "comida", "extra": ["feira", "doce"], "titulo": "San Telmo: Plaza Dorrego, Defensa e Mercado", "foto": "san-telmo",
             "texto": "Mercado de San Telmo na Bolívar 970. Almoço no Bar El Federal (Carlos Calvo 599; sem reserva), no "
                      "El Desnivel (Defensa 855; barato, com fila) ou na La Brigada (Estados Unidos 465; reservar). "
                      "Sobremesa: Un’Altra Volta (Defensa 973).",
             "mapas": [("Mercado de San Telmo", "Mercado de San Telmo, Bolívar 970, Buenos Aires"),
                       ("Bar El Federal", "Bar El Federal, Carlos Calvo 599, Buenos Aires"),
                       ("El Desnivel", "El Desnivel, Defensa 855, Buenos Aires"),
                       ("La Brigada", "La Brigada, Estados Unidos 465, Buenos Aires")]},
            {"hora": "15h", "tipo": "rua", "extra": ["feira"], "titulo": "Pela Defensa até a Plaza de Mayo e Puerto Madero", "foto": "tango",
             "texto": "Cerca de 1,3 km com paralelepípedos, depois mais 1,1 km até Puerto Madero. Última parada de café "
                      "opcional no Green Eat (Florida 102). Comprem o que faltar até as 17h: supermercados fecham por volta das 18h.",
             "mapas": [("Calle Defensa", "Calle Defensa, San Telmo, Buenos Aires")]},
            {"hora": "Noite", "tipo": "festa", "titulo": "Jantar de Réveillon", "reserva": True,
             "texto": "Menu fixo, de preferência a pé do hotel ou em Puerto Madero. O subte para de rodar entre 21h e "
                      "23h30, e Uber e táxi ficam raros e caros. Opções na seção Travessia e Réveillon.",
             "mapas": [("Puente de la Mujer", "Puente de la Mujer, Puerto Madero, Buenos Aires")]},
        ],
    },
    {
        "id": "d01", "data": "2027-01-01", "semana": "Sex", "cidade": "ba", "cena": "palermo", "cor": "roxo", "foto": "rosedal",
        "legenda": "Rosedal de Palermo",
        "titulo": "Feriado tranquilo",
        "lugar": "Palermo verde e rooftop do Barolo",
        "nota": "Ecoparque e Salón 1923 ainda dependem de confirmação para 01/01.",
        "paradas": [
            {"hora": "Manhã", "tipo": "pausa", "titulo": "Durmam até tarde",
             "texto": "A cidade só abre por volta do meio-dia; museus, shoppings e a maior parte do comércio ficam fechados."},
            {"hora": "12h30", "tipo": "comida", "titulo": "Almoço em Palermo",
             "texto": "Em 01/01/2026 estavam abertos o Williamsburg (12h–24h) e o Hierro (19h–1h); Av. Corrientes e Puerto "
                      "Madero costumam ter oferta. Confirmar em dezembro.",
             "mapas": [("Williamsburg", "Williamsburg burger Palermo Buenos Aires")]},
            {"hora": "14h", "tipo": "rua", "titulo": "Ecoparque", "reserva": True,
             "texto": "Av. Sarmiento 2601, junto à Plaza Italia (subte D). Desde junho/2026 estrangeiros pagam ARS 22.650 "
                      "(≈ R$ 77); ingresso por data no site oficial. Terça a domingo e feriados, 11h–17h30 (abertura em "
                      "01/01 a confirmar); fecha com chuva.",
             "mapas": [("Ecoparque", "Ecoparque, Av. Sarmiento 2601, Buenos Aires")],
             "links": [("Ingressos do Ecoparque", "https://ecoparque.buenosaires.gob.ar/ticketera/elegir/ecoparque-entrada-general")]},
            {"hora": "15h30", "tipo": "rua", "titulo": "Bosques de Palermo e Rosedal",
             "texto": "A pé, abertos e grátis, a poucos minutos do Ecoparque.",
             "mapas": [("Rosedal", "Rosedal de Palermo, Buenos Aires")]},
            {"hora": "17h", "tipo": "doce", "extra": ["mov"], "titulo": "Sorvete na Rapa Nui, na Recoleta",
             "texto": "Uber até a Arenales 2302 (chocolate 80% cacau). Se a feira de artesanato da Plaza Francia estiver "
                      "montada (n/c em 01/01), passem por ela.",
             "mapas": [("Rapa Nui", "Rapa Nui, Arenales 2302, Buenos Aires")]},
            {"hora": "19h", "tipo": "festa", "titulo": "Salón 1923, rooftop do Palacio Barolo", "foto": "barolo", "reserva": True,
             "texto": "Av. de Mayo 1370, 16º andar, com vista da cidade ao anoitecer. De sexta a segunda há sessão às 17h "
                      "(petiscos) e às 19h e 21h (tapeo, que serve de jantar leve). Reserva obrigatória e paga "
                      "antecipado pelo site; abertura em 01/01 n/c. Fecha às terças.",
             "mapas": [("Palacio Barolo", "Palacio Barolo, Av. de Mayo 1370, Buenos Aires")],
             "links": [("Reservar no Salón 1923", "https://www.reservaonline.support/salon1923/index.html")],
             "whatsapp": ("Salón 1923", "+54 9 11 3779-8847")},
        ],
    },
    {
        "id": "d02", "data": "2027-01-02", "semana": "Sáb", "cidade": "ba", "cena": "colon", "cor": "sol", "foto": "colon",
        "legenda": "Sala do Teatro Colón, inaugurado em 1908",
        "titulo": "Despedida e voo",
        "lugar": "Teatro Colón e Ezeiza",
        "nota": "",
        "paradas": [
            {"hora": "Manhã", "tipo": "cultura", "titulo": "Visita guiada ao Teatro Colón", "reserva": True,
             "texto": "Tucumán 1171; tours diários das 10h às 16h45, em português às 11h45 e 16h. Se sobrar tempo, Museo "
                      "Casa Rosada (sáb 11h–18h) ou Fragata Sarmiento (sáb 12h–19h; ARS 1.000 em dinheiro).",
             "mapas": [("Teatro Colón", "Teatro Colón, Tucumán 1171, Buenos Aires")],
             "links": [("Visitas guiadas", "https://www.teatrocolon.org.ar/es/visitas-guiadas")]},
            {"hora": "Almoço", "tipo": "comida", "extra": ["doce"], "titulo": "Almoço de despedida perto do Colón", "foto": "obelisco",
             "texto": "Los Galgos (Callao 501, confeitaria de 1930) ou La Pipeta (San Martín 498, desde 1961; entraña). "
                      "Último sorvete na Cadore (Av. Corrientes 1695).",
             "mapas": [("Los Galgos", "Los Galgos, Callao 501, Buenos Aires"),
                       ("La Pipeta", "La Pipeta, San Martín 498, Buenos Aires"),
                       ("Cadore", "Heladería Cadore, Av. Corrientes 1695, Buenos Aires")]},
            {"hora": "Voo", "tipo": "mov", "titulo": "Aeroporto de Ezeiza",
             "texto": "Cheguem 3 horas antes (regra da LATAM); o trajeto leva 40 a 70 min. Saiam do hotel cerca de "
                      "4h30 antes do voo.",
             "mapas": [("Ezeiza", "Aeropuerto Internacional Ezeiza, Buenos Aires")]},
        ],
        "aviso": ("Se o voo for de manhã ou começo da tarde",
                  "O Colón sai do roteiro. Para mantê-lo, façam o tour na terça 29/12 às 16h, se chegarem cedo de Montevidéu."),
    },
]

# ---------------------------------------------------------------------------
# Cidades, blocos e pontos
# ponto: (nome, endereço, horário, entrada, observação) + opcionais link/mapa
# ---------------------------------------------------------------------------
def P(nome, endereco, horario, entrada, obs, link=None, mapa=None):
    return {"nome": nome, "endereco": endereco, "horario": horario, "entrada": entrada,
            "obs": obs, "link": link, "mapa": mapa}


CIDADES = {
    "mvd": {
        "nome": "Montevidéu",
        "saudacao": "Bienvenidos a",
        "foto": "rambla",
        "legenda": "Rambla de Pocitos",
        "pais": "Uruguai",
        "sigla": "UY",
        "noites": "3 noites · 26 a 28/12",
        "moeda": "UYU · 1 UYU ≈ R$ 0,13",
        "cidade_mapa": "Montevideo",
        "intro": ("A história e os museus de Montevidéu se concentram na Ciudad Vieja e na Av. 18 de Julio; só o "
                  "Legislativo e a orla pedem Uber. Valores em pesos uruguaios (UYU)."),
        "blocos": [
            {"letra": "A", "nome": "Ciudad Vieja histórica", "sub": "Tudo em cerca de 700 m, 3 a 8 min entre pontos",
             "dias": ["d27", "d28"], "pontos": [
                P("Plaza Independencia, Puerta de la Ciudadela e Mausoléu de Artigas", "", "Praça livre; mausoléu n/c",
                  "Grátis", "Ponto zero da cidade; 30 a 40 min", mapa="Plaza Independencia, Montevideo"),
                P("Palacio Salvo", "Plaza Independencia 848", "Visitas guiadas em datas mensais, vendidas na RedTickets",
                  "UYU 600 (≈ R$ 78)", "Ícone de 1928; a visita de 45 min sobe ao terraço do 25º andar e termina no Museo del Tango",
                  link="https://www.descubrimontevideo.uy/palacio-salvo"),
                P("Peatonal Sarandí", "", "Livre; lojas fecham aos domingos", "Grátis", "Eixo do bloco",
                  mapa="Peatonal Sarandí, Montevideo"),
                P("Teatro Solís", "Buenos Aires esq. Bartolomé Mitre",
                  "Visitas (grade de set/2026): qua–sex 16h; sáb–dom 15h e 16h. Ingresso só na bilheteria, no dia",
                  "UYU 400 para estrangeiros (50% de desconto com o comprovante digital da Tasa Turística); quarta grátis",
                  "Tour de 50 a 60 min em espanhol, inglês e português; acessibilidade do tour n/c",
                  link="https://www.teatrosolis.org.uy/categoria/Horarios-119", mapa="Teatro Solís, Montevideo"),
                P("Plaza Matriz e Museo Histórico Cabildo", "Juan Carlos Gómez 1362",
                  "Cabildo: seg–sex 11h–17h45, sáb e feriados 11h–17h; domingo n/c", "Grátis",
                  "Só o 1º andar é acessível", link="https://www.descubrimontevideo.uy/museo-historico-cabildo"),
                P("Museo Torres García", "Sarandí 683", "Todos os dias 10h–18h; fecha 25/12 e 01/01", "UYU 400",
                  "Rampa e elevador", link="https://www.torresgarcia.org.uy/visita.php"),
                P("Museo Gurvich", "Sarandí 522", "Seg–sex 10h–18h, sáb 11h–15h; domingo fechado", "UYU 400",
                  "Elevador", link="https://museogurvich.org/visitar/"),
            ]},
            {"letra": "B", "nome": "Ciudad Vieja oeste e porto", "sub": "5 a 8 min entre pontos; do bloco A, 15 a 20 min a pé",
             "dias": ["d27", "d28"], "pontos": [
                P("Museo del Gaucho y de la Moneda", "Cerrito 351",
                  "Seg–sáb 10h–18h; tours de hora em hora, das 10h30 às 16h30; fecha domingo", "Grátis",
                  "Dentro do Banco República", link="https://www.descubrimontevideo.uy/museo-del-gaucho-y-la-moneda"),
                P("Palacio Taranco, Museo de Artes Decorativas", "25 de Mayo 376", "Ter–sáb 11h–18h; fecha domingo e segunda",
                  "Grátis", "Na Plaza Zabala"),
                P("MAPI", "25 de Mayo 279", "Seg–sáb 10h30–17h30", "Grátis às segundas; demais dias n/c",
                  "Arte pré-colombiana", mapa="MAPI Museo de Arte Precolombino e Indígena, Montevideo"),
                P("Museo Andes 1972", "Rincón 619", "Seg–sex 10h–17h, sáb 10h–15h; domingo fechado; 24 e 31/12 só 10h–13h", "US$ 8",
                  "60 a 90 min", link="https://mandes.uy/en/"),
                P("Mercado del Puerto", "Pérez Castellano", "Seg–sáb cerca de 9h–17h, dom 10h–17h", "Entrada grátis",
                  "Pico das 12h às 15h; parrillas", mapa="Mercado del Puerto, Montevideo"),
                P("Museo del Carnaval", "Rambla 25 de Agosto de 1825, 218",
                  "Normalmente qua–dom 11h–17h; o site fala em “todos os dias” a partir de dezembro, sem data", "UYU 200",
                  "Rampas; o TripAdvisor cita fechamento em 24, 25 e 31/12 e 01/01",
                  link="https://www.descubrimontevideo.uy/museo-del-carnaval-0"),
            ]},
            {"letra": "C", "nome": "Av. 18 de Julio e Cordón", "sub": "Linear e plano", "dias": ["d27"], "pontos": [
                P("Av. 18 de Julio, Plaza Cagancha e Centro de Fotografía", "18 de Julio 885",
                  "Avenida livre; centro de fotografia n/c", "Grátis", "Da Plaza Independencia à feira, cerca de 1,7 km"),
                P("Mirador Panorámico", "Soriano 1372, 22º andar", "Todos os dias 11h–19h (2026)",
                  "Grátis, com ingresso QR online", "Fecha com alerta laranja ou vermelho de tempo",
                  link="https://montevideo.gub.uy/noticias/nuevo-horario-del-mirador-panoramico",
                  mapa="Mirador Panorámico Intendencia de Montevideo"),
                P("Feria de Tristán Narvaja", "Cordón", "Só aos domingos, das 9h até cerca das 14h–16h", "Grátis",
                  "Brechó, antiguidades e frutas; voltada a moradores (TripAdvisor 3,6); chegar cedo",
                  link="https://montevideo.gub.uy/areas-tematicas/cultura-y-tiempo-libre/feria-de-tristan-narvaja"),
            ]},
            {"letra": "D", "nome": "Aguada", "sub": "Uber de 10 min, 2,5 a 3 km do centro", "dias": ["d28"], "pontos": [
                P("Palacio Legislativo", "Av. de las Leyes",
                  "Visita guiada seg–sex às 11h e 16h (2026); no verão passado foi 11h30 e 15h, confirmar",
                  "US$ 3 ou UYU 140, só em dinheiro", "30 a 45 min, sem agendamento; elevador para cadeira de rodas",
                  link="https://www.descubrimontevideo.uy/palacio-legislativo"),
                P("Mercado Agrícola (MAM)", "José L. Terra 2220", "Todos os dias 9h–22h; gastronomia 11h–23h", "Grátis",
                  "A cerca de 10 min a pé do Legislativo", link="https://www.mam.com.uy/",
                  mapa="Mercado Agrícola de Montevideo"),
            ]},
            {"letra": "E", "nome": "Orla: Parque Rodó, Punta Carretas e Pocitos", "sub": "Uber de 10 min, cerca de 3 km do centro",
             "dias": ["d26", "d28"], "pontos": [
                P("Parque Rodó e MNAV", "Julio Herrera y Reissig esq. Tomás Giribaldi",
                  "MNAV ter–dom 13h–20h (outra fonte diz 14h–19h); segunda fechado", "Grátis", "Parque plano",
                  mapa="Museo Nacional de Artes Visuales, Montevideo"),
                P("Rambla e letreiro “Montevideo”", "Plaza Gomensoro, Pocitos", "Livre", "Grátis",
                  "22 km contínuos; de Punta Carretas a Pocitos, cerca de 2,5 a 3 km (40 min a pé)",
                  mapa="Letras de Montevideo, Plaza Gomensoro"),
                P("Faro de Punta Carretas", "", "Horário n/c; há relato de pausa por volta das 13h", "Menos de US$ 1",
                  "Escada interna estreita", mapa="Faro de Punta Carretas, Montevideo"),
                P("Punta Carretas Shopping", "José Ellauri 350", "Todos os dias até 21h; sex e sáb até 22h", "Grátis",
                  "Antigo presídio"),
            ]},
        ],
        "fora": ("Ficaram de fora por baixa prioridade: o Cerro e a Fortaleza General Artigas (7 a 8 km, colina de 134 m "
                 "e horário incerto) e a Casa Garibaldi, que a Dirección Nacional de Cultura lista como fechada ao "
                 "público em janeiro de 2026."),
    },
    "ba": {
        "nome": "Buenos Aires",
        "saudacao": "¡Hola, che!",
        "foto": "obelisco",
        "legenda": "Obelisco ao pôr do sol",
        "pais": "Argentina",
        "sigla": "AR",
        "noites": "4 noites · 29/12 a 01/01",
        "moeda": "ARS · R$ 1 ≈ ARS 277 a 300",
        "cidade_mapa": "Buenos Aires",
        "intro": ("Buenos Aires funciona melhor em bairros: dentro de cada um dá para ir a pé, e o subte ou o Uber liga "
                  "um ao outro. Os horários de 31/12 e 01/01 seguem o padrão de 2024/25 da Prefeitura, porque o "
                  "comunicado de 2026 ainda não saiu."),
        "blocos": [
            {"letra": "A", "nome": "Plaza de Mayo e Av. de Mayo",
             "sub": "Plano; da Plaza ao Tortoni 5 min, ao Barolo cerca de 15 min, ao Congreso 25 a 30 min",
             "dias": ["d29", "d31", "d01"], "pontos": [
                P("Plaza de Mayo, Casa Rosada e Pirámide", "Balcarce 50", "Livre", "Grátis",
                  "30 min; visitas individuais ao palácio suspensas, segundo fonte secundária", mapa="Plaza de Mayo, Buenos Aires"),
                P("Museo Casa Rosada", "Av. Paseo Colón 100", "Qua–dom 11h–18h (entrada até 17h30); fecha seg e ter",
                  "Grátis", "Rampas e elevadores",
                  link="https://www.argentina.gob.ar/secretariageneral/museo-casa-rosada/horarios-e-informacion"),
                P("Catedral Metropolitana", "Rivadavia esq. San Martín", "Seg–sex 7h30–18h30, sáb–dom 9h–18h45 (n/c)",
                  "Grátis", "Túmulo de San Martín; 30 min", mapa="Catedral Metropolitana de Buenos Aires"),
                P("Cabildo", "Bolívar 65", "n/c; as fontes divergem", "n/c", "45 min",
                  mapa="Cabildo de Buenos Aires, Bolívar 65"),
                P("Manzana de las Luces", "Perú 272", "Visita guiada grátis qua–sex às 15h15, por ordem de chegada", "Grátis",
                  "Túneis só sáb e dom, com horário online"),
                P("Café Tortoni", "Av. de Mayo 825", "Todos os dias 8h–21h; 31/12 e 01/01 n/c", "Consumação",
                  "Chocolate com churros"),
                P("Palacio Barolo", "Av. de Mayo 1370", "Visitas seg e qua–dom, inclusive feriados; fecha terça",
                  "ARS 54.000 para não residentes (≈ R$ 184)", "Cerca de 1h30 em espanhol e inglês; 8 andares de escada; reserva online",
                  link="https://palaciobarolotours.com.ar/visitas-guiadas-diurnas/"),
                P("Congreso", "Rivadavia 1864",
                  "Visita guiada gratuita com reserva online (vagas abrem 5 a 10 dias antes); suspensa em dia de sessão", "Grátis",
                  "Cerca de 60 min, sem português; levar passaporte", mapa="Congreso de la Nación Argentina"),
            ]},
            {"letra": "B", "nome": "Teatro Colón e Obelisco",
             "sub": "Cerca de 10 min a pé entre eles; do bloco A, subte D ou Uber de 10 min", "dias": ["d02"], "pontos": [
                P("Teatro Colón", "Bilheteria na Tucumán 1171",
                  "Tour diário 10h–16h45, a cada 15 min; em português às 11h45 e 16h; fecha 24, 25 e 31/12 e 01/01",
                  "ARS 34.000 para estrangeiros", "50 min; elevador",
                  link="https://www.teatrocolon.org.ar/es/visitas-guiadas", mapa="Teatro Colón, Buenos Aires"),
                P("Obelisco e Av. Corrientes", "", "Livre", "Grátis",
                  "Teatros e livrarias; a Corrientes só abre depois do meio-dia em feriado",
                  mapa="Obelisco de Buenos Aires"),
            ]},
            {"letra": "C", "nome": "Recoleta e Retiro", "sub": "Compacto, cerca de 1,5 km de ponta a ponta",
             "dias": ["d30", "d01"], "pontos": [
                P("Cementerio de la Recoleta", "Junín 1760",
                  "Todos os dias 9h–17h; visita guiada gratuita em espanhol seg–sex 10h–16h; em 31/12 e 01/01 "
                  "provavelmente fechado ao turismo (n/c)",
                  "ARS 25.370 para estrangeiros (EntradasBA, set/2026); na porta, só cartão", "1 a 1h30"),
                P("Centro Cultural Recoleta", "Junín 1930", "Ter–sex 12h30–21h; sáb, dom e feriados 10h15–21h", "Grátis",
                  "Colado ao cemitério"),
                P("Floralis Genérica", "Plaza Naciones Unidas", "Livre", "Grátis", "7 a 10 min do cemitério",
                  mapa="Floralis Genérica, Buenos Aires"),
                P("Museo Nacional de Bellas Artes", "Av. del Libertador 1473",
                  "Ter–sex 11h–20h, sáb–dom 10h–20h; segunda fechado", "Grátis", "1 a 2 h",
                  link="https://www.argentina.gob.ar/cultura/mnba"),
                P("El Ateneo Grand Splendid", "Av. Santa Fe 1860",
                  "Seg–qui 9h–22h, sex–sáb 9h–24h, dom 12h–22h; 31/12 e 01/01 n/c", "Grátis",
                  "Livraria em antigo teatro; cerca de 15 min a pé"),
                P("Feria de Artesanos da Plaza Francia", "", "Sáb, dom e feriados 11h–20h; em 01/01 n/c", "Grátis",
                  "Provavelmente aberta em 02/01", mapa="Feria de Plaza Francia, Recoleta, Buenos Aires"),
            ]},
            {"letra": "D", "nome": "Palermo", "sub": "Da Recoleta, Uber de 8 min ou subte D; do MNBA ao MALBA, 20 a 25 min a pé",
             "dias": ["d30", "d01"], "pontos": [
                P("MALBA", "Av. Figueroa Alcorta 3415",
                  "Seg e qui–dom 12h–20h; qua 11h–20h com metade do preço; ter fechado; fecha 01/01 e, em 24 e 31/12, às 18h",
                  "ARS 14.000 (site)", "1h30 a 2h", link="https://www.malba.org.ar/en/visitar"),
                P("Museo Evita", "Lafinur 2988", "Ter–dom 11h–19h; fecha 24, 25 e 31/12 e 01/01", "ARS 17.000 para estrangeiros (≈ R$ 58)",
                  "Audioguia em português; cerca de 12 min a pé do MALBA"),
                P("Bosques de Palermo e Rosedal", "", "Abertos, sem entrada", "Grátis", "Abertos também em 01/01",
                  mapa="Rosedal de Palermo, Buenos Aires"),
                P("Jardín Japonés", "Av. Casares 3500", "Todos os dias 10h–18h45; 31/12 e 01/01 n/c", "ARS 24.000 para não residentes (≈ R$ 82)",
                  "Ingresso só na bilheteria; não fecha com chuva",
                  mapa="Jardín Japonés, Buenos Aires"),
                P("Palermo Soho e Hollywood", "Plaza Serrano, Honduras, Gorriti",
                  "Restaurantes e bares abertos à noite; comércio fecha em 01/01", "Grátis",
                  "15 a 20 min a pé da Plaza Italia", mapa="Plaza Serrano, Palermo Soho, Buenos Aires"),
            ]},
            {"letra": "E", "nome": "Puerto Madero", "sub": "Plano; da Plaza de Mayo à Puente de la Mujer, cerca de 1,1 km",
             "dias": ["d29", "d31"], "pontos": [
                P("Puente de la Mujer e diques", "Dique 3", "Livre", "Grátis", "Ponto informal dos fogos do Réveillon",
                  mapa="Puente de la Mujer, Buenos Aires"),
                P("Fragata Sarmiento", "Av. Alicia Moreau de Justo 980",
                  "Qui–sex 13h–19h; sáb, dom e feriados 12h–19h; fecha seg e ter", "ARS 1.000, só em dinheiro",
                  "Muitos degraus; 31/12 e 01/01 n/c; fecha com chuva",
                  link="https://www.argentina.gob.ar/armada/museos/buque-presidente-sarmiento"),
                P("Reserva Ecológica Costanera Sur", "",
                  "Ter–dom 9h–18h (última entrada 17h15); provavelmente fechada em 31/12 e 01/01", "Grátis",
                  "2 a 3 h; trilhas de terra", mapa="Reserva Ecológica Costanera Sur"),
            ]},
            {"letra": "F", "nome": "San Telmo", "sub": "Paralelepípedos; da Plaza de Mayo à Plaza Dorrego, cerca de 1,3 km",
             "dias": ["d31"], "pontos": [
                P("Plaza Dorrego e Calle Defensa", "", "Livre", "Grátis",
                  "A Feria de San Telmo é só aos domingos, 10h–17h, e não cai na viagem",
                  link="https://www.feriadesantelmo.com", mapa="Plaza Dorrego, San Telmo, Buenos Aires"),
                P("Mercado de San Telmo", "Bolívar 970",
                  "Seg–sex 10h–21h, sáb até 22h, dom até 20h; em 01/01 o comércio costuma fechar", "Grátis",
                  "Antiguidades, mate e comida"),
                P("Museo Histórico Nacional", "Defensa 1600, Parque Lezama", "n/c", "n/c", "Fica no fim da Defensa"),
            ]},
            {"letra": "G", "nome": "La Boca", "sub": "Só de Uber", "dias": ["d31"], "pontos": [
                P("Caminito", "La Boca", "De dia; lojas fecham por volta das 17h–18h", "Grátis",
                  "Cerca de 150 m; 1 a 2 h. Evitem dias de jogo do Boca e não venham a pé de San Telmo ou Puerto "
                  "Madero: o caminho é deserto e La Boca é onde há mais furtos.", mapa="Caminito, La Boca, Buenos Aires"),
            ]},
        ],
        "extras": [
            {"nome": "Salón 1923 (rooftop do Palacio Barolo)", "onde": "Av. de Mayo 1370, 16º andar", "quando": "Sex 01/01, 19h",
             "info": "Quarta a segunda (fecha terça). Coquetéis qua 18h30, 20h e 21h30; tapeo qui a seg 19h e 21h; lanche sex a "
                     "seg 17h. Reserva obrigatória e paga antecipado. Preço da sessão n/c; abertura em 01/01 n/c.",
             "link": "https://salon1923.com/", "whatsapp": "+54 9 11 3779-8847"},
            {"nome": "Ecoparque", "onde": "Av. Sarmiento 2601, Palermo", "quando": "Sex 01/01, 14h",
             "info": "ARS 22.650 por estrangeiro desde junho/2026; ingresso por data no site. Terça a domingo e feriados, 11h–17h30; fecha com chuva.",
             "link": "https://ecoparque.buenosaires.gob.ar/ticketera/elegir/ecoparque-entrada-general"},
            {"nome": "Museo Nacional de Arte Decorativo (Palacio Errázuriz)", "onde": "Av. del Libertador 1902, Palermo",
             "quando": "Qua 30/12, 14h30 (opção)",
             "info": "Qua a dom, 13h–19h; grátis; visita guiada às 16h (dado de um guia de turismo; confirmar).",
             "link": "https://www.buenosaires123.com.ar/museos/museo-de-arte-decorativo.html"},
            {"nome": "Green Eat (cafeteria)", "onde": "Florida 102, Monserrat", "quando": "Ter 29/12 ou Qui 31/12 (opção)",
             "info": "Horário n/c.",
             "link": "https://www.tripadvisor.com/Restaurant_Review-g312741-d9837799-Reviews-Green_Eat-Buenos_Aires_Capital_Federal_District.html"},
            {"nome": "Barolo Gourmet (visita guiada com gastronomia)", "onde": "Palacio Barolo, Av. de Mayo 1370",
             "quando": "Opção ao Salón, qui e sex às 20h",
             "info": "Quinta e sexta, 18h30–21h: visita, 1 tapa e 1 drink no rooftop. ARS 88.000 para não residentes (≈ R$ 299).",
             "link": "https://palaciobarolotours.com.ar/barolo-gourmet/", "whatsapp": "+54 9 11 6915-2385"},
        ],
        "fora": ("Ficaram fora do roteiro a pé: Campanópolis (aldeia medieval em González Catán, na Grande Buenos "
                 "Aires), o Parque de la Costa (Tigre) e o sorvete gigante, cuja loja não foi identificada. Os dois "
                 "parques pedem carro ou trem e mais de meio dia."),
    },
}

# ---------------------------------------------------------------------------
# Onde comer
# cat: carnes, restaurantes, cafes, sorvetes, pizzas
# ---------------------------------------------------------------------------
def R(nome, cidade, cat, onde, destaque="", preco="", nota="", reserva="", dia="", mapa=None, link=None, whatsapp=None):
    return {"nome": nome, "cidade": cidade, "cat": cat, "onde": onde, "destaque": destaque, "preco": preco,
            "nota": nota, "reserva": reserva, "dia": dia, "mapa": mapa, "link": link, "whatsapp": whatsapp}


RESTAURANTES = [
    # Montevidéu — carnes
    R("La Pulpería", "mvd", "carnes", "Lagunillas 448, Punta Carretas",
      "Entraña, ojo de bife, vacío, provoleta, boniato al plomo", "Médio a alto", "TA 4,6",
      "Não aceita reserva (só fila); jantar só ter–sex, almoço sáb–dom; fecha segunda", "Almoço de dom 27/12 (opção)",
      link="https://lapulperia.com.uy"),
    R("Garcia Parrilla", "mvd", "carnes", "Guipuzcoa 331, Punta Carretas", "Baby beef", "Muito alto", "TA 4,3",
      "Aberta todos os dias, 9h–2h; reserva recomendada", "Seg 28/12"),
    R("El Palenque", "mvd", "carnes", "Mercado del Puerto (Pérez Castellano 1579)",
      "Asado de tira, colita de cuadril, achuras", "Médio a alto", "TA 4,0; muito turístico", "n/c", "Dom 27/12 (opção)"),
    R("Cabaña Verónica, La Chacra del Puerto e El Peregrino", "mvd", "carnes", "Mercado del Puerto",
      "Asado clássico; a Chacra é rápida e o Peregrino, mais aconchegante",
      "Prato de R$ 72 a 120; parrillada para dois de R$ 180 a 264 (Dicas do Uruguai, 2026)", "", "n/c",
      "Dom 27/12 (opção)", mapa="Mercado del Puerto, Montevideo"),
    R("La Perdiz", "mvd", "carnes", "Guipúzcoa 350, Punta Carretas", "Grelhados e milanesas", "Cerca de US$ 20 por prato", "TA 4,3",
      "Só por telefone", "Sáb 26/12", mapa="La Perdiz Restaurant, Guipúzcoa 350, Montevideo"),
    # Montevidéu — restaurantes e chivito
    R("Primuseum", "mvd", "restaurantes", "Ciudad Vieja", "Jantar com tango", "Muito alto", "TA 4,8"),
    R("Es Mercat", "mvd", "restaurantes", "Montevidéu", "Frutos do mar", "", "TA 4,5", mapa="Es Mercat Montevideo"),
    R("Estrecho", "mvd", "restaurantes", "Montevidéu", "", "", "TA 4,6", mapa="Estrecho restaurante Montevideo"),
    R("La Fonda", "mvd", "restaurantes", "Montevidéu", "", "", "TA 4,5", mapa="La Fonda restaurante Montevideo"),
    R("Chivitería Marcos", "mvd", "restaurantes", "Pocitos", "Chivito, o sanduíche nacional", "", "", "",
      "Sáb 26/12 (plano B)", mapa="Chivitería Marcos Pocitos Montevideo"),
    R("Bar Tinkal", "mvd", "restaurantes", "Emilio Frugoni 853", "Chivito"),
    # Montevidéu — cafés
    R("Café Brasilero", "mvd", "cafes", "Ituzaingó 1447", "Desde 1877", "Seg–sex 8h30–19h, sáb 10h–19h, domingo fechado",
      "", "", "Seg 28/12"),
    R("Baar Fun Fun", "mvd", "cafes", "Ciudadela 1229", "Desde 1895, com uvita e tango ao vivo", "Ticket artístico + consumo", "", "Formulário no site",
      "Só sáb 26/12 à noite (fecha dom e seg)"),
    R("El Facal", "mvd", "cafes", "18 de Julio esq. Yi", "Café clássico da avenida", "", "", "",
      "Dom 27/12, 17h", mapa="El Facal, 18 de Julio y Yi, Montevideo"),
    # Montevidéu — sorvetes
    R("Las Delicias", "mvd", "sorvetes", "21 de Setiembre 2729, Pocitos", "", "", "", "", "Sáb 26/12"),
    R("La Cigale", "mvd", "sorvetes", "Ciudad Vieja, 18 de Julio 1179 e Pocitos", "", "", "TA 4,1 a 4,2", "", "Dom 27/12",
      mapa="La Cigale, 18 de Julio 1179, Montevideo"),
    R("Piwo Helados", "mvd", "sorvetes", "Sarandí 340", "", "", "", "", "Seg 28/12"),
    R("Los Trovadores", "mvd", "sorvetes", "Gabriel Pereira 3202", "Muitos doces de leite", "", "", "",
      "Seg 28/12, sobremesa"),
    R("Heladería García", "mvd", "sorvetes", "Av. Millán 3229, Prado", "Clássica, desde 1942; fecha segunda; fica longe"),
    # Buenos Aires — carnes
    R("Don Julio", "ba", "carnes", "Guatemala 4699, Palermo", "3º no Latin America’s 50 Best 2025",
      "Bife de chorizo cerca de ARS 87 mil; ARS 250 a 500 mil para dois (mai/2026)", "",
      "Essencial, com semanas de antecedência (Meitre ou WhatsApp); fóruns antigos falam em 90 dias",
      "Qua 30/12 (opção)", whatsapp="+54 9 11 5311-5668", mapa="Don Julio parrilla, Guatemala 4699, Buenos Aires"),
    R("Fogón Asado", "ba", "carnes", "Uriarte 1423, Palermo Soho", "Menu degustação de 9 etapas",
      "USD 90 no almoço e USD 116 no jantar, pré-pagos, mais USD 40 de harmonização", "TA 4,9", "Essencial",
      "Qua 30/12 (opção)"),
    R("La Carnicería", "ba", "carnes", "Thames 2317, Palermo Soho", "25 lugares; recomendada pelo Michelin", "n/c", "",
      "Essencial", "Alternativa para 30/12"),
    R("El Preferido de Palermo", "ba", "carnes", "Borges 2108", "24º no LatAm 50 Best 2025; bodegón gourmet", "n/c", "",
      "Via Meitre"),
    R("La Brigada", "ba", "carnes", "Estados Unidos 465, San Telmo", "Clássica desde 1992", "n/c", "",
      "Recomendada; uma fonte diz que fecha às segundas", "Qui 31/12 (opção)"),
    R("La Cabrera", "ba", "carnes", "José A. Cabrera 5099, Palermo Soho", "Muito turística",
      "Happy hour 18h30–20h com 40% off (ago/2025)", "", "Recomendada", "Qua 30/12 (opção)"),
    R("Hierro", "ba", "carnes", "San Telmo e Palermo", "", "Médio a alto", "TA 4,9 e 4,8", "n/c",
      "Sex 01/01 (abriu 19h–1h em 2026)", mapa="Hierro parrilla Palermo Buenos Aires"),
    R("El Mercado (Faena) e Cabaña Las Lilas", "ba", "carnes", "Puerto Madero",
      "El Mercado é o 27º no LatAm 50 Best 2025", "Muito alto", "", "Recomendada", "Ter 29/12 (opção)",
      mapa="Cabaña Las Lilas, Puerto Madero, Buenos Aires"),
    R("El Desnivel", "ba", "carnes", "Defensa 855, San Telmo", "Opção barata", "n/c", "", "Sem reserva (fila)",
      "Qui 31/12 (opção)"),
    R("Santos Manjares", "ba", "carnes", "Paraguay 938, Retiro", "Opção barata", "n/c", "", "Sem reserva (fila)"),
    # Buenos Aires — pizzas
    R("Güerrín", "ba", "pizzas", "Av. Corrientes 1368", "Muzzarella", "ARS 29.900 a 39.500", "", "",
      "Ter 29/12 (opção)"),
    R("Las Cuartetas", "ba", "pizzas", "Corrientes 838", "Desde 1932", "Muzzarella cerca de ARS 27 mil"),
    R("El Cuartito", "ba", "pizzas", "Talcahuano 937", "Desde 1934, fugazzeta; fecha segunda"),
    R("Bar El Federal", "ba", "pizzas", "Carlos Calvo 599, San Telmo", "De 1864", "", "", "Sem reserva", "Qui 31/12"),
    # Buenos Aires — cafés e clássicos
    R("Café Tortoni", "ba", "cafes", "Av. de Mayo 825", "De 1858; chocolate quente com churros", "", "", "Pode ter fila",
      "Ter 29/12"),
    R("La Biela", "ba", "cafes", "Av. Quintana 596, Recoleta", "De 1942", "", "", "", "Qua 30/12"),
    R("Los Galgos", "ba", "cafes", "Callao 501", "Confeitaria de 1930", "", "", "", "Sáb 02/01"),
    R("La Pipeta", "ba", "cafes", "San Martín 498", "Desde 1961; entraña", "", "", "", "Sáb 02/01"),
    R("Green Eat", "ba", "cafes", "Florida 102, Monserrat", "Cafeteria citada em vídeo de viagem", "Horário n/c", "", "",
      "Ter 29/12 ou Qui 31/12 (opção)"),
    R("Williamsburg", "ba", "restaurantes", "Palermo", "Aberto em 01/01/2026, 12h–24h; confirmar em dezembro", "", "",
      "", "Sex 01/01", mapa="Williamsburg burger Palermo Buenos Aires"),
    # Buenos Aires — sorvetes
    R("Cadore", "ba", "sorvetes", "Av. Corrientes 1695",
      "Peçam dulce de leche granizado, pistache, sambayón e mousse de limão", "", "", "", "Ter 29/12 e Sáb 02/01"),
    R("Rapa Nui", "ba", "sorvetes", "Arenales 2302, Recoleta", "Chocolate 80% cacau", "", "", "", "Sex 01/01"),
    R("Un’Altra Volta", "ba", "sorvetes", "Av. Quintana 502; Defensa 973; Florida 706", "", "", "", "",
      "Qua 30/12 e Qui 31/12", mapa="Un'Altra Volta, Defensa 973, Buenos Aires"),
    R("Persicco", "ba", "sorvetes", "Av. Quintana 595", "", "", "", "", "Qua 30/12"),
    R("Freddo", "ba", "sorvetes", "Várias unidades", "Dulce de leche", mapa="Freddo helados Buenos Aires"),
    R("Tufic", "ba", "sorvetes", "Guatemala 4597, Palermo", "", "", "TA 4,5", "", "Qua 30/12 à noite"),
]

CATEGORIAS = [
    ("carnes", "Carnes"),
    ("restaurantes", "Restaurantes"),
    ("cafes", "Cafés e clássicos"),
    ("pizzas", "Pizzas"),
    ("sorvetes", "Sorvetes"),
]

DICAS_COMIDA = [
    ("mvd", "No Mercado del Puerto, vão por volta de 12h–15h e peçam chivito ou “medio y medio”. Ele fecha por volta das 17h."),
    ("mvd", "Não há ranking recente confiável de sorveterias em Montevidéu; as do roteiro foram escolhidas pela localização."),
    ("ba", "As melhores carnes de Buenos Aires exigem reserva com semanas de antecedência."),
    ("ba", "Os horários de fim de ano de Mercado del Puerto, Café Brasilero, La Pulpería, Café Tortoni, Don Julio e La Brigada ainda precisam ser confirmados."),
]

# ---------------------------------------------------------------------------
# Compras
# ---------------------------------------------------------------------------
COMPRAS = {
    "ba": [
        ("Roupas de marcas argentinas", "Palermo Soho",
         "Ruas Honduras, Armenia e Gurruchaga e Plaza Serrano; cabe na noite de 30/12",
         "Preço alto; marcas como Jazmín Chebar, María Cher, Prune e Kevingston; Subte D"),
        ("Couro e custo-benefício", "Calle Murillo, Villa Crespo (números 500 a 900)",
         "Melhor de qua a sex pela manhã, evitando sábado; fecha domingo; cabe na manhã de 31/12 no lugar de La Boca",
         "Lojas citadas: Logia Lautaro, Catriel Cueros, Tríptico; desconto de 15 a 20% em dinheiro; Subte B"),
        ("Outlet", "Distrito Arcos (Paraguay 4979, Palermo)", "10h–21h todos os dias (em 01/01 n/c); cerca de 60 lojas",
         "Não garante preço menor; outra fonte lista o endereço Juan B. Justo 4700"),
        ("Shoppings", "Galerías Pacífico (Florida esq. Córdoba) e Alto Palermo (Av. Santa Fe 3253)",
         "Horários divergem entre fontes; fecham em 01/01", "Recoleta Mall e Patio Bullrich são mais caros"),
        ("Mate e bombilla", "El Viejo Almacén del Mate (Defensa 963, San Telmo) e TodoMates (Thames 1861, Palermo Soho)",
         "San Telmo cabe na tarde de 31/12", "TodoMates tem mais de 500 modelos e gravação; horários n/c"),
        ("Facas de churrasco", "Parrillerisimos Argentina (Av. Corrientes 1382, local 7)", "Horário n/c",
         "Facas artesanais e de aço damasco; vão na mala despachada"),
        ("Alfajores e doce de leite", "Havanna (várias lojas na Calle Florida), Cachafaz e Entre Dos; doce de leite Chimbote e Poncho Negro",
         "Supermercados também vendem", "Levem em bagagem despachada"),
        ("Vinho", "Lo de Joaquín Alberdi (Palermo Soho), Grand Cru (Recoleta e Palermo) e Winery (Microcentro)",
         "Para Malbec barato, supermercados como Coto, Carrefour e Disco", "Endereços exatos n/c"),
        ("Artesanato", "Feria de Plaza Francia (Recoleta)", "Sáb, dom e feriados, 11h–20h; provavelmente aberta em 02/01",
         "Em 01/01 n/c"),
    ],
    "mvd": [
        ("Lã e malharia", "Manos del Uruguay (cooperativa)",
         "Peatonal Sarandí, Punta Carretas Shopping (loja 252) e Montevideo Shopping (loja 114); horários n/c",
         "Bom para presente"),
        ("Roupas e couro", "Punta Carretas Shopping (José Ellauri 350) e Av. 18 de Julio",
         "Shopping até 21h; 18 de Julio, seg–sáb 9h–19h; Sarandí fecha domingo",
         "Jaqueta de couro de R$ 1.120 a 2.520 (Dicas do Uruguai, set/2026)"),
        ("Mate, cuia e térmica", "Tu Mate (Carlos Roxlo 1327, Cordón) e Mates Poco Sitio (Río Negro 1325, Centro)",
         "Ta-Ta (supermercado) também vende mates e térmicas", "Preços n/c"),
        ("Artesanato", "Mercado de los Artesanos (Plaza Cagancha 1365 e Piedras 258)",
         "Seg–sáb 11h–19h; a unidade da Piedras tem horário “até outubro”", "Couro, mates e cerâmica"),
        ("Alfajores", "Alfajores del Uruguay (Pérez Castellano 1600, junto ao Mercado del Puerto); marcas Punta Ballena, Portezuelo e Marley",
         "Seg–sex 9h–19h; sáb e dom 10h–18h", "Cabe no dia 27/12"),
        ("Doce de leite e vinho", "Conaprole, Los Nietitos e La Pataia; Tannat de Garzón, Bouza e Pisano",
         "Mercado Agrícola (MAM) tem doce artesanal, queijo e vinho", "Tannat de R$ 49 a 84 (Dicas do Uruguai)"),
        ("Ágata e ametista", "Ideas Creativa (San José 1319)", "Horário n/c", "Fonte única"),
        ("Feira", "Feria de Tristán Narvaja", "Domingo 27/12, das 9h até cerca das 14h–16h",
         "Mais brechó e antiguidade do que lembrancinha; TA 3,6"),
    ],
}

COMPRAS_INTRO = ("A Argentina segue mais barata para comida, couro, vinho e doces; o Uruguai é descrito como caro até "
                 "para roupa (IVA básico de 22%). Marcas importadas já não compensam na Argentina. Os “melhores” vêm "
                 "do cruzamento de blogs e guias recentes; não há ranking oficial.")

IMPOSTOS = [
    ("Tax free argentino",
     "Desde 2026 o sistema é digital (Resolução Geral ARCA 5843/2026). Devolve o IVA de 21% da fatura menos a comissão "
     "da operadora, só para bens de fabricação argentina, em lojas aderidas, com fatura B e documento estrangeiro "
     "(passaporte). Ficam de fora hospedagem, gastronomia, passeios e passagens. A validação é em terminais de "
     "autogestão em Ezeiza, Aeroparque e Buquebus. O valor mínimo aparece como “70”, sem moeda confirmada (n/c)."),
    ("IVA no Uruguai",
     "Hospedagem registrada no MINTUR tem IVA zero o ano todo para não residentes com cartão estrangeiro. Em "
     "restaurantes e bares o benefício valeu até 30/04/2026, e a Uruguay XXI informou em 21/09/2026 a ampliação para "
     "o verão de 2027, sem datas exatas; confirmem se cobre 26 a 29/12. Paguem com cartão brasileiro, não com dinheiro. "
     "Compras em lojas não entram nesse benefício."),
    ("Tax free uruguaio",
     "Devolve 80% do IVA (22%) em lojas aderidas (Global Blue), com passaporte: roupas, couro, malharia, alimentos, "
     "bebidas e artesanato. Mínimo por fatura de 500 ou 600 UYU (fontes divergem); uma fonte cita comissão de 20 a 40%. "
     "A restituição é feita no aeroporto de Carrasco. Como o grupo sai do Uruguai de ferry, confirmem se o porto de "
     "Montevidéu faz a validação; caso contrário, o tax free uruguaio não serve."),
    ("Alfândega no Brasil",
     "Uma fonte de fevereiro de 2026 cita cota de US$ 1.000 por via aérea e 12 litros de bebida alcoólica; outra fala "
     "em 5 litros ou 6 garrafas. Reconfirmem na Receita Federal."),
]

# ---------------------------------------------------------------------------
# Travessia e Réveillon
# ---------------------------------------------------------------------------
TRAVESSIA_INTRO = ("A travessia é feita por ferry, em duas empresas; não há serviço regular de iate ou catamarã de luxo "
                   "entre as duas capitais. Os horários de dezembro ainda não foram publicados e a alta temporada "
                   "esgota: comprem as seis passagens juntas em outubro ou novembro.")

TRAVESSIA = [
    {"nome": "Buquebus direta", "detalhe": "Navio Francisco", "duracao": "2h15 a 2h30", "preco": "UYU 3.222 a 6.496 (≈ R$ 420 a 845)",
     "texto": "Sai do porto de Montevidéu (Rambla 25 de Agosto de 1825) e chega a Puerto Madero (Av. Antártida "
              "Argentina 821). Em 29/12: saídas às 11h (chega 13h45) e 20h (chega 22h45).",
     "no_roteiro": True, "link": "https://www.buquebus.com"},
    {"nome": "Buquebus via Colonia", "detalhe": "Ônibus e navio", "duracao": "Cerca de 4h30", "preco": "UYU 2.580 a 2.969 (≈ R$ 335 a 386)",
     "texto": "Em 29/12: UYU 2.580 a 2.969 por pessoa (site oficial, consulta de 29/09/2026).", "link": "https://www.buquebus.com"},
    {"nome": "Colonia Express", "detalhe": "Ônibus e ferry via Colonia", "duracao": "Cerca de 4h45", "preco": "UYU 3.676 a 4.251 (≈ R$ 478 a 553)",
     "texto": "Ônibus do Terminal Tres Cruces; chegada em Puerto Madero Sur (Av. Elvira Rawson de Dellepiane 155). "
              "Em 29/12: saídas às 6h (chega 10h45) e 14h30 (chega 19h15).",
     "link": "https://www.coloniaexpress.com/uy/Horarios"},
]

TRAVESSIA_NOTAS = [
    "Preços dos sites oficiais para 29/12/2026, consultados em 29/09/2026; são dinâmicos e sobem perto da data.",
    "Comprem só nos sites oficiais (buquebus.com e coloniaexpress.com).",
    "Cheguem ao terminal de 1h30 a 2h antes; a imigração é feita ali, e a taxa migratória uruguaia (cerca de USD 2,10) já vem no bilhete.",
    "Bagagem citada: 20 kg despachados na Buquebus e 30 kg na Colonia Express (agregador; n/c nos sites oficiais).",
]

REVEILLON_INTRO = ("O Réveillon portenho é uma ceia de menu fixo, paga antes, com reserva por WhatsApp, e-mail ou "
                   "Meitre. Os valores abaixo são de 2025; os de 2026 ainda não saíram e devem subir. Com R$ 1 = ARS "
                   "294, ARS 200 a 290 mil equivalem a R$ 680 a 990 por pessoa.")

REVEILLON = [
    {"letra": "A", "nome": "Puerto Madero",
     "lugar": "Cabaña Las Lilas (ARS 240 a 275 mil, com DJ) ou Villegas Resto & Grill (ARS 250 a 290 mil, 5 etapas, até 4h)",
     "preco": "Cerca de R$ 820 a 990", "obs": "Mais perto do ponto informal dos fogos; a pé do hotel, se ficarem por ali"},
    {"letra": "B", "nome": "Palermo, para quem quer carne",
     "lugar": "La Carnicería (ARS 200 mil; pequena, reservar cedo) ou Lo de Jesús (ARS 150 mil)",
     "preco": "Cerca de R$ 510 a 680", "obs": "Volta de Uber, com tarifa alta"},
    {"letra": "C", "nome": "Costanera Norte, com festa", "lugar": "Enero (Av. Rafael Obligado 7180)",
     "preco": "US$ 150, com open bar e DJ (≈ R$ 825)", "obs": "Música ao vivo, DJ, fogos e estacionamento em 2025"},
]

REVEILLON_NOTAS = [
    ("Fogos", "Não há show oficial confirmado. Em 2025/26 o ponto informal foi a Puente de la Mujer, em Puerto Madero, "
              "com fogos privados apesar da proibição de pirotecnia com som, em vigor desde 19/12/2025 (fogos "
              "silenciosos são permitidos). A situação para 2026/27 não está confirmada."),
    ("Meia-noite", "O último subte costuma sair entre 21h e 23h30, os ônibus reduzem e táxi e aplicativo ficam raros e "
                   "caros. Jantem e fiquem em Puerto Madero, ou reservem antes um transfer de volta. Bancos fecham em "
                   "31/12 e supermercados por volta das 18h; em 01/01 quase tudo fica fechado."),
]

# ---------------------------------------------------------------------------
# Antes de embarcar
# ---------------------------------------------------------------------------
ANTES_INTRO = ("Levem passaporte válido: ele resolve a entrada nos dois países e é o documento citado nos tax free. "
               "Cotações e regras são de 28 e 29/09/2026 e mudam até dezembro.")

ANTES = [
    ("Documentos", "Passaporte válido ou RG físico original, com menos de 10 anos de emissão, em bom estado e com foto "
                   "atual. CNH e documento digital não valem. A CIN entrou no acordo do Mercosul em maio/2026, mas a "
                   "aceitação prática nas fronteiras não está confirmada."),
    ("Seguro-saúde", "O Uruguai não exige. Na Argentina, um decreto de 2025 prevê seguro para não residentes, mas falta "
                     "regulamentação. Contratem seguro-viagem com cobertura médica e levem a apólice em espanhol ou inglês."),
    ("Câmbio na Argentina", "Dólar oficial a ARS 1.545 em 28/09/2026; o blue fica cerca de 1% acima, então câmbio de rua "
                            "não compensa e traz risco de nota falsa. R$ 1 vale entre ARS 277 e 300, conforme a fonte."),
    ("Pagamento na Argentina", "Cartão internacional (conta global como Wise ou Nomad), sempre em pesos, recusando a "
                               "conversão em reais na maquininha. IOF de 3,5% em cartão e espécie. O Pix só funciona em "
                               "comércios credenciados, com IOF de 3,5% e spread de 2 a 3%. Gorjeta de 10%, de "
                               "preferência em dinheiro; o “cubierto” é uma taxa de mesa à parte."),
    ("Pagamento no Uruguai", "1 UYU vale cerca de R$ 0,13. Cartão é aceito em quase tudo; dinheiro serve para táxi e "
                             "pequenos comércios. Gorjeta de 10%, voluntária; confiram o cubierto."),
    ("Clima", "Buenos Aires: máxima de 27 a 28 °C, mínima de 19 a 21 °C, cerca de 10 dias de chuva por mês e muita "
              "umidade. Montevidéu: 26 a 27 °C e 17 a 18 °C, cerca de 8 dias de chuva e vento de 19 km/h. Levem roupa "
              "leve, casaco fino para a Rambla e o barco, capa de chuva, protetor solar e chapéu."),
    ("Transporte local", "Uber, DiDi e Cabify funcionam nas duas cidades. Em Buenos Aires, uma decisão judicial de "
                         "maio/2026 exige licença profissional dos motoristas; o cenário de dezembro não está "
                         "confirmado. Cartão SUBE em Buenos Aires (subte a ARS 1.753 e ônibus a partir de ARS 888, em "
                         "set/2026) e STM em Montevidéu. Para seis pessoas, dois carros."),
    ("Chip", "eSIM é o mais indicado; o roaming das operadoras brasileiras sai de 3 a 4 vezes mais caro."),
    ("Aeroportos", "Carrasco (Montevidéu): 20 km, 25 a 40 min; Uber ou Cabify de R$ 180 a 220, táxi oficial de R$ 280 "
                   "a 350, ônibus COT até Tres Cruces de R$ 35 a 40. Ezeiza: 30 km, 40 a 70 min; Uber de ARS 30 a 40 "
                   "mil e transfer privado de USD 27 a 38 por carro de até 3 pessoas. Aeroparque: 5 a 7 km, 10 a 25 min."),
]

# Cotações de referência para o conversor (editáveis no próprio site)
CAMBIO = {"brl_por_uyu": 0.13, "ars_por_brl": 294}

# ---------------------------------------------------------------------------
# Acessibilidade e segurança
# ---------------------------------------------------------------------------
DESLOCAMENTOS = ("O roteiro usa Uber em cerca de dez trechos curtos (8 a 15 min), além dos traslados de aeroporto e "
                 "da travessia; todo o resto é a pé.")

ACESSIBILIDADE = [
    ("Bons para andar", "Em Montevidéu, Centro e 18 de Julio, Rambla, Parque Rodó e MAM; em Buenos Aires, Plaza de "
                        "Mayo, Av. de Mayo, Puerto Madero, as praças da Recoleta e os Bosques de Palermo. A Ciudad "
                        "Vieja é plana, mas tem calçadas antigas, estreitas e com meios-fios altos."),
    ("Rampa ou elevador", "Torres García, Gurvich, Carnaval e Gaucho (Montevidéu); Legislativo (elevador, com algumas "
                          "escadas); Museo Casa Rosada (rampas e elevadores) e Teatro Colón (elevador). A Prefeitura de "
                          "Buenos Aires tem cinco circuitos acessíveis, entre eles centro histórico, Recoleta e Puerto Madero."),
    ("Com escadas ou desníveis", "Cabildo de Montevidéu (só o 1º andar), Faro de Punta Carretas, Palacio Barolo (o "
                                 "Salón 1923 exige elevador até o 14º andar e mais dois lances de escada), Fragata "
                                 "Sarmiento, trilhas de terra da Reserva Ecológica e os paralelepípedos de San Telmo."),
    ("Calçadas de Buenos Aires", "Estreitas e cheias, com rampas às vezes bloqueadas por carros e pisos irregulares e "
                                 "escuros à noite."),
]

SEGURANCA = [
    ("Buenos Aires", "O risco principal é furto de celular e carteira, por batedor ou “motochorro”. Não andem com o "
                     "celular na mão, principalmente na Calle Florida e perto das estações Retiro, Constitución e Once. "
                     "Recoleta e Palermo são mais seguros."),
    ("Evitem", "La Boca fora do trecho turístico e depois do fim da tarde, e o Centro depois das 22h. Prefiram Uber a "
               "táxi de rua e nunca troquem dinheiro na rua (troco falso). Há uma delegacia do turista na Av. Corrientes."),
    ("Montevidéu", "Pocitos e Punta Carretas são tranquilos à noite; a Ciudad Vieja esvazia à noite. O risco é furto de "
                   "oportunidade, então guardem celular e bolsa."),
]

# ---------------------------------------------------------------------------
# Pendências
# ---------------------------------------------------------------------------
ATENCAO = [
    ("Pacote com “super iate”", "O pacote da Viagens Fit, se for ele que estiverem considerando, vale de novembro/2026 "
                                "a novembro/2027 exceto Natal, Réveillon e Carnaval. Esta viagem passa pelo Réveillon. "
                                "Confirmem por escrito as datas e o que está incluído antes de pagar."),
    ("Tax free uruguaio", "É reembolsado no aeroporto de Carrasco. Como o grupo sai do Uruguai de ferry, confirmem se o "
                          "porto de Montevidéu valida o reembolso."),
    ("Horários de 31/12 e 01/01", "Ainda não divulgados: Cementerio de la Recoleta, Feria de Plaza Francia, Cabildo, "
                                  "Manzana de las Luces, Jardín Japonés, Salón 1923 e Palacio Barolo (sessões de "
                                  "01/01), Ecoparque, Museo Nacional de Arte Decorativo, Green Eat, Fragata Sarmiento, "
                                  "Museo del Carnaval, Palacio Legislativo e o comunicado da Prefeitura de Buenos Aires."),
]

CHECKLIST = [
    ("travessia", "Comprar as seis passagens da travessia de 29/12 (Buquebus ou Colonia Express)", "Outubro ou novembro"),
    ("jantar30", "Reservar Don Julio, Fogón Asado ou La Cabrera para a noite de 30/12 (La Carnicería é a alternativa)",
     "As vagas somem com semanas de antecedência"),
    ("mvd", "Reservar La Perdiz (26/12) e Garcia Parrilla (28/12) em Montevidéu", "La Pulpería (27/12) não aceita reserva"),
    ("reveillon", "Reservar o jantar de Réveillon (menu fixo e pré-pago)", "Puerto Madero, Palermo ou Costanera Norte"),
    ("seguro", "Contratar seguro-viagem com cobertura médica e conferir passaporte ou RG", ""),
    ("ingressos", "Reservar tour do Teatro Colón (02/01), Salón 1923 (01/01, 19h) e ingresso do Ecoparque (01/01)", ""),
    ("dezembro", "Em dezembro, reconferir todos os horários marcados como n/c", ""),
]

PERGUNTAS = [
    "Qual o horário de chegada em 26/12 e do voo de volta em 02/01, e de qual aeroporto? Isso decide o Colón e o Uber de Ezeiza.",
    "Onde ficarão hospedados? Sugestão: Centro/Ciudad Vieja ou Pocitos em Montevidéu; Recoleta/Retiro ou Puerto Madero em Buenos Aires. Puerto Madero facilita a noite de Réveillon.",
    "Há alguém com mobilidade reduzida ou restrição alimentar, e qual o orçamento por refeição?",
    "Querem trocar o ferry direto pela rota via Colonia del Sacramento?",
]

# ---------------------------------------------------------------------------
# Fontes (pesquisa de 29/09/2026)
# ---------------------------------------------------------------------------
FONTES = [
    ("Montevidéu", [
        ("Teatro Solís — horários", "https://www.teatrosolis.org.uy/categoria/Horarios-119"),
        ("Museo Torres García — visita", "https://www.torresgarcia.org.uy/visita.php"),
        ("Museo Gurvich — visitar", "https://museogurvich.org/visitar/"),
        ("Museo Andes 1972", "https://mandes.uy/en/"),
        ("Museos en verano — Dirección Nacional de Cultura", "http://www.museos.gub.uy/index.php/noticias/item/2541-museos-en-verano-la-direccion-nacional-de-cultura-informa-dias-y-horarios"),
        ("Mirador Panorámico — novo horário", "https://montevideo.gub.uy/noticias/nuevo-horario-del-mirador-panoramico"),
        ("Feria de Tristán Narvaja — Intendencia", "https://montevideo.gub.uy/areas-tematicas/cultura-y-tiempo-libre/feria-de-tristan-narvaja"),
        ("Mercado Agrícola (MAM)", "https://www.mam.com.uy/"),
        ("Palacio Legislativo — Descubrí Montevideo", "https://www.descubrimontevideo.uy/palacio-legislativo"),
        ("Cabildo — Descubrí Montevideo", "https://www.descubrimontevideo.uy/museo-historico-cabildo"),
        ("Museo del Gaucho — Descubrí Montevideo", "https://www.descubrimontevideo.uy/museo-del-gaucho-y-la-moneda"),
        ("Museo del Carnaval — Descubrí Montevideo", "https://www.descubrimontevideo.uy/museo-del-carnaval-0"),
        ("Palacio Salvo — Descubrí Montevideo", "https://www.descubrimontevideo.uy/palacio-salvo"),
        ("Mercado del Puerto — Liva Viagens", "https://blog.livareviagens.com.br/mercado-del-puerto-uruguai/"),
        ("Feriados 2026 no Uruguai", "https://elacontecer.com.uy/sociedad/feriados-2026-uruguay-calendario-completo/"),
        ("Roteiro de 3 dias em Montevidéu — Dicas do Uruguai", "https://dicasdouruguai.com.br/roteiros/roteiro-de-3-dias-em-montevideu/"),
    ]),
    ("Buenos Aires", [
        ("Teatro Colón — visitas guiadas", "https://www.teatrocolon.org.ar/es/visitas-guiadas"),
        ("MALBA — visitar", "https://www.malba.org.ar/en/visitar"),
        ("Museo Nacional de Bellas Artes", "https://www.argentina.gob.ar/cultura/mnba"),
        ("Museo Casa Rosada — horários", "https://www.argentina.gob.ar/secretariageneral/museo-casa-rosada/horarios-e-informacion"),
        ("Fragata Sarmiento", "https://www.argentina.gob.ar/armada/museos/buque-presidente-sarmiento"),
        ("Feria de San Telmo", "https://www.feriadesantelmo.com"),
        ("Palacio Barolo Tours", "https://palaciobarolotours.com.ar"),
        ("O que abre no Natal e no Ano-Novo — Baires Secreta", "https://www.bairessecreta.com/que-abre-navidad-ano-nuevo-buenos-aires"),
        ("Salón 1923 — sessões e reservas", "https://salon1923.com/en/"),
        ("Barolo Gourmet — Palacio Barolo Tours", "https://palaciobarolotours.com.ar/barolo-gourmet/"),
        ("Buenos Aires Eco-park — turismo.buenosaires.gob.ar", "https://turismo.buenosaires.gob.ar/en/otros-establecimientos/buenos-aires-eco-park"),
        ("Ecoparque: entradas, dias e horários — El Destape", "https://www.eldestapeweb.com/sociedad/actividades/ecoparque-de-buenos-aires-entradas-dias-horarios-y-como-llegar-202571815734"),
        ("Museo Nacional de Arte Decorativo — buenosaires123", "https://www.buenosaires123.com.ar/museos/museo-de-arte-decorativo.html"),
        ("Green Eat, Florida 102 — Tripadvisor", "https://www.tripadvisor.com/Restaurant_Review-g312741-d9837799-Reviews-Green_Eat-Buenos_Aires_Capital_Federal_District.html"),
    ]),
    ("Gastronomia e Réveillon", [
        ("Melhores parrillas de Montevidéu — Urubus", "https://urubus.com.uy/blog/mejores-parrillas-en-montevideo"),
        ("La Pulpería", "https://lapulperia.com.uy"),
        ("Mercado del Puerto — Dicas do Uruguai", "https://dicasdouruguai.com.br/montevideu/mercado-del-puerto-em-montevideu"),
        ("Melhores parrillas de Buenos Aires — Vidriera", "https://vidrierabuenosaires.com/blog/mejores-parrillas-buenos-aires"),
        ("Latin America’s 50 Best Restaurants", "https://www.the50.com"),
        ("Restaurantes abertos em 1º de janeiro — Ámbito", "https://www.ambito.com/lifestyle/que-restaurantes-abren-el-1-enero-n6226046"),
        ("Réveillon em Buenos Aires — Viaje Bonito", "https://viajeibonito.com.br/reveillon-em-buenos-aires"),
        ("Ano-Novo em Buenos Aires — Dicas Argentina", "https://dicasargentina.com/buenos-aires/ano-novo-em-buenos-aires"),
    ]),
    ("Compras, impostos, documentos e dinheiro", [
        ("Novo tax free argentino — El Cronista", "https://www.cronista.com/economia-politica/cambia-el-tax-free-en-argentina-las-modificaciones-que-introdujo-arca-para-la-devolucion-del-iva/"),
        ("Sistema digital de tax free — Panrotas", "https://www.panrotas.com.br/mercado/destinos/2026/05/argentina-lanca-sistema-digital-de-tax-free-para-agilizar-devolucao-do-iva-a-turistas_228402.html"),
        ("Tax free no Uruguai — Aduanas", "https://www.aduanas.gub.uy/innovaportal/v/10590/1/innova.front/guia_practica_sobre_aplicacion_de_regimen_tax_free_para_turistas.html"),
        ("IVA para turistas no verão de 2027 — Uruguay XXI", "https://www.uruguayxxi.gub.uy/es/noticias/articulo/uruguay-amplia-los-beneficios-para-quienes-visiten-el-pais-en-la-temporada-estival-de-2027/"),
        ("Compras em Montevidéu — Dicas do Uruguai", "https://dicasdouruguai.com.br/montevideu/compras-em-montevideu/"),
        ("Outlets em Buenos Aires — Dicas Argentina", "https://dicasargentina.com/buenos-aires/outlets-em-buenos-aires/"),
        ("Palermo Soho — Mi Buenos Aires Querido", "https://mibuenosairesquerido.com/guia/circuitos-de-compras/palermo-soho"),
        ("Argentina em 2026 está mais barata — Correio Braziliense", "https://www.correiobraziliense.com.br/aqui/2026/07/16/argentina-em-2026-viajar-para-o-pais-vizinho-esta-mais-barato/"),
        ("RG físico para o Mercosul — Polícia Científica de SC", "https://policiacientifica.sc.gov.br/2026/02/10/carteira-de-identidade-fisica-ainda-e-exigida-para-viagens-internacionais-em-paises-do-mercosul/"),
        ("Horários da Colonia Express", "https://www.coloniaexpress.com/uy/Horarios"),
        ("Colonia Express x Buquebus — Urubus", "https://urubus.com.uy/blog/diferencia-entre-colonia-express-y-buquebus/"),
        ("Pix na Argentina — Wise", "https://wise.com/br/blog/pix-argentina"),
        ("Câmbio em Buenos Aires — Um Viajante", "https://www.umviajante.com.br/cambio-buenos-aires-qual-moeda-levar-para-a-argentina-real-peso-dolar-ou-cartao"),
    ]),
]


# ---------------------------------------------------------------------------
# Cultura: o que se vê, se ouve e se come em cada cidade
# ---------------------------------------------------------------------------
CULTURA = {
    "mvd": [
        {"foto": "candombe", "cor": "vermelho", "tag": "Patrimônio da UNESCO", "titulo": "Candombe",
         "texto": "Tambores de origem africana que ecoam pelos bairros Sur e Palermo. O candombe é Patrimônio "
                  "Imaterial da Humanidade (UNESCO, 2009) e a alma do Carnaval uruguaio, o mais longo do mundo. "
                  "O Museo del Carnaval (27/12) conta essa história."},
        {"foto": "mate", "cor": "verde", "tag": "Hábito nacional", "titulo": "Mate na Rambla",
         "texto": "Uruguaios andam com a cuia na mão e a garrafa térmica debaixo do braço, até na praia. O país "
                  "está entre os maiores consumidores de erva-mate por pessoa do mundo. Cuia e térmica são a "
                  "lembrancinha mais uruguaia que existe."},
        {"foto": "salvo", "cor": "azul", "tag": "Música", "titulo": "Onde nasceu La Cumparsita",
         "texto": "O tango mais famoso do mundo estreou em 1917 na Confitería La Giralda, no terreno onde depois "
                  "ergueram o Palacio Salvo. O prédio tem um Museo del Tango e um mirante sobre a Plaza Independencia."},
        {"foto": "chivito", "cor": "laranja", "tag": "Comida de rua", "titulo": "Chivito",
         "texto": "O sanduíche nacional: bife macio, presunto, queijo, ovo, alface e tomate, quase sempre com "
                  "batata frita. Ótimo para a noite de chegada (Chivitería Marcos) ou no Mercado del Puerto."},
    ],
    "ba": [
        {"foto": "tango", "cor": "vermelho", "tag": "Patrimônio da UNESCO", "titulo": "Tango",
         "texto": "Nasceu nos cortiços e portos do Rio da Prata e virou Patrimônio da Humanidade em 2009, "
                  "reconhecido junto com o Uruguai. Em San Telmo é comum ver casais dançando na rua, perto da "
                  "Plaza Dorrego."},
        {"foto": "filete", "cor": "sol", "tag": "Patrimônio da UNESCO", "titulo": "Filete porteño",
         "texto": "Volutas, flores, fitas e letras caprichadas: a arte nasceu decorando carroças e ônibus e hoje "
                  "enfeita placas de bares e lojas. É Patrimônio Imaterial da Humanidade desde 2015."},
        {"foto": "asado", "cor": "laranja", "tag": "Ritual", "titulo": "Asado",
         "texto": "Mais que churrasco: fogo lento, achuras, chorizo, provoleta e cortes como entraña e bife de "
                  "chorizo. A grande noite de carne do roteiro é 30/12, em Palermo."},
        {"foto": "alfajor", "cor": "rosa", "tag": "Doce", "titulo": "Alfajor e doce de leite",
         "texto": "Dois biscoitos, recheio de doce de leite e cobertura de chocolate: a lembrancinha número um "
                  "(Havanna, Cachafaz). No sorvete, peçam dulce de leche granizado."},
        {"foto": "tortoni", "cor": "roxo", "tag": "Desde 1858", "titulo": "Cafés notables",
         "texto": "Buenos Aires protege seus cafés históricos como patrimônio da cidade. O Café Tortoni, aberto "
                  "em 1858, recebeu Borges e Gardel e ainda serve chocolate com churros."},
    ],
}

GEMEOS = {
    "titulo": "Os gêmeos do Rio da Prata",
    "texto": ("O arquiteto italiano Mario Palanti projetou o Palacio Barolo (Buenos Aires, 1923) e o Palacio Salvo "
              "(Montevidéu, 1928), quase irmãos e ambos com um farol no topo. Vocês visitam os dois: o Salvo no "
              "domingo 27/12 e o rooftop do Barolo, o Salón 1923, na sexta 01/01."),
    "fotos": [("salvo", "Salvo · 1928"), ("barolo", "Barolo · 1923")],
}

# Fotos do topo do site
POLAROIDES = [
    ("salvo", "Palacio Salvo"),
    ("tango", "Tango em San Telmo"),
    ("ateneo", "El Ateneo"),
    ("candombe", "Candombe"),
]
