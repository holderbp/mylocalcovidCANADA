# mylocalcovidCANADA

## Setup

### Run the code

You will need to install the app's dependencies in a virtual envrionment to be able to run the app.

1. In a terminal shell, navigate to the directory where you would like to clone this repo, e.g., ``cd ~/Documents/Projects``.

2. Clone the repo using the following command:
```
git clone https://github.com/holderbp/mylocalcovidCANADA.git
```

3. Navigate into the new directory ``mylocalcovidCANADA`` and use one of the following two options to establish a virtual environment.
- **Python Virtual Environment** 
```
python -m venv portal_env
source portal_env/bin/activate  # Windows: \portal_env\scripts\activate
pip install -r requirements_venv_portal.txt
```
(This assumes you are running Python 3. If ``python --version`` returns, e.g., 2.7.*, then try ``python3 -m venv portal_env``, or install Python 3). To deactivate your python environment, use the shell command ``deactivate``.
- **Conda Environment** 
```
conda env create -f requirements_conda_portal.yml
```
and then activate it before running the portal app
```bash
conda activate portal
```
If the ``.yml`` environment file is updated, then update your conda environment with
```
conda env update -f requirements_conda_portal.yml --prune
```
(This assumes an installation of, e.g., ``miniconda``). To deactivate your conda environment, use ``conda deactivate``.

4. Run the portal app using: ```python covid_portal_app.py```

5. You should now see the app running at: http://localhost:8050/

---
*Copied from @jolenezheng's [COVIDDashboard](https://github.com/jolenezheng/COVIDDashboard) on 2021-10-26. Written and maintained by: Jolene Zheng (Waterloo), Shafika Olalekan Koiki (Waterloo), and Ben Holder (GVSU)*

