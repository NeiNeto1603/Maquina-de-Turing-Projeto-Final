# TuringMachineSimulator.py

class TuringMachineSimulator:
    def _init_(self, initial_tape, initial_state):
        # Inicializa a Máquina de Turing com a fita inicial, estado inicial e outras variáveis.
        self.transitions = {}  # Dicionário para armazenar as transições da Máquina de Turing.
        self.tape = list(initial_tape)  # Converte a fita inicial em uma lista para facilitar a manipulação.
        self.head_position = 0  # Posição inicial da cabeça de leitura/escrita na fita.
        self.current_state = initial_state  # Estado inicial da Máquina de Turing.

    def add_transition(self, current_state, current_symbol, next_state, write_symbol, move):
        # Adiciona uma transição à tabela de transições.
        self.transitions[(current_state, current_symbol)] = (next_state, write_symbol, move)

    def run(self):
        # Executa a Máquina de Turing até que uma condição de parada seja atingida.
        while True:
            current_symbol = self.tape[self.head_position]  # Lê o símbolo atual na posição da cabeça.
            current_state_symbol_pair = (self.current_state, current_symbol)  # Par estado/símbolo atual.

            # Verifica se há uma transição definida para o estado/símbolo atual.
            if current_state_symbol_pair not in self.transitions:
                break  # Se não houver transição, interrompe a execução.

            # Obtém a próxima transição com base no estado/símbolo atual.
            next_state, write_symbol, move = self.transitions[current_state_symbol_pair]

            # Atualiza o estado, escreve o símbolo na fita e move a cabeça conforme as regras.
            self.current_state = next_state
            self.tape[self.head_position] = write_symbol

            # Move a cabeça para a direita, esquerda ou mantém a posição, conforme especificado.
            if move == 'R':
                self.head_position += 1
            elif move == 'L':
                self.head_position -= 1

            # Garante que a fita seja infinita à direita, inserindo/removendo 'B' quando necessário.
            if self.head_position < 0:
                self.tape.insert(0, 'B')
                self.head_position = 0
            elif self.head_position == len(self.tape):
                self.tape.append('B')

            # Imprime o estado atual e a configuração da fita após cada passo.
            print(f"State: {self.current_state}, Tape: {''.join(self.tape)}")

    def load_program(self, program_file):
        # Carrega as transições da Máquina de Turing a partir de um arquivo de configuração.
        with open(program_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                self.add_transition(parts[0], parts[1], parts[2], parts[3], parts[4])

    def load_input_tape(self, input_tape_file):
        # Carrega a fita de entrada a partir de um arquivo de texto.
        with open(input_tape_file, 'r') as file:
            self.tape = list(file.read().strip())

    def save_output_tape(self, output_tape_file):
        # Salva a fita resultante em um arquivo de texto.
        with open(output_tape_file, 'w') as file:
            file.write(''.join(self. Tape))