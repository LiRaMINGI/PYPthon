import numpy as np
from scipy.stats import multivariate_normal
import time


def logpdf_multivariate_normal(X, m, C):
    D = len(m)
    N = X.shape[0]

    det_C = np.linalg.det(C)
    C_inv = np.linalg.inv(C)

    logpdf = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C))
    for i in range(N):
        x_i = X[i]
        logpdf[i] -= 0.5 * np.dot(np.dot((x_i - m), C_inv), (x_i - m).T)

    return logpdf

N = 1000
D = 5
m = np.random.randn(D)
C = np.random.randn(D, D)
C = np.dot(C, C.T)
X = np.random.multivariate_normal(m, C, N)

start_time = time.time()
logpdf_custom = logpdf_multivariate_normal(X, m, C)
end_time = time.time()
time_custom = end_time - start_time

start_time = time.time()
logpdf_scipy = multivariate_normal.logpdf(X, mean=m, cov=C)
end_time = time.time()
time_scipy = end_time - start_time

print(f"Время работы моей функции: {time_custom:.4f} секунд")
print(f"Время работы scipy.stats.multivariate_normal.logpdf: {time_scipy:.4f} секунд")

print(f"Максимальная абсолютная ошибка: {np.max(np.abs(logpdf_custom - logpdf_scipy)):.4f}")

print(f"Моя функция: {logpdf_custom}")
print(f"Scipy.stats: {logpdf_scipy}")