from agenttaskmanager.agent import root_agent
from google import genai
import os

print("🤖 A iniciar o Agente de Tarefas do Trello...")
print(f"Nome do agente: {root_agent.name}")
print(f"Descrição: {root_agent.description}")
print("-" * 50)
print("Dica: Podes começar a conversar com o agente ou pedir para gerir as tuas tarefas!")

# Inicializar o cliente GenAI
client = genai.Client()

# Criar a sessão de chat passando as instruções do sistema E as ferramentas do agente
chat = client.chats.create(
    model="gemini-3.8-flash", 
    config={
        "system_instruction": root_agent.instruction,
        "tools": root_agent.tools,
    }
)

print("\n💬 Chat iniciado! Escreve a tua mensagem (ou 'sair' para terminar):\n")

while True:
    try:
        user_input = input("Tu: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Até breve!")
            break
        
        if not user_input.strip():
            continue
            
        # Enviar mensagem (o SDK gere a execução automática das ferramentas se necessário)
        response = chat.send_message(user_input)
        print(f"\nAgente: {response.text}\n")
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}\n")