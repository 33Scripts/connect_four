class Player:
    """Represents a player in the Connect Four game.
    
    Stores player information including their name and piece color.
    
    Attributes:
        name (str): The player's name.
        color (str): The colorama color code for the player's pieces.
    """
    
    def __init__(self, name, color):
        """Initialize a new player.
        
        Args:
            name (str): The player's name.
            color (str): The colorama color code for the player's pieces.
        """
        self.name = name
        self.color = color
