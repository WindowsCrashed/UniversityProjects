import matplotlib.pyplot as plt
from time import sleep
from os import system, name


# --------------------- Classes -------------------------


# ------------ Erros ---------------

# Para tratar erros relacionados à incompatibilidade de arrays
class LengthError(Exception):
    pass


# Para tratar erros relacionados a uma função inexistente
class FunctionError(Exception):
    pass


# ------------ Matemática ---------------

# Fórmulas adicionais
class Calculations:

    # Multiplica valores de 2 arrays
    def mult_xy(self, x, y):
        return [x[i]*y[i] for i in range(len(x))]

    # Calcula os quadrados de valores dentro de um array
    def sqr_arr(self, arr):
        return [x**2 for x in arr]

    # Calcula a equação dos mínimos quadrados,
    # retornando A, B e a equação em formato de string
    def calc_lea_sqr(self, sum_x, sum_y, sum_xy, sum_x2, n):
        a = round(((n * sum_xy) - (sum_x * sum_y)) /
                  ((n * sum_x2) - (sum_x**2)), 4)

        b = round((sum_y - (a * sum_x)) / n, 4)

        return {'val_a': a, 'val_b': b, 'func': f'y = {a}x + {b}'}

    # Estima um valor com base em determinada função
    def estimate(self, func, x):
        return (func['val_a'] * x) + func['val_b']


# Elementos relacionados a funções
class Function:
    def __init__(self):
        self.calc = Calculations()
        self.utils = Utilities()
        self.create_function()

    # Cria uma nova função
    def create_function(self):

        # Recebe um array de coordenadas X
        while True:
            try:
                print('\nLista de valores de X:')
                self.x = [round(float(val_x), 1) for val_x in input().split()]
                self.utils.clear()
                break

            except Exception:
                self.utils.print_error(
                    'Valores inválidos', 'Somente números são aceitos')

        # Recebe um array de coordenadas Y
        while True:
            try:
                print('\nLista de valores de Y:')
                self.y = [round(float(val_y), 1) for val_y in input().split()]
                self.utils.clear()

                if len(self.y) != len(self.x):
                    raise LengthError

                break

            except LengthError:
                self.utils.print_error('Valores inválidos',
                                       'Arrays devem ter o mesmo tamanho')

            except Exception:
                self.utils.print_error(
                    'Valores inválidos', 'Somente números são aceitos')

        # Cálculos
        n = len(self.x)
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_xy = sum(self.calc.mult_xy(self.x, self.y))
        sum_x2 = sum(self.calc.sqr_arr(self.x))
        self.line_min_sqr = self.calc.calc_lea_sqr(
            sum_x, sum_y, sum_xy, sum_x2, n)

    # Estima um valor usando a função atual
    def estimate_value(self):
        while True:
            try:
                print(f"{self.line_min_sqr['func']}\n")
                self.est_x = float(input('Valor estimado para X = '))

                self.utils.clear()

                break
            except Exception:
                self.utils.print_error(
                    'Valor inválido', 'Somente números são aceitos')

        self.est_y = self.calc.estimate(self.line_min_sqr, self.est_x)

        self.utils.clear()

    # Exibe a função em formato de título
    def display_function(self):
        print()
        self.utils.print_title('    Equação dos Mínimos Quadrados     ')
        print()

        print(self.line_min_sqr['func'])

        sleep(3)

        self.utils.clear()

    # Exibe o valor estimado, junto da função, em formato de título
    def display_estimate(self):
        print()
        self.utils.print_title(
            f'    Valor estimado para X = {self.est_x:.1f}     ')
        print()

        print(f"{self.line_min_sqr['func']}\n")

        print(f'y = {self.est_y:.2f}')

        sleep(3)

        self.utils.clear()


