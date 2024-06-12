import requests
from WebScaping import precioInicial
from WebScaping import precioDeseado

def telegram_bot_sendtext(bot_message):
    
    bot_token = '7310243413:AAGIzMU5AQYBElWdsVJoowjNpKjvcscAaCg'
    bot_chatID = '6392260582'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    
if precioInicial < precioDeseado:
    test = telegram_bot_sendtext(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioInicial)}\nEnlace: https://n9.cl/ptq0xw")
else:
    test = telegram_bot_sendtext(f" ¡El precio sigue muy alto! Esta en:  {'$'+str(precioInicial)}")
 