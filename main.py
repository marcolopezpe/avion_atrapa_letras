from game.game import Game

# Para compilar y crear ejecutable
# https://parzibyte.me/blog/2018/12/27/pyinstaller-assets-imagenes-archivos-ejecutable-python/
# https://www.youtube.com/watch?v=OzR2mfpbjYI
# https://www.youtube.com/watch?v=Vr9vl0qlggE
#
# pyinstaller --windowed --onefile --icon=icon.ico main.py

if __name__ == "__main__":
    g = Game()
