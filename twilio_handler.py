from twilio.rest import Client

# credenciais da API do Twilio
TWILIO_ACCOUNT_SID = 'tulio'
TWILIO_AUTH_TOKEN = 'tulio'
client_twilio = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
twilio_number = 'whatsapp:+19033475768' # Coloca ogit numero do twilio aqui


class Twilio:

    # Função para enviar mensagem de texto para o WhatsApp usando o Twilio
    def send_message_to_whatsapp(message, to_number):

        message = client_twilio.messages.create(
            from_=twilio_number,
            body=message,
            to=to_number
        )
        print(f"Message sent to WhatsApp")


    # # Função para enviar mensagem de audio para o WhatsApp usando o Twilio
    # def send_audio_message_to_whatsapp(audioURL, to_number):
    #     message = client_twilio.messages.create(
    #         from_=twilio_number,
    #         to=to_number,
    #         media_url = audioURL
    #     )
    #     print(f"Message sent to WhatsApp")
