# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.


class Note:
    def __init__(self, High: str, Medium: str, Low: str ):
        self.High:str = High
        self.Medium:str = Medium
        self.Low:str = Low

    def __int__(self, code: str , tittle: str , text: str , importance: str , datetime: str):
        self.code = code
        self.tittle = tittle
        self.text = text
        self.importance = importance
        self.creation.date = datetime.now()
        self.tags = []

    def add_tag(self, tag):



class Notebook:
    def __init__(self):
