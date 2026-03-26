def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError("Can not devide by Zero") from e
    
devide(10,0)


def devidee(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ValueError("Can not deivedeby zero")
devidee(10,0)
