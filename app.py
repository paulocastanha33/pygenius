import sys
import random
from PyQt5 import QtWidgets, uic, QtCore, QtGui

# Lista de cores disponíveis
cores = ["verde", "vermelho", "amarelo", "azul"]

class GeniusGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(GeniusGame, self).__init__()
        
        # Carregar a interface gráfica do arquivo .ui
        uic.loadUi('/home/paulocastanha/Área de trabalho/pygenius/genius.ui', self)

        # Conectar os botões à lógica do jogo
        self.green_button = self.findChild(QtWidgets.QPushButton, 'greenButton')
        self.red_button = self.findChild(QtWidgets.QPushButton, 'redButton')
        self.yellow_button = self.findChild(QtWidgets.QPushButton, 'yellowButton')
        self.blue_button = self.findChild(QtWidgets.QPushButton, 'blueButton')
        self.start_button = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.restart_button = self.findChild(QtWidgets.QPushButton, 'restartButton')  # Novo botão Restart
        
        self.timer_label = self.findChild(QtWidgets.QLabel, 'timerLabel')  # Adicionar um QLabel para o cronômetro

        # Conectar sinais dos botões a métodos
        self.green_button.clicked.connect(lambda: self.player_input("verde"))
        self.red_button.clicked.connect(lambda: self.player_input("vermelho"))
        self.yellow_button.clicked.connect(lambda: self.player_input("amarelo"))
        self.blue_button.clicked.connect(lambda: self.player_input("azul"))
        self.start_button.clicked.connect(self.start_game)
        self.restart_button.clicked.connect(self.restart_game)  # Conectar o botão restart ao método restart_game

        # Inicializar variáveis do jogo
        self.sequence = []          # Sequência de cores a ser mostrada
        self.player_sequence = []   # Sequência de cores escolhidas pelo jogador
        self.level = 0              # Nível atual do jogo

        # Variáveis do cronômetro
        self.time_elapsed = 0
        self.timer = QtCore.QTimer()  # Criar um timer para o cronômetro
        self.timer.timeout.connect(self.update_timer)  # Conectar o timer a um método para atualizar o tempo

    def start_game(self):
        """Inicia o jogo e o cronômetro."""
        self.sequence = []  # Reiniciar a sequência
        self.level = 0      # Reiniciar o nível
        self.time_elapsed = 0  # Reiniciar o tempo
        self.timer.start(1000)  # Iniciar o cronômetro, atualiza a cada segundo
        self.next_level()  # Avançar para o próximo nível

    def next_level(self):
        """Avança para o próximo nível do jogo."""
        self.level += 1  # Aumenta o nível
        self.player_sequence = []  # Reiniciar a sequência do jogador
        self.sequence.append(random.choice(cores))  # Adicionar uma nova cor aleatória à sequência
        self.show_sequence()  # Mostrar a sequência ao jogador

    def show_sequence(self):
        """Mostra a sequência de cores para o jogador."""
        for i, color in enumerate(self.sequence):
            # Acender os botões na sequência com um atraso
            QtCore.QTimer.singleShot(1000 * (i+1), lambda c=color: self.light_up(c))

    def light_up(self, color):
        """Acende o botão correspondente à cor e depois o apaga."""
        button = self.get_button_by_color(color)  # Obtém o botão correspondente à cor
        original_color = button.palette().color(QtGui.QPalette.Window)  # Guarda a cor original do botão
        button.setStyleSheet("background-color: white")  # Muda a cor do botão para branco
        QtCore.QTimer.singleShot(500, lambda: button.setStyleSheet(f"background-color: {color}"))  # Retorna à cor original

    def get_button_by_color(self, color):
        """Retorna o botão correspondente à cor fornecida."""
        if color == "verde":
            return self.green_button
        elif color == "vermelho":
            return self.red_button
        elif color == "amarelo":
            return self.yellow_button
        elif color == "azul":
            return self.blue_button

    def player_input(self, color):
        """Registra a entrada do jogador e verifica a sequência."""
        self.player_sequence.append(color)  # Adiciona a cor à sequência do jogador
        self.check_sequence()  # Verifica se a sequência está correta

    def check_sequence(self):
        """Verifica se a sequência do jogador está correta."""
        if self.player_sequence == self.sequence[:len(self.player_sequence)]:
            # Se a sequência do jogador estiver correta
            if len(self.player_sequence) == len(self.sequence):
                # Se o jogador completou toda a sequência
                if self.level == 5:  # Colocar o nível máximo (por exemplo, 5)
                    self.victory()  # Chama o método de vitória
                else:
                    QtCore.QTimer.singleShot(1000, self.next_level)  # Avança para o próximo nível
        else:
            self.game_over()  # Se a sequência estiver errada, chama o método de game over

    def game_over(self):
        """Método chamado quando o jogador erra."""
        self.start_button.setText("Tentar Novamente")  # Altera o texto do botão para "Tentar Novamente"
        self.timer.stop()  # Para o cronômetro quando o jogo termina
        
        # Exibir a mensagem e a sequência correta
        correct_sequence = ", ".join(self.sequence)  # Converte a sequência correta em uma string
        msg = QtWidgets.QMessageBox()  # Cria uma mensagem
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Game Over")
        msg.setText("Você perdeu!")  # Mensagem de perda
        msg.setInformativeText(f"A sequência correta era: {correct_sequence}")  # Mostra a sequência correta
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()  # Exibe a mensagem

    def victory(self):
        """Exibe uma mensagem de vitória."""
        self.start_button.setText("Vitória!")  # Altera o texto do botão para "Vitória"
        self.timer.stop()  # Para o cronômetro quando o jogador ganha
        
        # Exibir uma mensagem de vitória
        msg = QtWidgets.QMessageBox()  # Cria uma mensagem
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Vitória!")
        msg.setText("Parabéns! Você completou a sequência corretamente.")  # Mensagem de vitória
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()  # Exibe a mensagem

    def restart_game(self):
        """Método para reiniciar o jogo."""
        self.timer.stop()  # Para o cronômetro
        self.time_elapsed = 0  # Zera o tempo
        self.timer_label.setText(f"Tempo: 0s")  # Reseta o cronômetro na tela
        self.start_button.setText("Iniciar")  # Reseta o texto do botão de início
        self.sequence = []  # Reinicia a sequência
        self.player_sequence = []  # Reinicia a sequência do jogador
        
        # Restaurar as cores originais dos botões
        self.green_button.setStyleSheet("background-color: green")
        self.red_button.setStyleSheet("background-color: red")
        self.yellow_button.setStyleSheet("background-color: yellow")
        self.blue_button.setStyleSheet("background-color: blue")
        
        print("Jogo reiniciado!")  # Mensagem no console para indicar que o jogo foi reiniciado

    def update_timer(self):
        """Atualiza o cronômetro a cada segundo."""
        self.time_elapsed += 1  # Aumenta o tempo
        self.timer_label.setText(f"Tempo: {self.time_elapsed}s")  # Atualiza o QLabel com o tempo

# Inicializa a aplicação
app = QtWidgets.QApplication(sys.argv)
window = GeniusGame()  # Cria uma instância do jogo
window.show()  # Exibe a janela do jogo
app.exec_()  # Inicia o loop da aplicação
