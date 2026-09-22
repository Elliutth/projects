#combinacion o concatenacion de STRING
first_name = "elliutth"
last_name = "guevara"
full_name = first_name +" "+ last_name
print(full_name)
print("hola", "elliutth" + " " + " isaac", first_name.title() + " " + last_name.title())
message = "!hola, " + full_name.title() + "!"
print(message)
#WhiteSpace
"""
Whitespace se refiere a cualquier string
(caracter) que no se imprime, es decir,
un espacio (" "), tabulacores (\t) y
finales de linea (\n)

los whitespaces se utilizan communmente para
organizar las salidas de texto a usuario
de talmanera que sea mas amigable de leer 
o ver para los usuarios.
"""
print("python")
print("\tpython")
print("\t\tpython")
print("Lenguajes: \n python \n C \n JavaScript")

#f-string
famous_person = "charly mercury"
message = f"{famous_person} una vez dijo: python es amor"
print(message)

qoute = "python is in the air"
message_2 = f"{famous_person} una vez dijo {qoute}"
print(message_2)