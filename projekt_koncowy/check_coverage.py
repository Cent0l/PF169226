import subprocess

def run_coverage():
    print("==> Sprawdzanie pokrycia testami dla folderów 'src/' oraz 'tests/'...\n")
    subprocess.run(
        ["pytest", "--cov=src", "--cov=tests", "--cov-report=term", "tests/"]
    )

if __name__ == "__main__":
    run_coverage()
