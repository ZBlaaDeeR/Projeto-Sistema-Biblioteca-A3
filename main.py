import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from VIEW.tela_Login import TelaLogin


tela = TelaLogin()
tela.iniciar()