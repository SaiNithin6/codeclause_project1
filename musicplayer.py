from playsound import playsound
print("No.of available Songs\n1.Nagila\n2.NenLocal\n3.Voilin")
order=input('Enter the music which you want to play: ')
if "Nagila" in order:
    playsound('C://Program Files//Python311//H8//Nagila.mpeg')
elif "NenLocal" in order:
    playsound('C://Program Files//Python311//H8//NenLocal.mpeg')
elif "Voilin" in order:
    playsound('C://Program Files//Python311//H8//Voilin.mpeg')
