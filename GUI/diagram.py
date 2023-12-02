import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO


# draw a figure based on the input data, return image as bytes


def draw(account_id, measure, data, label=None) -> bytes:
    if not label:
        data = np.array(data)
        memory_file = BytesIO()
        plt.title(account_id)
        plt.ylabel(measure)
        plt.plot(data, marker='o')
        plt.savefig(memory_file, format='png')
        data = memory_file.getvalue()
        return data
    else:
        pass
