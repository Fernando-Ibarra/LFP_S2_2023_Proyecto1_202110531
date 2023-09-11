class Configuration:
    
    def __init__(self, title: str = None, backgroundColor: str = None, fontStyle: str = None, style: str = None):
        self.title = title
        self.backgroundColor = backgroundColor
        self.fontStyle = fontStyle
        self.style = style
    
    def __str__(self):
        return f"Configuration(title={self.title}, backgroundColor={self.backgroundColor}, fontStyle={self.fontStyle}, style={self.style})"

    def getTitle(self):
        return self.title

    def getBackgroundColor(self):
        return self.backgroundColor
    
    def getFontStyle(self):
        return self.fontStyle
    
    def getStyle(self):
        return self.style