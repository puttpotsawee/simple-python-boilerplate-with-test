# My Python Project

This is a simple Python project that demonstrates how to structure a Python application with a focus on testing using pytest.

## Project Structure

```
my-python-project
├── src
│   └── main.py
├── tests
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Getting Started

To get started with this boilerplate, follow these steps:

1. **Clone the repository** (if applicable):
   ```
   git clone git@github.com:puttpotsawee/simple-python-boilerplate-with-test.git .
   ```

- **(Optional) to clear up the git history** run the following command:
   ```
   rm -rf .git
   git init
   ```
   then initiate this clonned folder as a repository

2. **Install the required dependencies**:
   If you use `venv`, run this command:
   ```shell
   python -m venv .venv
   ```
   You can install the dependencies listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   To run the main script, execute the following command:
   ```
   python src/main.py
   ```

5. **Run the tests**:
   To run the tests using pytest, execute:
   ```
   pytest
   ```

## Project Description

- `src/main.py`: The main entry point of the application where the primary logic resides.
- `tests/test_main.py`: Contains test cases for the functionality implemented in `main.py`.
- `requirements.txt`: Lists the dependencies required for the project.
- `pytest.ini`: Configuration file for pytest to customize test discovery and behavior.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
