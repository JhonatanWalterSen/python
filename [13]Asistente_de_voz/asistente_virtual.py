import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / Idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#microfono escuchar de voz a texto
def trasnformar_audio_en_texto():

    # almacenar el recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera desde activación
        r.pause_threshold = 0.8

        # informar que inició la grabación
        print('Ya puedes hablar')

        # guardar lo escuchado como audio
        audio = r.listen(origen)

        try:
            # buscar en google lo escuchado
            pedido = r.recognize_google(audio, language='es-pe')

            # prueba de que puedo ingresar y transformar
            print(f' Dijiste: {pedido}')

            # devolver pedido
            return pedido

        # en caso que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print('No entendí')

            # devolver error
            return "Sigo esperando"

        except sr.RequestError:

            # prueba de que no comprendió el audio
            print('Ups no hay servicio')

            # devolver error
            return "Sigo esperando"

        except:
            # prueba de que no comprendió el audio
            print('Ups algo ha salido mal')

            # devolver error
            return "Sigo esperando"

# función pueda ser escuchadpo el asistente
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    # pronuncia el mensaje
    engine.say(mensaje)
    engine.runAndWait()

#engine = pyttsx3.init()
#for voces in engine.getProperty('voices'):
#    print(voces)

# informar el día de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear una var para el día de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }

    # decir el día de la semana
    hablar(f'El día de hoy es {calendario[dia_semana]}')

# informar que hora es
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)

#función de iniciar saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    # decir el saludo
    hablar(f'{momento}, soy Robotin, tu asistente virtual ¿En qué te puedo ayudar')

#funcion central del asistente
def pedir_cosas():

    # activar el saludo iniciar
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = trasnformar_audio_en_texto().lower()
        print(pedido)
        if 'abrir youtube' in pedido:
            hablar('Con gusto, buscando en youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar(f'Claro, estoy en ello')
            webbrowser.open('https://www.google.com')
            continue
        elif 'el día es' in pedido:
            pedir_dia()
            continue
        elif 'la hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Reproduciendo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion= pedido.split('de')[-1].strip()
            cartera = {
                        'apple': 'APPL',
                        'amazon': 'AMZN',
                        'google': 'GOOGL'
                        }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar(f'Perdón no la he encontrado')
                continue
        elif 'Adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break

pedir_cosas()