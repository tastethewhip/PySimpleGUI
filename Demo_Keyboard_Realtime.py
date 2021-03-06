#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.Text("Hold down a key")],
          [sg.Button("OK")]]

window = sg.Window("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False).Layout(layout)

while True:
    event, values = window.ReadNonBlocking()

    if event == "OK":
        print(event, values, "exiting")
        break
    if event is not None:
        if len(event) == 1:
            print('%s - %s' % (event, ord(event)))
        else:
            print(event)
    elif values is None:
        break
