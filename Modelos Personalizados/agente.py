# Instalação da biblioteca atualizada:
# pip install -U google-genai

from google import genai
from google.genai import types

# Aqui é onde inserimos a chave da API
client = genai.Client(api_key="sua chave")


configuracao_personalizada = types.GenerateContentConfig(
    # Instrução de Sistema que molda o comportamento da IA
    system_instruction=(
        "Você é um tutor de programação sarcástico, mas muito prestativo. "
        "Seu nome é 'Dev ranzinza'. Você NUNCA deve dar o código pronto de primeira. "
        "Em vez disso, faça perguntas inteligentes para guiar o aluno até a solução. "
        "Use gírias de desenvolvedor e seja um pouco irônico."
    ),
    # Temperatura (Otimização): Controla a criatividade (0.0 = preciso, 1.0 = criativo)
    temperature=0.7, 
)

print("=== Bem-vindo ao Dev Ranzinza (Modelo Personalizado) ===\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() in ["sair", "exit"]:
        break
        
    # Chamada do modelo com as nossas customizações aplicadas
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Versão estável ideal para tarefas gerais
        contents=entrada,
        config=configuracao_personalizada # <--- Aqui é onde inserimos a personalização
    )

    print(f"\nDev Ranzinza: {response.text}\n")