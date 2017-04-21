def data_type(data_in=None):
    if isinstance(data_in, str):
        length = len(data_in)
        return length
    elif data_in == None:
        return 'no value'
    elif data_in == False or data_in == True:
        return data_in
    elif isinstance(data_in, int):
        if data_in > 100:
            return "more than 100"
        elif data_in < 100:
            return "less than 100"
        else:
            return "equal to 100"
    else:
        while isinstance(data_in, list):
            if len(data_in) > 2:
                return data_in[2]
            return None
