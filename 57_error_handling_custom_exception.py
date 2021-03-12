class customException(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)

try:
    string = 'Python '
    v = 3.9

    if not (isinstance(string,str) and isinstance(v,str)):
        raise customException('Custom error raised check variable datatype.')

except customException as er:
    print(er)