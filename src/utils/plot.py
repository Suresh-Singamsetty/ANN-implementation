import pandas as pd
import matplotlib.pyplot as plt
import os
import time


def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S_{filename}")
    return unique_filename


def save_plot(loss_acc, plot_name, plot_dir):
    unique_filename = get_unique_filename(plot_name)
    path_to_plot = os.path.join(plot_dir, unique_filename)
    pd.DataFrame(loss_acc).plot(figsize=(10, 7))
    plt.grid(True)
    plt.savefig(path_to_plot)
