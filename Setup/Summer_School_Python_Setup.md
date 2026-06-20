# Python Setup for the Summer School Notebooks

This document explains how to set up Python locally for the Lecture 7--12 companion notebooks and the Problem Class 2 tutorial notebook.

The notebooks should also work in Google Colab. To use Google Colab:

1. Open https://colab.research.google.com/.
2. Upload the notebook file.
3. Run the notebook in the browser.

Google Colab usually has the main packages installed already, including NumPy, scikit-learn, Matplotlib, and PyTorch.

These following instructions are for students who want to run the code on their own laptop instead.

## 1. What you need

You should have:

- **Python 3.10 or newer.**  
  To check whether Python is already installed, open a terminal or command prompt and run:

  ```bash
  python --version
  ```
  
  On MacOS you may need to run:
  
  ```bash
  python3 --version
  ```
  
  If you do not already have Python 3.10 or newer, download it from the [official Python website](https://www.python.org/downloads/). On Windows, tick the box “Add Python to PATH” during installation.
  
- **A working terminal or command prompt**
- **The course notebooks**, for example `.ipynb` files
- **The requirements file** `summer_school_requirements.txt`
- **The dependency checker** `check_summer_school_dependencies.py`

A GPU is **not required**. The neural network examples are small and should run on CPU.

## 2. Required Python packages

The notebooks use the following packages:

```text
numpy
scipy
pandas
matplotlib
scikit-learn
pillow
torch
ipython
jupyterlab
notebook
ipykernel
nbformat
```

What these are used for:

| Package | Used for |
|---|---|
| `numpy` | arrays, numerical computation |
| `scipy` | scientific computing utilities used by some ML tools |
| `pandas` | small result tables and summaries |
| `matplotlib` | plots and figures |
| `scikit-learn` | datasets, PCA, logistic regression, train/test splits, metrics |
| `pillow` | image and GIF handling |
| `torch` | PyTorch neural networks |
| `ipython` | notebook display utilities |
| `jupyterlab`, `notebook`, `ipykernel` | running Jupyter notebooks locally |
| `nbformat` | notebook utilities/checking |

## 3. Recommended installation using a virtual environment

Open a terminal in the folder where you have saved the course files.

### macOS / Linux

Create a virtual environment:

```bash
python3 -m venv summer-school-env
```

Activate it:

```bash
source summer-school-env/bin/activate
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

Install the dependencies:

```bash
python -m pip install -r summer_school_requirements.txt
```

### Windows PowerShell

Create a virtual environment:

```powershell
py -m venv summer-school-env
```

Activate it:

```powershell
.\summer-school-env\Scripts\Activate.ps1
```

If Windows blocks the activation script, you may need to run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate the environment again:

```powershell
.\summer-school-env\Scripts\Activate.ps1
```

Upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Install the dependencies:

```powershell
python -m pip install -r summer_school_requirements.txt
```

## Alternative: install directly without a virtual environment

If you are comfortable installing packages directly into your usual Python environment, run:

```bash
python -m pip install numpy scipy pandas matplotlib scikit-learn pillow torch ipython jupyterlab notebook ipykernel nbformat
```

Using a virtual environment is recommended because it keeps the course setup separate from other Python projects.

## 4. Check that everything works

After installation, run the dependency checker:

```bash
python check_summer_school_dependencies.py
```

The script checks that the required packages can be imported and runs small tests for:

- NumPy
- scikit-learn
- Matplotlib
- PyTorch forward and backward passes
- Jupyter-related packages

If everything is installed correctly, the script should finish with a success message.

## 5. Launch Jupyter

Once the dependency check passes, start JupyterLab with:

```bash
jupyter lab
```

or start the classic notebook interface with:

```bash
jupyter notebook
```

Your browser should open automatically. From there, open the `.ipynb` notebook file you want to run.

## 6. Running the notebooks

For each notebook:

1. Open the notebook in Jupyter.
2. Run the first few setup/import cells.
3. If an import error appears, check that your environment is activated.
4. Run the notebook from top to bottom.

The neural network notebooks may take a few seconds to a few minutes on CPU, depending on your laptop. They do not require a GPU.

## 7. Deactivating the virtual environment

When you are finished working, you can leave the virtual environment by running:

```bash
deactivate
```
To resume work later, reactivate the environment using the activate command from section 3.

## 8. Checklist

Before the tutorial, make sure you can do all of the following:

- [ ] Open a terminal or command prompt.
- [ ] Run `python --version` and see Python 3.10 or newer.
- [ ] Install packages using `summer_school_requirements.txt`.
- [ ] Run `python check_summer_school_dependencies.py` successfully.
- [ ] Launch Jupyter with `jupyter lab` or `jupyter notebook`.
- [ ] Open and run the first few cells of a course notebook.
