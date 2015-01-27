
def sanintize(time_string):
    if '_' in time_string:
        spliter = '_'
    elif ':' in time_string:
        spliter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.spliter(soliter)
    return (mins + '.' + secs)
