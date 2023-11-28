import matplotlib.pyplot as plt
import numpy as np
from database.database import DATABASE

ypoints = np.array([1, 3, 4, 5, 8, 9, 6, 1, 3, 4, 5, 2, 4])

plt.plot(ypoints, marker='o')
plt.show()


def draw(account_id, what='calories'):
    match(what):
        case 'intake':
            pass
        case 'weight':
            pass
        case 'workout_hours':
            pass
        case 'height':
            pass
        case _:
            pass
