# Standard library
import random

# Third-party libraries
from matplotlib import pyplot as plt
from matplotlib.cm import Dark2

# Custom modules
from thread_plot import thread_plot

def get_data(k, max_len, choices):
    data = []
    for i in range(k):
        value = ''
        for j in range(random.randint(2, max_len)):
            value += random.choice(choices)
        data.append(value)
    return data


if __name__ == '__main__':
    choices = 'ABCDEFGH'
    data = get_data(1000, 6, choices)

    # We need to make a color choice for each letter in the sequence
    cm = plt.get_cmap('Dark2')
    colors = dict([(choices[i], cm(1.*i/len(choices))) for i in range(len(choices))])

    # Make the plot
    fig, ax = plt.subplots(1)
    thread_plot(ax, colors, data)

    # Since we're using patches (rectangles), Matplotlib doesn't know about our legend, so we have
    # to generate some fake data to force the legend to appear properly
    markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in colors.values()]
    plt.legend(markers, colors.keys(), numpoints=1, bbox_to_anchor=(1.05, 1))
    plt.tight_layout()

    plt.show()

