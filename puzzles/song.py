from dataclasses import dataclass

@dataclass
class Note:
    length_quarternotes: float
    frequency_hz: float

# One is the loneliest number that you'll ever do

C = 523.25
Bb = 466.16
G = 392
F = 349.23
Eb = 311.13
Ab = 415.3

notes = [Note(.5, C), Note(.25, Bb), Note(0.125, C), Note(.25, Bb), 
         Note(.125, G), Note(.125, F), Note(.25, Eb), Note(.125, F),
         Note(.125, G), Note(.75+.25+.125, G)]

preoutput = []

for note in notes:
    preoutput.append( f'{note.length_quarternotes:.3f}|{note.frequency_hz:.2f}')

output = ','.join(preoutput)

print (output)