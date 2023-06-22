# Non Linear Fitting - Python
A plug-and-play python code for applying non-linear fitting to two lists of data, which can be further used for linear correlation analysis. Open Demo.ipynb for a demo on using the module.

## Usage
'''
# find a non-linear fit to map score1 to score2
nlinfit = NonLinearFit(score1, score2)

# use the learnt fitting parameters to trensform score1
fitted_score = nlinfit.transform(score2)
'''
