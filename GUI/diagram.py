import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from web.auth import fetch_account

# draw a figure based on the input data, return image as bytes


def draw(account_id, measure) -> bytes:
    data = fetch_account(account_id)['msg'][measure]
    data = np.array(data)
    memory_file = BytesIO()
    plt.title(account_id)
    plt.ylabel(measure)
    plt.plot(data, marker='o')
    plt.savefig(memory_file, format='png')
    data = memory_file.getvalue()
    plt.clf()
    return data


def draw_all(account_id):
    try:
        data = fetch_account(account_id)['msg']
        # print(data)
        memory_file = BytesIO()
        plt.title(account_id)
        # print(data['BMI'], data['calorie'], data['height'],
        #       data['weight'], data['duration'])
        plt.plot(data['BMI'], data['calorie'], data['height'],
                 data['weight'], data['duration'])
        plt.savefig(memory_file, format='png')
        plt.clf()
        data = memory_file.getvalue()
        return data
    except:
        return b''
