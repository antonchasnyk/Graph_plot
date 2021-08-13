import matplotlib.pyplot as plt
import numpy as np
import argparse


def make_plot(filename: str, image_file: str):
    with open('traces.txt', 'r') as inp_file:
        axes = '#'
        while axes.startswith('#'):
            axes = inp_file.readline()
        axes = axes.split('/')
        splitted = inp_file.read().split()
        x = np.array(np.float64(splitted[0::3]))
        teoretical = np.array(np.float64(splitted[1::3]))
        measurements = np.array(np.float64(splitted[2::3]))

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        ax1.plot(x, teoretical, label=axes[3].strip().capitalize())
        ax1.plot(x, measurements, label=axes[4].strip().capitalize())
        ax1.set(xlabel=axes[0].strip(), ylabel=axes[1].strip())
        ax1.legend(loc=axes[5].strip().lower(), shadow=True,
                   fontsize=axes[6].strip().lower())
        ax1.grid()

        ax2.plot(x, teoretical - measurements)
        ax2.set(xlabel=axes[0].strip(), ylabel=axes[2].strip())
        ax2.grid()

        fig.savefig(image_file)
        plt.show()


if __name__ == '__main__':
    DESCRIPTION = 'Plot comparision of two graph'
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('filename', metavar='FILE', type=str,
                        help='a file name with data')
    parser.add_argument('image_name', metavar='PICTURE', type=str, nargs='?',
                        default='fig.png', help='an image file name')
    args = parser.parse_args()
    if args.filename:
        make_plot(args.filename, args.image_name)
