def getEnvVar():
    with open(".env", "r") as f:
        raw = f.read()

    listRaw = raw.split("\n")

    listClean = []
    for _ in listRaw:
        listClean += [_.split("=")]
    del listClean[-1]
    settings = {}
    for _ in listClean:
        key = _[0]
        try :
            content = int(_[1])
        except :
            content = str(_[1])
        settings[key] = content
    return settings
