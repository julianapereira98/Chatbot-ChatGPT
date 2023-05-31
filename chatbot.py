# Projeto 3 - Construindo Chatbot Personalizado com ChatGPT e Linguagem Python

# Imports
import openai
from config import OPENAI_API_KEY

# Key
openai.api_key = OPENAI_API_KEY

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    # Obtém a resposta do modelo de linguagem
    response = openai.Completion.create(

        #Modelo usado
        engine = "text-davinci-003",

        # Texto inicial da conversa com o chatbot
        prompt = texto,

        # Comprimento da respostaa gerada pelo modelo
        max_tokens = 150,

        # Quantas conclusões gerar para cada prompt
        n = 5,

        # O texto retornado não conterá a sequência de parada
        stop = None,

        # Medidade da aleatoriedade de um texto gerado pelo modelo, valor entre 0 e 1
        # Valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a 0 significam que a saída pe muito identificável
        temperature = 0.8,
    )

    return response.choices[0].text.strip()

def main():

    print("\nBem-Vindo ao GPT Chatbot do Projeto 3 do curso da Data Science Academy!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    while True:

        # Coleta a pergunta digitada pelo usuário
        user_message = input("\nVocê: ")

        # Se a mensagem for "sair" finaliza o programa
        if user_message.lower() == "sair":
            break

        # Coloca a mensagem digitada pelo usuário na variável gpt4_prompt
        gpt_prompt = f"\nUsuário: {user_message}\nChatbot:"

        # Obtém a resposta do modelo executadno a função gera_texto()
        chatbot_response = gera_texto(gpt_prompt)

        # Imprime a resposta do chatbot
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa
if __name__ == "__main__":
    main()