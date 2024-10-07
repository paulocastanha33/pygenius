# pygenius
Jogo desenvolvido em Python com QtDesigner - com inspiração no jogo Genius anos 80

Este projeto é uma implementação do clássico jogo "Genius" (ou "Simon") utilizando Python e PyQt5 para a interface gráfica. O objetivo do jogo é memorizar e repetir uma sequência de cores que é gerada aleatoriamente, com a sequência aumentando em complexidade a cada nível. O jogador deve alcançar um determinado nível para vencer o jogo.

# Funcionalidades

Botões interativos: Quatro botões coloridos (verde, vermelho, amarelo, azul) que o jogador deve apertar em uma ordem específica.
Sequência de cores: Uma sequência de cores é gerada aleatoriamente a cada nível, e o jogador deve repeti-la.
Níveis de dificuldade: A sequência de cores aumenta a cada nível, e o jogador deve chegar ao nível 5 para vencer.
Cronômetro: Exibe o tempo que o jogador leva para completar o jogo.
Mensagens de vitória e derrota: Exibe uma mensagem ao final do jogo, indicando se o jogador venceu ou perdeu.
Reiniciar jogo: Possui um botão de reiniciar para começar o jogo novamente.

# Requisitos

Python 3.x
PyQt5: A biblioteca de interface gráfica do usuário.
Instalação do PyQt5
Para instalar o PyQt5, execute o seguinte comando no terminal:

bash
Copiar código
pip install PyQt5

# Como Jogar

Inicie o jogo: Clique no botão "Iniciar".
Memorize a sequência: O jogo irá mostrar uma sequência de cores. Memorize-a.
Reproduza a sequência: Aperte os botões coloridos na mesma ordem que foi mostrada.
Avance de nível: Se a sequência estiver correta, você avança de nível e uma nova cor será adicionada à sequência.
Vença: Complete até o nível 5 para vencer o jogo.
Perdeu?: Caso aperte uma cor errada, o jogo exibe uma mensagem de derrota e permite reiniciar.

# Estrutura do Código
GeniusGame: Classe principal do jogo.

# Atributos:

sequence: Armazena a sequência de cores a ser reproduzida.
player_sequence: Armazena a sequência de cores reproduzida pelo jogador.
level: Armazena o nível atual do jogo.
time_elapsed: Contabiliza o tempo total do jogo.

# Métodos principais:

start_game(): Inicia o jogo e o cronômetro.
next_level(): Avança para o próximo nível.
show_sequence(): Mostra a sequência de cores ao jogador.
player_input(): Registra a entrada do jogador e verifica a sequência.
check_sequence(): Verifica se a sequência reproduzida pelo jogador está correta.
game_over(): Exibe uma mensagem de derrota se a sequência estiver incorreta.
victory(): Exibe uma mensagem de vitória ao jogador.
restart_game(): Reinicia o jogo.
update_timer(): Atualiza o cronômetro.

# Como Executar o Projeto

Clone este repositório para o seu computador.

bash
Copiar código
git clone https://github.com/paulocastanha33/pygenius.git
Navegue até a pasta do projeto.

bash
Copiar código
cd genius-game

Execute o script Python:

bash
Copiar código
python genius.py

# Interface Gráfica
A interface gráfica foi criada usando o Qt Designer e carregada no código através do método uic.loadUi(). O arquivo .ui utilizado para a interface está localizado em /home/paulocastanha/Área de trabalho/pygenius/genius.ui.

# Botões
Os quatro botões de cores (verde, vermelho, amarelo e azul) são conectados ao código para capturar os cliques do jogador e validar a sequência. A interface também conta com um botão "Iniciar" e um botão "Reiniciar".

# Cronômetro
O tempo de jogo é mostrado em um QLabel e é atualizado a cada segundo, permitindo que o jogador veja quanto tempo levou para completar o jogo.

# Estrutura do Diretório
genius.py: Script principal que contém a lógica do jogo.
genius.ui: Arquivo da interface gráfica criada no Qt Designer.

README.md: Este arquivo, com instruções e documentação.

# Contribuições

Contribuições são bem-vindas! Se você deseja melhorar o projeto ou adicionar novos recursos, sinta-se à vontade para abrir um pull request.

Com isso, o jogo está pronto para ser jogado e modificado conforme necessário.
