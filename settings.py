from pathlib import Path

# создаём переменную и указываем путь к корневой папке
ROOT_PATH = Path(__file__).parent
# создаём переменную и указываем путь к файлу json
OPERATIONS = Path.joinpath(ROOT_PATH, "src", "files", "operations.json")