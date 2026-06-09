# Projeto Horizon

## Descrição

A Horizon é uma proposta de estufa-laboratório inteligente voltada para a análise de substratos em futuras aplicações de agricultura lunar.

Nesta etapa da Global Solution, desenvolvemos um programa em Python para comparar quatro compartimentos:

- solo terrestre comum;
- rególito lunar simulado puro;
- rególito simulado com biochar;
- rególito simulado com hidrogel.


## Atenção: duração da simulação

A simulação considera um período de **6 minutos**. Esse intervalo representa a janela de análise adotada para o experimento Horizon durante o voo suborbital.

Como o período em microgravidade é curto, o objetivo do projeto não é acompanhar o crescimento completo de plantas. A proposta é comparar o comportamento dos substratos, observando principalmente a retenção de água e a estabilidade da umidade.

Por esse motivo, o gráfico pode apresentar uma variação discreta durante os seis minutos. Mesmo assim, ele permite comparar quais substratos mantêm melhor a umidade nesse intervalo.



## Como funciona

Cada substrato possui uma taxa simulada de perda de água. Quanto menor essa taxa, maior é a capacidade de manter a umidade durante o experimento.

Para representar essa perda gradual, utilizamos o número de Euler, aproximado no código como `2.71828`. Ele é usado porque a umidade não diminui de uma vez: ela vai reduzindo aos poucos ao longo do tempo.

O programa também calcula o **IVSE**, que significa **Índice de Viabilidade do Substrato Espacial**. Esse índice foi criado pelo grupo para facilitar a comparação dos resultados. Ele leva em consideração:

- retenção de água;
- estabilidade da umidade;
- estabilidade térmica;
- energia restante;
- risco de falha.

Depois dos cálculos, cada substrato recebe uma classificação:

- promissor;
- aceitável;
- inviável.

Ao final, o programa informa qual substrato apresentou o melhor resultado simulado.

## O que o código utiliza

O arquivo `Horizon_GS.py` utiliza somente conteúdos básicos de Python:

- funções;
- variáveis;
- cálculos matemáticos;
- `if`, `elif` e `else`;
- `print`.

Não é necessário instalar ou importar nenhuma biblioteca.

## Como executar

Basta ter o Python instalado. No terminal, dentro da pasta do projeto, execute:

```bash
python Horizon.py
```

## Observação

Os valores utilizados são simulados para fins acadêmicos. Eles não representam resultados reais de laboratório ou de testes realizados em microgravidade.

## Integrantes

- Gabriel Ferreira Flausino | RM572486
- Felipe Kenji Takata | RM568739
- Kelso Oliveira do Amaral Sobrinho | RM573719
- Joaquim Gaspardo Souza Moura | RM572208

## Instituição

FIAP - Global Solution 2026  
Disciplina: Differentiated Problem Solving
