from Content.Content import Content

class TextContent(Content):
    def __init__(self, string: str):
        super(). __init__(string)

    def getValue(self) -> str : 
        return self.value
    
    def setValue(self, value: str) -> None:
        self.value = value