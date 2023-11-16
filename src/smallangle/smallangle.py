import click
import numpy as np
from numpy import pi
import pandas as pd

# Creating a group of commands with a decorator
@click.group()
def cmd_group():
    pass

# Creating a 1st command, which can be called to calculate the sin of numbers
@cmd_group.command()

# Defining the argument for the option and a default value
@click.option(
    "-n",
    "--number",
    default=10,
    show_default=True,  
)

# Function run by the sin command with fitting docstrings
def sin(number):
    """ Calculate the sin of numbers in [0-2pi] with equal intervals

    Args:
        number (int): the number of steps taken between 0 and 2pi, for which the sin will be calculated

    Returns:
        array: sin of numbers between 0 and 2pi with given number of steps
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# Creating a 2nd command, which can be called to calculate the tan of numbers
@cmd_group.command()

# Defining the argument for the option and a default value
@click.option(
    "-n",
    "--number",
    default=10,
    show_default=True, 
)

# Function run by the tan command with fitting docstrings
def tan(number):
    """ Calculate the tan of numbers in [0-2pi] with equal intervals

    Args:
        number (int): the number of steps taken between 0 and 2pi, for which the tan will be calculated

    Returns:
        array: tan of numbers between 0 and 2pi with given number of steps
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

# Calling the group of commands to "activate" those
if __name__ == "__main__":
    cmd_group()