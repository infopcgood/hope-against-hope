# extra project-wide functions here but not really much


# floating point error correction
def same_with_errors(a, b, error=1.5):
    return bool(abs(a - b) <= error)


# quit game
def quit_game(screen, scene, main_player):
    exit()
