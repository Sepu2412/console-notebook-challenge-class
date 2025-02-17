# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.


class Note:
    def __init__(self, High: str, Medium: str, Low: str ):
        self.High:str = High
        self.Medium:str = Medium
        self.Low:str = Low

    def __int__(self, code: str , tittle: str , text: str , importance: str , datetime: str):
        self.code: str = code
        self.tittle: str = tittle
        self.text: str = text
        self.importance: str = importance
        self.creation_date: str = datetime.now()
        self.tags = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"date: {self.creation_date}\n{self.tittle}: {self.text}"



class Notebook:
    def __init__(self):
        self.notes: list[Note]= []

    def add_note(self, tittle: str , text: str , importance: str )-> int:
