import numpy as np
from scipy import stats

# Dataset of the Employees Salary 
salaries = [25000, 28000, 30000, 32000, 35000, 37000, 40000, 42000, 45000, 150000]

# Mean of the Employees Salary
Mean_Salary = np.mean(salaries)
print("Mean Salary:", Mean_Salary)


# Median of the Employees Salary
Median_Salary = np.median(salaries)
print("Median Salary:", Median_Salary)

# Mode of the Employees Salary 
Mode_Salary = stats.mode(salaries, keepdims=True)
print("Mode Salary:", Mode_Salary.mode)