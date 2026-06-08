# Projeto Horizon - Global Solution 2026
# Comparacao simulada de substratos para agricultura lunar.

## ATENCAO:
# Esta simulacao considera um periodo de 6 minutos.
# Esse intervalo representa a janela de analise do experimento Horizon
# durante o voo suborbital.
# O objetivo nao e simular o crescimento completo de plantas,
# mas comparar como os substratos mantem a umidade durante
# um curto periodo em condicoes de microgravidade.
# Os valores utilizados sao simulados para fins academicos.


def calcular_umidade(umidade_inicial, taxa_perda, tempo):
    # 2.71828 e uma aproximacao do numero de Euler.
    # Ele permite representar uma reducao gradual da umidade.
    umidade_final = umidade_inicial * (2.71828 ** (-taxa_perda * tempo))
    return umidade_final


def calcular_retencao(umidade_inicial, umidade_final):
    retencao = (umidade_final / umidade_inicial) * 100
    return retencao


#IVSE - Indice de Viabilidade para Substratos Espaciais
def calcular_ivse(retencao, estabilidade_umidade, estabilidade_termica, energia, risco_falha):
    confiabilidade = 100 - risco_falha

    ivse = (
        0.35 * retencao
        + 0.25 * estabilidade_umidade
        + 0.20 * estabilidade_termica
        + 0.10 * energia
        + 0.10 * confiabilidade
    )

    return ivse


def classificar_substrato(ivse):
    if ivse >= 80:
        return "Promissor"
    elif ivse >= 60:
        return "Aceitavel"
    else:
        return "Inviavel"


# Configuracoes da simulacao
umidade_inicial = 100
periodo_em_minutos = 6

# Compartimento A - Solo terrestre comum
umidade_solo_comum = calcular_umidade(umidade_inicial, 0.015, periodo_em_minutos)
retencao_solo_comum = calcular_retencao(umidade_inicial, umidade_solo_comum)
ivse_solo_comum = calcular_ivse(retencao_solo_comum, 78, 84, 88, 8)
classificacao_solo_comum = classificar_substrato(ivse_solo_comum)

# Compartimento B - Regolito lunar simulado puro
umidade_regolito_puro = calcular_umidade(umidade_inicial, 0.035, periodo_em_minutos)
retencao_regolito_puro = calcular_retencao(umidade_inicial, umidade_regolito_puro)
ivse_regolito_puro = calcular_ivse(retencao_regolito_puro, 42, 72, 84, 24)
classificacao_regolito_puro = classificar_substrato(ivse_regolito_puro)

# Compartimento C - Regolito simulado com biochar
umidade_biochar = calcular_umidade(umidade_inicial, 0.012, periodo_em_minutos)
retencao_biochar = calcular_retencao(umidade_inicial, umidade_biochar)
ivse_biochar = calcular_ivse(retencao_biochar, 80, 83, 87, 9)
classificacao_biochar = classificar_substrato(ivse_biochar)

# Compartimento D - Regolito simulado com hidrogel
umidade_hidrogel = calcular_umidade(umidade_inicial, 0.006, periodo_em_minutos)
retencao_hidrogel = calcular_retencao(umidade_inicial, umidade_hidrogel)
ivse_hidrogel = calcular_ivse(retencao_hidrogel, 92, 88, 90, 5)
classificacao_hidrogel = classificar_substrato(ivse_hidrogel)

# Resultados
print("PROJETO HORIZON - RESULTADOS SIMULADOS")
print("Periodo analisado:", periodo_em_minutos, "minutos")
print()

print("A - Solo terrestre comum")
print("Umidade final:", round(umidade_solo_comum, 2), "%")
print("Retencao:", round(retencao_solo_comum, 2), "%")
print("IVSE:", round(ivse_solo_comum, 2))
print("Classificacao:", classificacao_solo_comum)
print()

print("B - Regolito lunar simulado puro")
print("Umidade final:", round(umidade_regolito_puro, 2), "%")
print("Retencao:", round(retencao_regolito_puro, 2), "%")
print("IVSE:", round(ivse_regolito_puro, 2))
print("Classificacao:", classificacao_regolito_puro)
print()

print("C - Regolito simulado com biochar")
print("Umidade final:", round(umidade_biochar, 2), "%")
print("Retencao:", round(retencao_biochar, 2), "%")
print("IVSE:", round(ivse_biochar, 2))
print("Classificacao:", classificacao_biochar)
print()

print("D - Regolito simulado com hidrogel")
print("Umidade final:", round(umidade_hidrogel, 2), "%")
print("Retencao:", round(retencao_hidrogel, 2), "%")
print("IVSE:", round(ivse_hidrogel, 2))
print("Classificacao:", classificacao_hidrogel)
print()

# Encontrando maior IVSE
melhor_substrato = "Solo terrestre comum"
melhor_ivse = ivse_solo_comum

if ivse_regolito_puro > melhor_ivse:
    melhor_substrato = "Regolito lunar simulado puro"
    melhor_ivse = ivse_regolito_puro

if ivse_biochar > melhor_ivse:
    melhor_substrato = "Regolito simulado com biochar"
    melhor_ivse = ivse_biochar

if ivse_hidrogel > melhor_ivse:
    melhor_substrato = "Regolito simulado com hidrogel"
    melhor_ivse = ivse_hidrogel

print("Melhor resultado simulado:", melhor_substrato)
print("Maior IVSE:", round(melhor_ivse, 2))
print()
print("Observacao: os valores utilizados sao simulados para fins academicos.")
