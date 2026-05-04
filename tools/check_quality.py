from pathlib import Path
import sys

PROJECT_DIR = Path(__file__).resolve().parent.parent

FORBIDDEN_WORDS = [
    "TODO",
    "System.out.println",
    "debug"
]

JAVA_SOURCE_DIRS = [
    PROJECT_DIR / "src" / "main" / "java",
    PROJECT_DIR / "src" / "test" / "java"
]


def check_forbidden_words():
    print("\nComprobando palabras prohibidas...")

    java_files = []
    for source_dir in JAVA_SOURCE_DIRS:
        if source_dir.exists():
            java_files.extend(source_dir.rglob("*.java"))

    for file in java_files:
        content = file.read_text(encoding="utf-8")

        for word in FORBIDDEN_WORDS:
            if word in content:
                print(f"ERROR: palabra prohibida '{word}' encontrada en:")
                print(f"  {file}")
                return False

    return True


def check_tests_exist():
    print("\nComprobando existencia de tests...")

    test_dir = PROJECT_DIR / "src" / "test" / "java"

    if not test_dir.exists():
        print("ERROR: no existe la carpeta src/test/java")
        return False

    test_files = list(test_dir.rglob("*Test.java"))

    if not test_files:
        print("ERROR: no se ha encontrado ningún test Java")
        return False

    print(f"Tests encontrados: {len(test_files)}")
    return True


def main():
    checks = [
        ("No usar TODO, System.out.println ni debug", check_forbidden_words),
        ("Existencia de tests", check_tests_exist),
    ]

    for name, check in checks:
        print(f"\n=== {name} ===")
        if not check():
            print(f"\nCommit bloqueado por: {name}")
            sys.exit(1)

    print("\nTodas las comprobaciones han pasado.")
    sys.exit(0)


if __name__ == "__main__":
    main()