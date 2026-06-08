def calcular_retencao(umidade_inicial, umidade_final):
    retencao = (umidade_final / umidade_inicial) * 100
    return retencao


def calcular_ivse(r, u, t, e, f):
    ivse = (0.35 * r) + (0.25 * u) + (0.20 * t) + (0.10 * e) - (0.10 * f)
    return ivse


def classificar_substrato(ivse):
    if ivse >= 80:
        return "Promissor"
    elif ivse >= 60:
        return "Aceitável"
    else:
        return "Inviável"


umidade_inicial = 100
umidade_final = 90

retencao = calcular_retencao(umidade_inicial, umidade_final)

ivse = calcular_ivse(
    retencao,
    88,
    85,
    90,
    10
)

resultado = classificar_substrato(ivse)

print("Retenção de Água:", retencao)
print("IVSE:", round(ivse, 2))
print("Classificação:", resultado)