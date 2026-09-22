"""
 STRINGS
    
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples
    '' o de dobles comillas "" es considerado un string. 
    
    Ejemplos:
        "Esto es un string"
        'Esto también es un string'
        'Le dije a un amigo, "Python" es mi lenguage favorito'
        "El lenguaje 'Python' lleva el nombre por Monty Python y no por la serpiente"

"""
name = "clase de proGramacion"
print(name)
print(name.title())
name = name.title() 
print(name)
"""
un metodo es una accion que python puede
realizar en un fragmento de datos o sobre
una variable. El punto  . despues de una variable
seguido del metodo title() dice que se tiene que
ejecutar title() de la variable name.

todos los metodos van seguidos de parentesis por que en ocaciones 
nesesita informacion adicional para funionar lo cual iria dentro
de los parentesis. En esta ociacion el metodo .title() no requiere 
informacion adicional para funcionar
"""
#otros metodos
print(name.upper())
print(name.lower())