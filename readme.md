# Professional Calculator

A simple and interactive command-line calculator built with Python.

Professional Calculator supports basic arithmetic, powers, percentages, and square roots through a terminal-based interface.

---

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Power / Exponentiation
* Percentage calculations
* Square root
* Open and exit controls
* Division-by-zero protection
* Invalid operation handling
* Calculator can be reopened without restarting the program

---

## Built With

* Python 3
* Standard Python libraries only
* No external dependencies

---

## Supported Operations

| Operation | Description    | Example          |
| --------- | -------------- | ---------------- |
| `+`       | Addition       | `10 + 5 = 15`    |
| `-`       | Subtraction    | `10 - 5 = 5`     |
| `*`       | Multiplication | `10 * 5 = 50`    |
| `/`       | Division       | `10 / 5 = 2`     |
| `^`       | Power          | `2 ^ 3 = 8`      |
| `%`       | Percentage     | `20% of 50 = 10` |
| `√`       | Square root    | `√25 = 5`        |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Professional-Calculator.git
```

### 2. Navigate to the Project

```bash
cd Professional-Calculator
```

### 3. Run the Calculator

```bash
python calculator.py
```

Replace `calculator.py` with your actual Python filename if it is different.

---

## Usage

When the program starts, you will see:

```text
welcome to Calculator! type /open/ to start and /exit/ to turn off
```

Type:

```text
open
```

to start the calculator.

Then choose an operation:

```text
enter operation(+, -, *, /, ^, % and √(square root) or 'exit' ):
```

For example:

```text
enter operation(+, -, *, /, ^, % and √(square root) or 'exit' ): +
enter first number : 25
enter second number : 15

25.0 + 15.0 = 40.0
```

---

## Project Structure

```text
Professional-Calculator/
│
├── calculator.py
└── README.md
```

---

## How It Works

The calculator is organized into separate functions for different operations:

* `basic_operation()` handles addition, subtraction, multiplication, and division.
* `power()` calculates powers and exponents.
* `sqrt()` calculates square roots.
* `persentage()` calculates percentages.
* `exit_open_function()` manages the calculator's open and exit states.
* `main()` controls the main program loop.

Separating the functionality into different functions makes the code easier to understand and maintain.

---

## Current Limitations

The project currently operates through the command line.

Possible improvements include:

* Better error handling for invalid number input
* Calculation history
* More mathematical functions
* Improved terminal interface
* Scientific calculator mode
* GUI version
* Improved percentage output
* Unit testing

---

## Future Plans

The project can be expanded into a more complete scientific calculator.

```text
Basic arithmetic
Powers
Square roots
Calculation history
Trigonometric functions
Logarithms
Factorials
Scientific notation
GUI
```

## Author

Created as a Python programming project focused on practicing:

* Functions
* Conditional statements
* Loops
* User input
* Error handling
* Program structure
* Mathematical operations
