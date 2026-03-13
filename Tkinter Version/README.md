# LBM Fluid Simulator (Tkinter Version)

A Tkinter-based Lattice Boltzmann Method (LBM) fluid dynamics simulator.

## Setting Up the Environment

It is recommended to use a virtual environment to manage dependencies for this project.

**1. Create a virtual environment:**

```bash
python3 -m venv .venv-tkinter
```

**2. Activate the virtual environment:**

*   **Linux/macOS:**
    ```bash
    source venv/bin/activate
    ```
*   **Windows:**
    ```powershell
    .\venv\Scripts\Activate
    ```

## Installation

**1. Install system dependencies (Linux only):**

On many Linux distributions (like Ubuntu/Debian), `tkinter` is not included with Python by default and must be installed via the package manager:

```bash
sudo apt-get update
sudo apt-get install python3-tkinter
```

**2. Install Python dependencies:**

Once your virtual environment is active and system dependencies are installed, proceed to install the required Python libraries:

```bash
pip install numpy matplotlib
```

## Running the Application

To launch the simulator, run the `main.py` script:

```bash
python main.py
```

### Language Selection

You can specify the language at startup using the `--lang` or `-l` command-line argument.

**Supported Languages:**
*   `zh` (Chinese - Default)
*   `en` (English)
*   `es` (Spanish)

**Examples:**

Launch in English:
```bash
python main.py --lang en
```

Launch in Spanish:
```bash
python main.py -l es
```

Launch in Chinese (default):
```bash
python main.py
```

You can also change the language dynamically from the "Language" menu in the application.