# Elementos relacionados ao Gráfico
class Graph:
    def __init__(self, _x, _y, _func):
        self.x = _x
        self.y = _y
        self.func = _func
        self.calc = Calculations()
        self.utils = Utilities()
        self.plot_scatter()

    # Planta o diagrama de dispersão
    def plot_scatter(self):
        plt.clf()

        # De certa forma centraliza do gráfico
        max_height = max(self.y) + (max(self.y) // 4)
        min_height = min(self.y) - (max(self.x) // 4)
        max_width = max(self.x) + (max(self.x) // 4)
        min_width = min(self.x) - (max(self.x) // 4)
        y_coord = []

        for val_x in self.x:
            y_coord.append(self.calc.estimate(self.func, val_x))

        plt.plot(self.x, self.y, 'o', color='xkcd:lightblue')
        plt.axis([min_width, max_width, min_height, max_height])
        plt.plot(self.x, y_coord, 'xkcd:deep sky blue')
        plt.grid(color='xkcd:deep sky blue', linewidth=0.35)
        ax = plt.gca()
        ax.set_facecolor('xkcd:black')

    # Exibe o diagrama de dispersão, junto de um título
    def display_scatter(self):
        print()
        self.utils.print_title('         Exibindo Gráfico...     ')
        print()

        sleep(2)

        plt.show()

        self.utils.clear()


# ------------ Miscelânea ---------------

# Métodos utilitários
class Utilities:

    # Limpa o console
    def clear(self):
        system("cls" if name == "nt" else "clear")

    # Imprime um texto/título entre linhas
    def print_title(self, title):
        print('-'*36)
        print(title)
        print('-'*36)

    # Exibe uma mensagem de erro
    def print_error(self, invalid_msg, error_msg):
        self.clear()
        print(f'\n{invalid_msg}:\n{error_msg}')
        print('Tente novamente')
        sleep(3)
        self.clear()


# ------------ Principal ---------------

# Programa principal, contendo a UI
class MainProgram:
    def __init__(self):
        self.func = None
        self.est_y_val = None
        self.est_x_val = None
        self.utils = Utilities()

    def main(self):

        # --------------- Menu ----------------
        while True:
            try:
                self.utils.print_title(
                    '   Calculadora de Regressão Linear    ')

                if self.func is not None:
                    print()
                    self.utils.print_title(
                        f"       {self.func['func']}         ")

                if self.func is None:
                    print('\n1 - Criar Equação dos Mínimos Quadrados')
                else:
                    print('\n1 - Alterar Equação dos Mínimos Quadrados')

                print('\n2 - Exibir Diagrama de Dispersão')

                if self.est_y_val is None:
                    print('\n3 - Estimar Valor')
                else:
                    print('\n3 - Estimar Valor ', end='')
                    print(
                        f' (Última estimativa: Y = {self.est_y_val:.2f} ',
                        end='')
                    print(f'para X = {self.est_x_val:.1f})')

                print('\n\n0 - Sair\n')

                # --- Selecionar Opção ---
                self.choice = int(input())

                self.utils.clear()

                # Criar/Alterar equação (se já existir alguma)
                if self.choice == 1:
                    self.function_class = Function()

                    self.func = self.function_class.line_min_sqr

                    self.function_class.display_function()

                # Gerar e exibir diagrama (se uma equação tiver sido inserida)
                elif self.choice == 2:
                    if self.func is None:
                        raise FunctionError

                    self.graph = Graph(self.function_class.x,
                                       self.function_class.y, self.func)

                    self.graph.display_scatter()

                # Calcular uma estimativa (caso uma função tenha sido inserida)
                elif self.choice == 3:
                    if self.func is None:
                        raise FunctionError

                    self.function_class.estimate_value()

                    self.est_y_val = self.function_class.est_y

                    self.est_x_val = self.function_class.est_x

                    self.function_class.display_estimate()

                # Sair do programa
                elif self.choice == 0:
                    self.utils.clear()
                    break
                else:
                    raise Exception

            except FunctionError:
                self.utils.print_error(
                    'Opção inválida', 'Nenhuma equação inserida')
            except Exception:
                self.utils.print_error(
                    'Opção inválida',
                    'Apenas os números 1, 2, 3 e 0 são aceitos')


# --------------------- Execução do Programa Principal ------------------------
mp = MainProgram()

mp.main()
