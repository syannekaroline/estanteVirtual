from controller.request import request
from interface.screens.HomeWindow import HomeWindow
from controller.database import *


# criando banco e tabelas
create_database()

home_window = HomeWindow()
home_window.generate_home_window()




# 9788595081536 -> O Homem Mais Rico da Babilônia
# 8524905549 -> A REvoluçã Informacional
# 8573081082 -> Computer Crimes - A Criminalidadena Era dos Computadores 
# 9780805210408 -> O processo - Kafka
# 9780132350884 -> Clean Code
# pattern = re.compile(r"\[\'|\'\]") -> Padrão para retornar uma string de lista em lista novamente