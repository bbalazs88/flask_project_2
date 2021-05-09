import numpy as np
import math

"""
this part contains the input values for the translation matrix between two reference spaces
probably inverse could be calculated as they should be invertible so one set of value / coordinate pair 
should be enough but you need to use different values e.g. between system A and B
"""

# predefined logic values
def logic_selector(logic_num):

    # from Barney to Nietzsche space
    if logic_num == 1:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = 0

        # Rotation in radian
        pitch = -0.1
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.95
        resize_y = 1
        resize_z = 0.93

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Nietzsche to Barney space
    elif logic_num == 2:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = 0

        # Rotation in radian
        pitch = 0.1
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 1.05263157894737
        resize_y = 1
        resize_z = 1.0752688172043

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Barney to BBT
    elif logic_num == 3:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = -1

        # Rotation in radian
        pitch = 0.1
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 1.1
        resize_y = 1.1
        resize_z = 1.1

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from BBT to Barney space
    elif logic_num == 4:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = 1

        # Rotation in radian
        pitch = -0.1
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.909090909
        resize_y = 0.909090909
        resize_z = 0.909090909

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from BBT to Nitzsche space
    elif logic_num == 5:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = -1

        # Rotation in radian
        pitch = 0
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.952380952
        resize_y = 0.909090909
        resize_z = 1.052631579

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Nitzsche to BBT
    elif logic_num == 6:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = 1

        # Rotation in radian
        pitch = 0
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 1.05
        resize_y = 1.1
        resize_z = 0.95

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Maya to Barney
    elif logic_num == 7:
        # translation given in number of voxels
        # tanslation

        deltax = 0
        deltay = -9  # now swapped y & z
        deltaz = 4

        # Rotation in radian
        pitch = 0
        roll = -0.01
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.97
        resize_z = 1.05
        resize_y = 0.99

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Barney to Maya
    elif logic_num == 8:

        # translation given in number of voxels
        deltax = 0
        deltay = -4  # now swapped y & z
        deltaz = 9

        # Rotation in radian
        pitch = 0
        roll = -0.07
        yaw = 0

        # zoom/scaling factor
        resize_x = 1.030927835
        resize_z = 0.980392157
        resize_y = 0.952380952  # now swapped y & z

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Nietzsche to Maya
    elif logic_num == 9:

        # translation given in number of voxels
        deltax = 0
        deltay = -6  # now swapped y & z OR NOR???
        deltaz = 10

        # Rotation in radian
        pitch = 0
        roll = 0.01
        yaw = 0

        # zoom/scaling factor
        resize_x = 1.09
        resize_z = 1.11111  # now swapped y & z or not???
        resize_y = 1.17647

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Maya to Nietzsche
    elif logic_num == 10:
        # translation given in number of voxels
        deltax = 0
        deltay = -10
        deltaz = 6

        # Rotation in radian
        pitch = 0
        roll = 0.01
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.91743119266055
        resize_y = 0.85
        resize_z = 0.9

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from BBT to Maya
    elif logic_num == 11:
        # translation given in number of voxels
        deltax = 0
        deltay = -4
        deltaz = 8

        # Rotation in radian
        pitch = 0
        roll = 0.01
        yaw = 0

        # zoom/scaling factor
        resize_x = 1.1
        resize_y = 1.05
        resize_z = 1.1

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Maya to BBT
    elif logic_num == 12:

        # translation given in number of voxels
        deltax = 0
        deltay = -8  # y and z swapped
        deltaz = 4

        # Rotation in radian
        pitch = 0
        roll = 0.02
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.909090909090909
        resize_y = 0.909090909090909  # y and z swapped
        resize_z = 0.952380952380952

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    else:
        # ide valami olyan kell, amitől meghal
        return 'Invalid logic number.'


