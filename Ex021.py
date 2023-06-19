# Importando a biblioteca Pygame
import pygame

# Inicializar os módulos do Pygame instalado
pygame.init()

# Inicializar o mixer Pygame
pygame.mixer.init()

# Carregar um arquivo de música para reprodução
pygame.mixer.music.load('teste.mp3')

# Iniciar a reprodução do fluxo de música
pygame.mixer.music.play()

# Verificar se o fluxo de música está em uso,
# Quando não estiver mais em uso, ele sairá do loop
while pygame.mixer.music.get_busy():
    continue

# Sair do programa
pygame.quit()
