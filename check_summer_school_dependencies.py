#!/usr/bin/env python3
"""Dependency check for Imperial Summer School Lectures 7--12 and Problem Class 2.

Run from a terminal with:

    python check_summer_school_dependencies.py

The script checks imports, prints versions, and runs tiny smoke tests for
scikit-learn, matplotlib, and PyTorch. It does not require a GPU.
"""
from __future__ import annotations

import importlib
import platform
import subprocess
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class PackageCheck:
    import_name: str
    pip_name: str
    required: bool = True
    note: str = ""


PACKAGES = [
    PackageCheck("numpy", "numpy"),
    PackageCheck("scipy", "scipy"),
    PackageCheck("pandas", "pandas"),
    PackageCheck("matplotlib", "matplotlib"),
    PackageCheck("sklearn", "scikit-learn"),
    PackageCheck("PIL", "pillow"),
    PackageCheck("torch", "torch"),
    PackageCheck("IPython", "ipython"),
    PackageCheck("jupyterlab", "jupyterlab"),
    PackageCheck("notebook", "notebook"),
    PackageCheck("ipykernel", "ipykernel"),
    PackageCheck("nbformat", "nbformat", note="needed if regenerating or editing notebooks programmatically"),
]


def get_version(module) -> str:
    for attr in ("__version__", "VERSION"):
        if hasattr(module, attr):
            v = getattr(module, attr)
            return str(v() if callable(v) else v)
    return "installed"


def check_imports():
    print("=" * 72)
    print("Python environment")
    print("=" * 72)
    print("Python:", sys.version.replace("\n", " "))
    print("Executable:", sys.executable)
    print("Platform:", platform.platform())
    print()

    if sys.version_info < (3, 10):
        print("WARNING: Python 3.10+ is recommended for these notebooks.")
        print()

    missing = []
    print("=" * 72)
    print("Package imports")
    print("=" * 72)
    for pkg in PACKAGES:
        try:
            module = importlib.import_module(pkg.import_name)
            version = get_version(module)
            extra = f" — {pkg.note}" if pkg.note else ""
            print(f"[OK]      {pkg.pip_name:<15} import `{pkg.import_name}`  version: {version}{extra}")
        except Exception as exc:  # noqa: BLE001 - broad on purpose for environment diagnostics
            status = "MISSING" if pkg.required else "OPTIONAL MISSING"
            print(f"[{status}] {pkg.pip_name:<15} import `{pkg.import_name}` failed: {exc}")
            if pkg.required:
                missing.append(pkg.pip_name)
    print()
    return missing


def smoke_tests() -> bool:
    print("=" * 72)
    print("Smoke tests")
    print("=" * 72)
    ok = True

    try:
        from sklearn.datasets import load_digits
        from sklearn.decomposition import PCA
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import make_pipeline

        digits = load_digits()
        X = digits.data / 16.0
        y = digits.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0, stratify=y
        )
        pipe = make_pipeline(PCA(n_components=10, random_state=0), LogisticRegression(max_iter=1000))
        pipe.fit(X_train, y_train)
        acc = pipe.score(X_test, y_test)
        print(f"[OK] scikit-learn digits + PCA + logistic regression smoke test. Accuracy: {acc:.3f}")
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[FAIL] scikit-learn smoke test failed: {exc}")

    try:
        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(0, 1, 5)
        fig, ax = plt.subplots()
        ax.plot(x, x**2)
        plt.close(fig)
        print("[OK] matplotlib plotting smoke test.")
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[FAIL] matplotlib smoke test failed: {exc}")

    try:
        import torch
        from torch import nn

        torch.manual_seed(0)
        model = nn.Sequential(nn.Linear(4, 3), nn.ReLU(), nn.Linear(3, 2))
        x = torch.randn(8, 4)
        y = torch.randint(0, 2, (8,))
        loss_fn = nn.CrossEntropyLoss()
        logits = model(x)
        loss = loss_fn(logits, y)
        loss.backward()
        print(f"[OK] PyTorch forward/backward smoke test. Loss: {loss.detach().item():.3f}")
        print("     CUDA available:", torch.cuda.is_available(), "(GPU is not required)")
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[FAIL] PyTorch smoke test failed: {exc}")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "jupyter", "--version"],
            text=True,
            capture_output=True,
            timeout=20,
            check=False,
        )
        if result.returncode == 0:
            first_line = result.stdout.strip().splitlines()[0] if result.stdout.strip() else "available"
            print(f"[OK] Jupyter command-line smoke test: {first_line}")
        else:
            ok = False
            print("[FAIL] Jupyter command-line test failed:")
            print(result.stderr.strip() or result.stdout.strip())
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[FAIL] Jupyter command-line smoke test failed: {exc}")

    print()
    return ok


def main() -> int:
    missing = check_imports()
    if missing:
        print("Install missing packages with:")
        print("  python -m pip install " + " ".join(missing))
        print()
        print("Or install everything from requirements with:")
        print("  python -m pip install -r summer_school_requirements.txt")
        print()
        return 1

    ok = smoke_tests()
    if ok:
        print("All dependency checks passed. The notebooks should be ready to run locally.")
        return 0

    print("Some smoke tests failed. Check the messages above.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
