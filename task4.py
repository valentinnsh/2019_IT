import matplotlib.pyplot as plt
import numpy as np


def gen_input_data(n, m, sp):
    X = sp*np.random.random_sample((n, m)) - sp/2
    return X


def in_pareto_front(ind, X):
    for i, element in enumerate(X):
        if i != ind and not np.any(element < X[ind:]):
            return False
    return True


if __name__ == "__main__":

    m = 3   # number of axis
    n = 7   # total vector num
    sp = 100  # scale param
    X = gen_input_data(n, m, sp)

    front_ind = []
    for i in range(X.shape[0]):
        if in_pareto_front(i, X):
            front_ind.append(i)

    pareto = X[front_ind, :]
    ax_plt_angle = 2 * np.pi * np.arange(m + 1) / m

    a, axes = plt.subplots(ncols=2, subplot_kw=dict(polar=True))

    axes[0].set_title('Pareto front')
    for vec in pareto:
        axes[0].plot(ax_plt_angle, np.append(vec, vec[0]))

    axes[1].set_title('All vectors')
    for vec in X:
        axes[1].plot(ax_plt_angle, np.append(vec, vec[0]))

    plt.show()