def logic_calc(x_in, y_in, z_in, deltax_in, deltay_in, deltaz_in, pitch_in, roll_in, yaw_in,
                                    resize_x_in, resize_y_in, resize_z_in, logic):

    # Logic number
    logic = logic

    # Input of start coordinates
    x = x_in
    y = y_in
    z = z_in

    # translation given in number of voxels
    deltax = deltax_in
    deltay = deltay_in
    deltaz = deltaz_in

    #Rotation in radian
    pitch = pitch_in
    roll = roll_in
    yaw = yaw_in

    # zoom/scaling factor
    resize_x = resize_x_in
    resize_y = resize_y_in
    resize_z = resize_z_in

    # Barney to Nietzsche
    if logic == 1:
        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])

        M2 = start_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Nietzsche to Barney
    elif logic == 2:

        start_coordinate = np.array([x, y, z, 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = start_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Barney to BBT
    elif logic == 3:
        start_coordinate = np.array([x, y, z, 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = start_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # BBT to Barney
    elif logic == 4:

        start_coordinate = np.array([x, y, z, 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = start_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # BBT to Nietzsche
    elif logic == 5:
        start_coordinate = np.array([x, y, z, 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = start_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Nietzsche to BBT
    elif logic == 6:

        start_coordinate = np.array([x, y, z, 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = start_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Maya to Barney
    elif logic == 7:

        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        pitch_matrix = np.array([[-(math.sin(-1 * (math.pi / 2))), math.cos(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(-1 * (math.pi / 2)), math.sin(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 0, 1]])

        M00 = start_coordinate.dot(pitch_matrix)

        print(M00)

        yaw_matrix = np.array([[math.cos(math.pi), math.sin(math.pi), 0, 0],
                               [-(math.sin(math.pi)), math.cos(math.pi), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M01 = M00.dot(yaw_matrix)

        print(M01)

        swapped_coordinate = np.array([M01[0], M01[1], M01[2], 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = swapped_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        print(M2)

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        print(M3)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        print(M4)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        print(M5)

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Barney to Maya
    elif logic == 8:

        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        pitch_matrix = np.array([[-(math.sin(-1 * (math.pi / 2))), math.cos(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(-1 * (math.pi / 2)), math.sin(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 0, 1]])

        M00 = start_coordinate.dot(pitch_matrix)

        yaw_matrix = np.array([[math.cos(math.pi), math.sin(math.pi), 0, 0],
                               [-(math.sin(math.pi)), math.cos(math.pi), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M01 = M00.dot(yaw_matrix)

        ##########################

        swapped_coordinate = np.array([M01[0], M01[1], M01[2], 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = swapped_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Nietzsche to Maya
    elif logic == 9:

        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        pitch_matrix = np.array([[-(math.sin(-1 * (math.pi / 2))), math.cos(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(-1 * (math.pi / 2)), math.sin(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 0, 1]])

        M00 = start_coordinate.dot(pitch_matrix)

        yaw_matrix = np.array([[math.cos(math.pi), math.sin(math.pi), 0, 0],
                               [-(math.sin(math.pi)), math.cos(math.pi), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M01 = M00.dot(yaw_matrix)

        ##########################

        swapped_coordinate = np.array([M01[0], M01[1], M01[2], 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = swapped_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Maya to Nietzsche
    elif logic == 10:

        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        pitch_matrix = np.array([[-(math.sin(-1 * (math.pi / 2))), math.cos(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(-1 * (math.pi / 2)), math.sin(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 0, 1]])

        M00 = start_coordinate.dot(pitch_matrix)

        yaw_matrix = np.array([[math.cos(math.pi), math.sin(math.pi), 0, 0],
                               [-(math.sin(math.pi)), math.cos(math.pi), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M01 = M00.dot(yaw_matrix)

        swapped_coordinate = np.array([M01[0], M01[1], M01[2], 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = swapped_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # BBT to Maya
    elif logic == 11:

        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        pitch_matrix = np.array([[-(math.sin(-1 * (math.pi / 2))), math.cos(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(-1 * (math.pi / 2)), math.sin(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 0, 1]])

        M00 = start_coordinate.dot(pitch_matrix)

        yaw_matrix = np.array([[math.cos(math.pi), math.sin(math.pi), 0, 0],
                               [-(math.sin(math.pi)), math.cos(math.pi), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M01 = M00.dot(yaw_matrix)

        swapped_coordinate = np.array([M01[0], M01[1], M01[2], 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = swapped_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    # Maya to BBT
    elif logic == 12:

        # axes swaps
        start_coordinate = np.array([x, y, z, 1])
        pitch_matrix = np.array([[-(math.sin(-1 * (math.pi / 2))), math.cos(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(-1 * (math.pi / 2)), math.sin(-1 * (math.pi / 2)), 0, 0],
                                 [0, 0, 0, 1]])

        M00 = start_coordinate.dot(pitch_matrix)

        yaw_matrix = np.array([[math.cos(math.pi), math.sin(math.pi), 0, 0],
                               [-(math.sin(math.pi)), math.cos(math.pi), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M01 = M00.dot(yaw_matrix)

        swapped_coordinate = np.array([M01[0], M01[1], M01[2], 1])
        # translation

        tranlation_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [deltax, deltay, deltaz, 1]])
        M2 = swapped_coordinate.dot(tranlation_matrix)
        # Rotation in radian

        pitch_matrix = np.array([[-(math.sin(pitch)), math.cos(pitch), 0, 0],
                                 [0, 0, 1, 0],
                                 [math.cos(pitch), math.sin(pitch), 0, 0],
                                 [0, 0, 0, 1]])
        M3 = M2.dot(pitch_matrix)

        roll_matrix = np.array([[0, 0, 1, 0],
                                [math.cos(roll), math.sin(roll), 0, 0],
                                [-(math.sin(roll)), math.cos(roll), 0, 0],
                                [0, 0, 0, 1]])
        M4 = M3.dot(roll_matrix)

        yaw_matrix = np.array([[math.cos(yaw), math.sin(yaw), 0, 0],
                               [-(math.sin(yaw)), math.cos(yaw), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        M5 = M4.dot(yaw_matrix)
        # zoom/scaling

        resize_matrix = np.array([[resize_x, 0, 0, 0],
                                  [0, resize_y, 0, 0],
                                  [0, 0, resize_z, 0],
                                  [0, 0, 0, 1]])

        M6 = M5.dot(resize_matrix)

        x_out = M6[0].round(2)
        y_out = M6[1].round(2)
        z_out = M6[2].round(2)

        return x_out, y_out, z_out

    else:
        print('Error')
