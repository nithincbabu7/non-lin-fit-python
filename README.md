# Non Linear Fitting - Python
A plug-and-play python code for applying non-linear fitting to two lists of data, which can be further used for linear correlation analysis. Open Demo.ipynb for a demo on using the module.

## Usage
```
from analysis import NonLinearFit

# find a non-linear fit to map score2 to score1
nlinfit = NonLinearFit(score1, score2)

# use the learned fitting parameters to transform score2
fitted_score = nlinfit.transform(score2)
```
