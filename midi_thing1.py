import mido
import time
port = mido.open_output()
print("Detected device: " + port.name)
if not port.is_output:
    print("Error: Port " + port.name + " is not an output!!")
    exit()
mid = mido.MidiFile('Windows_XP_Startup.mid')
print("Playing MIDI File: " + mid.filename)
for msg in mid.play():
    port.send(msg)
time.sleep(5)
mid = mido.MidiFile('Hamilton_-_Dear_Theodosia.mscz.mid')
print("Playing MIDI File: " + mid.filename)
for msg in mid.play():
    port.send(msg)
mid = mido.MidiFile('CANYON.MID.mid')
print("Playing MIDI File: " + mid.filename)
for msg in mid.play():
    port.send(msg)
