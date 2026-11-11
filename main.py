memewords = {
    "LOL": "una respuesta a algo gracioso",
    "CRINGE": "algo raro o embarazoso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado",
}
word = input('Que palabra deseas aprender?')
while True:
    if word in memewords.keys():
        word = input('Que otra palabra deseas aprender?')
        print(memewords[word])
    else:
        print("Esa palabra no esta en nuestro diccionario")
