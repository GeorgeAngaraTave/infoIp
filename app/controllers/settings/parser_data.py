import re
import html

def parserNumbers(value):
    if not value:
        value = 0

    return re.sub(r"\D", "", value).strip()

def parseCoordenates(type='latitude', d=0, m=0, s=0 ):
    degrees = parserNumbers(d)
    minutes = parserNumbers(m)
    seconds = parserNumbers(s)

    coord_text =  degrees+"° "+minutes+"\' "+seconds+"\'\'"

    if type=='longitude':
        coord_decimal = (degrees + (minutes/60) + (seconds/3600))*(-1)
    else:
        coord_decimal = (degrees + (minutes/60) + (seconds/3600))

    coordenates = {"text":coord_text, "decimal":coord_decimal}

    return coordenates

def clear_value(value):
    return html.escape(value.strip().replace("'", "\\'"), True)

def clear_params(params):
    json_data = []
    keys = []

    for key in params:
        keys.append(key)

    for result in params:
        json_data.append(clear_value(params[result]))

    data = dict(zip(keys,json_data))

    return data

def convert_to_string(value):
    return str(value)
