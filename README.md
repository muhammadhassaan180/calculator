# Calculator

A command-line calculator with seven arithmetic operations, built for Programming Fundamentals at SSUET. This started as my first self-written program and was later improved with a menu, input validation, and error handling.

## Features

- **Seven operations:** add, subtract, multiply, divide, power, modulus, and floor division
- **Interactive menu:** choose one operation at a time; type `quit` to exit
- **Float input:** handles whole numbers and decimals
- **Input validation:** invalid operations and non-numeric input don't crash the program
- **Division-by-zero handling:** divide, modulus, and floor division show a clear error
- **Clean output:** prints the full expression, e.g. `10 + 2 = 12`
- **One function per operation:** each returns a result; `main()` handles the menu and output

## How to Run

```bash
python3 calculator.py
```

Example:

```
Enter the function you want to perform (...): add
Enter first number: 10
Enter second number: 2
10 + 2 = 12
```

## What I Learned

1. **Functions:** one function per operation, with parameters and return values
2. **Loops and menus:** keeping the calculator running until the user quits
3. **Exception handling:** `try/except` for `ValueError` and `ZeroDivisionError`
4. **Input validation:** rejecting invalid operations and non-numeric input without crashing
5. **Separation of concerns:** functions calculate; `main()` handles input and output
6. **Arithmetic operators:** `+ - * / ** % //`, including the difference between division, floor division, and modulus

---

*My first university project — Software Engineering at SSUET. Originally a basic functions exercise; later improved with a menu, validation, and error handling.*
