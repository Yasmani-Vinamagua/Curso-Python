def is_palindrome(string: str) -> bool: #funcion que recibe un string como parametro y devuelve un boolenao
    string = string.replace(" ","").lower() #borrar espacios y hacerlos minusculas
    return string == string[::-1]


def run():
    print(is_palindrome("ana"))

if __name__ == "__main__":
    run()