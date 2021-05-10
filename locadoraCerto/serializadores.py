def diretor_net(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
    }


def diretor_bd(*args):
    return {
        "nome_completo": args[0]
    }


def genero_net(**kwargs):
    return {
        "nome": kwargs["nome"] if kwargs["nome"] else "",
    }


def genero_bd(*args):
    return {
        "nome": args[0]
    }


def filme_net(**kwargs):
    return {
        "titulo": kwargs["titulo"] if kwargs["titulo"] else "",
        "ano": kwargs["ano"] if kwargs["ano"] else "",
        "classificacao": kwargs["classificacao"] if kwargs["classificacao"] else "",
        "preco": kwargs["preco"] if kwargs["preco"] else "",
        "diretores_id": kwargs["diretores_id"] if kwargs["diretores_id"] else "",
        "generos_id": kwargs["generos_id"] if kwargs["generos_id"] else ""
    }


def filme_bd(*args):
    return {
        "titulo": args[0],
        "ano": args[0],
        "classificacao": args[0],
        "preco": args[0],
        "diretores_id": args[0],
        "generos_id": args[0]
    }


def usuario_net(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
        "CPF": kwargs["CPF"] if kwargs["CPF"] else ""
    }


def usuario_bd(*args):
    return {
        "nome_completo": args[0],
        "CPF": args[0]
    }

def delete_web(**kwargs):
    return {
        "id": kwargs["id"] if kwargs["id"] else ""
    }


def delete_bd(*args):
    return {
        "id": args[0]
    }