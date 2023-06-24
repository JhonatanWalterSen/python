import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

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


trasnformar_audio_en_texto()