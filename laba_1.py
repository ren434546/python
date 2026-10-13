import hashlib


def generate_file_hashes(*file_paths):
    file_hashes = {}

    for file_path in file_paths:
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            file_hashes[file_path] = sha256_hash.hexdigest()
        except FileNotFoundError:
            print(f"Ошибка: Файл '{file_path}' не найден.")
        except IOError as e:
            print(f"Ошибка ввода-вывода при чтении файла '{file_path}': {e}")

    return file_hashes


print(generate_file_hashes("apache_logs.txt"))