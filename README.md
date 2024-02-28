# Maquina-de-Turing-Projeto-Final
Projeto Final para aula do Della

Como configurar os arquivos program_config.txt e input_tape.txt para o seu simulador de Máquina de Turing.
1. Arquivo program_config.txt
O arquivo program_config.txt é utilizado para definir as transições da Máquina de Turing. Cada linha representa uma transição no formato:

estado_atual,simbolo_atual,proximo_estado,simbolo_escrito,movimento

•	estado_atual: O estado atual da Máquina de Turing.
•	simbolo_atual: O símbolo lido na fita no estado atual.
•	proximo_estado: O próximo estado para onde a Máquina de Turing deve ir.
•	simbolo_escrito: O símbolo que será escrito na fita no lugar do símbolo atual.
•	movimento: A direção para a qual a cabeça da Máquina de Turing deve se mover (R para direita, L para esquerda).

Exemplo:

q0,0,q1,1,R
q0,1,q2,0,L
q1,0,q1,0,R
q1,1,q1,1,R
q2,0,q2,0,L
q2,1,q2,1,L
q2,B,q3,B,R

Neste exemplo, temos transições que especificam como a Máquina de Turing deve se comportar ao ler diferentes símbolos nos estados específicos.

2. Arquivo input_tape.txt

O arquivo input_tape.txt contém a configuração inicial da fita que a Máquina de Turing irá ler. Cada símbolo da fita é representado por um caractere. O conteúdo do arquivo é lido como a fita inicial da esquerda para a direita.

Exemplo:
0101
Neste exemplo, a fita inicial contém os símbolos "0", "1", "0", "1".

Execução do Código
Quando você executa o código da Máquina de Turing com esses arquivos de entrada, o código processa a fita de acordo com as transições definidas no arquivo program_config.txt e imprime o estado da Máquina de Turing e a configuração da fita após cada passo. O resultado final é salvo no arquivo output_tape.txt.
Certifique-se de adaptar os arquivos program_config.txt e input_tape.txt de acordo com a lógica específica da sua Máquina de Turing.
