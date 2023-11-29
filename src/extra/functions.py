"""extra functions"""


def same_with_errors(a, b, error=1.5):
    """hidden method for error correction"""
    return bool(abs(a - b) <= error)


def quit_game(screen, scene, main_player):
    """quit game"""
    exit()
