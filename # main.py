# main.py
from TuringMachineSimulator import TuringMachineSimulator

if _name_ == "_main_":
    # Cria uma instância da Máquina de Turing com uma fita inicial e estado inicial.
    tm = TuringMachineSimulator("0101", "q0")

    # Carrega as transições da Máquina de Turing a partir de um arquivo de configuração.
    tm.load_program("program_config.txt")

    # Carrega a fita de entrada a partir de um arquivo de texto.
    tm.load_input_tape("input_tape.txt")
    # Executa a Máquina de Turing.
    tm.run()

    # Salva a fita resultante em um arquivo de texto.
    tm.save_output_tape("output_tape.txt")