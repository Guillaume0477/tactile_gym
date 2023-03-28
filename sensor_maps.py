import numpy as np
from matplotlib import pyplot as plt

# CONSTANTS
sensors = ['digit', 'digitac', 'tactip']
sides = ['forward', 'right_angle', 'standard', 'mini_right_angle', 'flat']
parts = ['border_mask', 'nodef_dep', 'nodef_gray']


def sensors_map(side):

    size = '/680x480/'

    plt.figure()

    for i in range(len(sensors)):
        sensor = sensors[i]
        for j in range(len(parts)):
            part = parts[j]

            if (sensor != 'tactip' and (side in ['mini_right_angle', 'flat'])):
                break

            if sensor == 'tactip':
                size = '/256x256/'

            path = 'tactile_gym/assets/robot_assets/' + sensor + \
                '/reference_images/' + side + size + part + '.npy'
            img_array = np.load(path)

            plot_nmb = (i + 1) + j * 3
            print(plot_nmb, sensor, side, part)
            plt.subplot(3, 3, plot_nmb)
            plt.title(sensor + " " + side + " " + part)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(img_array, cmap='gray')

    plt.show()


def tactip_only():
    sensor = 'tactip'
    sides = ['mini_right_angle', 'flat']
    size = '/256x256/'

    plt.figure()

    for i in range(len(sides)):
        side = sides[i]
        for j in range(len(parts)):
            part = parts[j]

            path = 'tactile_gym/assets/robot_assets/' + sensor + \
                '/reference_images/' + side + size + part + '.npy'
            img_array = np.load(path)

            plot_nmb = (i + 1) + j * 2
            print(plot_nmb, sensor, side, part)
            plt.subplot(3, 2, plot_nmb)
            plt.title(sensor + " " + side + " " + part)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(img_array, cmap='gray')

    plt.show()


def digitac_only():
    sensor = 'digitac'
    sides = ['forward', 'right_angle', 'standard']
    size = '/680x480/'

    plt.figure()

    for i in range(len(sides)):
        side = sides[i]
        for j in range(len(parts)):
            part = parts[j]

            path = 'tactile_gym/assets/robot_assets/' + sensor + \
                '/reference_images/' + side + size + part + '.npy'
            img_array = np.load(path)

            plot_nmb = (i + 1) + j * 3

            plt.subplot(3, 3, plot_nmb)
            plt.title(sensor + " " + side + " " + part)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(img_array, cmap='gray')

    plt.show()


side = 'forward'
# side = 'right_angle'
# side = 'standard'

# digitac_only()
# sensors_map(side)
# tactip_only()
