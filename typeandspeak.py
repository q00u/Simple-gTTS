from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound
import PySimpleGUI as sg

def speak(txt, lang='en'):
    gTTS(text=txt, lang=lang).write_to_fp(voice := NamedTemporaryFile())
    playsound(voice.name)
    voice.close()

# All the stuff in the window.
layout = [  [sg.InputText("Enter text to speak", key='Input1')] ]

# Todo (maybe): History window of previous things said

# Todo: Add quick buttons for common phrases
# Todo: Find a way to make that ^ dynamic

# Create the window
# Todo: Clear placeholder text when first typing
window = sg.Window("Type and Speak", layout, finalize=True)
# Bind to enter key
window['Input1'].bind('<Return>', '_Enter')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Input1' + '_Enter':
        speak(values['Input1'])
        window['Input1'].update(value='')

# Todo: Find out why it freezes when I ask a question
