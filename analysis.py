import numpy as np
from scipy.optimize import curve_fit

class NonLinearFit():
    def __init__(self, x=None, y=None):
        self.maxfev = 10000
        self.nlinfunc = self.four_param_logistic_QA
        if x.any():
            beta_init = [np.min(x), np.max(x), np.mean(y), 1]
            self.params, self.params_covariance = curve_fit(self.nlinfunc, y, x, p0=beta_init, maxfev=self.maxfev)
    
    def fit(self, x, y):
        beta_init = [np.min(x), np.max(x), np.mean(y), 1]
        self.params, self.params_covariance = curve_fit(self.nlinfunc, y, x, p0=beta_init, maxfev=self.maxfev)
    
    def transform(self, y):
        fitted_predictions = self.nlinfunc(y, *self.params)
        return fitted_predictions
    
    def four_param_logistic_QA(self, x, beta1, beta2, beta3, beta4):
        return ((beta1 - beta2)/(1 + (np.exp((beta3-x)/np.abs(beta4))))) + beta2
    
    def exponential(self, x, beta1, beta2, beta3):
        return beta1 + beta2 * np.exp(beta3 * x)
    
    def affine(self, x, beta1, beta2):
        return beta1 + beta2 * x
