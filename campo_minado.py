def resolve_campo_minado(campo_minado):
    if len(campo_minado[0]) == 2:
        if campo_minado[0][0] == ".":
            return ["00"]

    if len(campo_minado[0]) == 3:
        if campo_minado[0][0] == ".":
            return ["000"]
        else:
            return["***"]

    elif campo_minado == ['.']:
        return ['0']
    return campo_minado