from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg


def main() -> None:
    matrix = np.array([[2.0, 1.0], [1.0, 2.0]])
    eigenvalues = linalg.eigvals(matrix)
    x = np.linspace(0.0, 2.0 * np.pi, 200)
    y = np.sin(x)

    figure_path = Path("experiments") / "scientific_stack_smoke_test.png"
    figure_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label="sin(x)")
    plt.title("Scientific Stack Smoke Test")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(figure_path)
    plt.close()

    print("NumPy mean:", float(np.mean(y)))
    print("SciPy eigenvalues:", [complex(value) for value in eigenvalues])
    print("Matplotlib output:", figure_path.resolve())


if __name__ == "__main__":
    main()
