import matplotlib.pyplot as plt
from time import sleep
from os import system, name


# --------------------- Classes -------------------------


# ------------ Errors ---------------

# For treating errors related to incompatible arrays
class LengthError(Exception):
    pass


# For treating errors related to a nonexistent function
class FunctionError(Exception):
    pass


# ------------ Math ---------------

# Additional math formulas
class Calculations:

    # Multiplies values from 2 arrays
    def mult_xy(self, x, y):
        return [x[i]*y[i] for i in range(len(x))]

    # Calculates the squares of values within an array
    def sqr_arr(self, arr):
        return [x**2 for x in arr]

    # Calculates the least squares function,
    # returning A, B and a string form of the function
    def calc_lea_sqr(self, sum_x, sum_y, sum_xy, sum_x2, n):
        a = round(((n * sum_xy) - (sum_x * sum_y)) /
                  ((n * sum_x2) - (sum_x**2)), 4)

        b = round((sum_y - (a * sum_x)) / n, 4)

        return {'val_a': a, 'val_b': b, 'func': f'y = {a}x + {b}'}

    # Estimates a value based on a given function
    def estimate(self, func, x):
        return (func['val_a'] * x) + func['val_b']


# Function related elements
class Function:
    def __init__(self):
        self.calc = Calculations()
        self.utils = Utilities()
        self.create_function()

    # Creates a new function
    def create_function(self):

        # Input array of X coordinates
        while True:
            try:
                print('\nList of X values:')
                self.x = [round(float(val_x), 1) for val_x in input().split()]
                self.utils.clear()
                break

            except Exception:
                self.utils.print_error(
                    'Invalid values', 'Only numbers accepted')

        # Input array of Y coordinates
        while True:
            try:
                print('\nList of Y values:')
                self.y = [round(float(val_y), 1) for val_y in input().split()]
                self.utils.clear()

                if len(self.y) != len(self.x):
                    raise LengthError

                break

            except LengthError:
                self.utils.print_error('Invalid values',
                                       'Arrays must have the same length')

            except Exception:
                self.utils.print_error(
                    'Invalid values', 'Only numbers accepted')

        # Calculations
        n = len(self.x)
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_xy = sum(self.calc.mult_xy(self.x, self.y))
        sum_x2 = sum(self.calc.sqr_arr(self.x))
        self.line_min_sqr = self.calc.calc_lea_sqr(
            sum_x, sum_y, sum_xy, sum_x2, n)

    # Estimates a value using the current function
    def estimate_value(self):
        while True:
            try:
                print(f"{self.line_min_sqr['func']}\n")
                self.est_x = float(input('Estimated value for X = '))

                self.utils.clear()

                break
            except Exception:
                self.utils.print_error(
                    'Invalid value', 'Only numbers accepted')

        self.est_y = self.calc.estimate(self.line_min_sqr, self.est_x)

        self.utils.clear()

    # Displays function in title format
    def display_function(self):
        print()
        self.utils.print_title('       Least Squares Function     ')
        print()

        print(self.line_min_sqr['func'])

        sleep(3)

        self.utils.clear()

    # Displays estimated value along function in title format
    def display_estimate(self):
        print()
        self.utils.print_title(
            f'    Estimated Value for X = {self.est_x:.1f}     ')
        print()

        print(f"{self.line_min_sqr['func']}\n")

        print(f'y = {self.est_y:.2f}')

        sleep(3)

        self.utils.clear()


# Graph related elements
class Graph:
    def __init__(self, _x, _y, _func):
        self.x = _x
        self.y = _y
        self.func = _func
        self.calc = Calculations()
        self.utils = Utilities()
        self.plot_scatter()

    # Plots scatter graph
    def plot_scatter(self):
        plt.clf()

        # Sort of centers the graph
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

    # Displays scatter graph along title
    def display_scatter(self):
        print()
        self.utils.print_title('           Showing Graph...     ')
        print()

        sleep(2)

        plt.show()

        self.utils.clear()


# ------------ Miscellaneous ---------------

# Utilily methods
class Utilities:

    # Clears console
    def clear(self):
        system("cls" if name == "nt" else "clear")

    # Prints text/title in-between lines
    def print_title(self, title):
        print('-'*36)
        print(title)
        print('-'*36)

    # Displays error message
    def print_error(self, invalid_msg, error_msg):
        self.clear()
        print(f'\n{invalid_msg}:\n{error_msg}')
        print('Try again')
        sleep(3)
        self.clear()


# ------------ Main ---------------

# Main program, containing the UI
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
                    '    Linear Regression Calculator    ')

                if self.func is not None:
                    print()
                    self.utils.print_title(
                        f"       {self.func['func']}         ")

                if self.func is None:
                    print('\n1 - Create Function')
                else:
                    print('\n1 - Change Function')

                print('\n2 - Show Graph')

                if self.est_y_val is None:
                    print('\n3 - Estimate Value')
                else:
                    print('\n3 - Estimate Value ', end='')
                    print(
                        f' (Last estimate: Y = {self.est_y_val:.2f} ', end='')
                    print(f'for X = {self.est_x_val:.1f})')

                print('\n\n0 - Exit\n')

                # --- Make selection ---
                self.choice = int(input())

                self.utils.clear()

                # Create function/Change function (if one already exists)
                if self.choice == 1:
                    self.function_class = Function()

                    self.func = self.function_class.line_min_sqr

                    self.function_class.display_function()

                # Generate and display graph (if a function has been inserted)
                elif self.choice == 2:
                    if self.func is None:
                        raise FunctionError

                    self.graph = Graph(self.function_class.x,
                                       self.function_class.y, self.func)

                    self.graph.display_scatter()

                # Calculate and display estimate
                # (if a function has been inserted)
                elif self.choice == 3:
                    if self.func is None:
                        raise FunctionError

                    self.function_class.estimate_value()

                    self.est_y_val = self.function_class.est_y

                    self.est_x_val = self.function_class.est_x

                    self.function_class.display_estimate()

                # Exit program
                elif self.choice == 0:
                    self.utils.clear()
                    break
                else:
                    raise Exception

            except FunctionError:
                self.utils.print_error(
                    'Invalid option', 'No function created')
            except Exception:
                self.utils.print_error(
                    'Invalid option', 'Only numbers 1, 2, 3 and 0 accepted')


# --------------------- Main Program Execution -------------------------
mp = MainProgram()

mp.main()
