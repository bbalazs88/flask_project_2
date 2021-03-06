import numpy as np
import math

# this part contains the input values for the translation matrix between two reference spaces
# probably inverse could be calculated as they should be invertible so one set of value / coordinate pair should be enough but you need to use different values
# e.g. between system A and B

def logic_selector(logic_num):

    # from Barney to Nietzsche space
    if logic_num == 1:
        # translation given in number of voxels
        deltax = 0
        deltay = 0
        deltaz = 0

        # Rotation in radian
        pitch = 0.1
        roll = 0
        yaw = 0

        # zoom/scaling factor
        resize_x = 0.95
        resize_y = 1
        resize_z = 0.93

        return deltax, deltay, deltaz, pitch, roll, yaw, resize_x, resize_y, resize_z

    # from Nietzsche to Barney space
    if logic_num == 2:
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

    # from Barney to T1w_BBT_template_all beagle dogsspace
    if logic_num == 3:
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

    # from T1w_BBT_template_all beagle dogs to Barney space
    if logic_num == 4:
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

    # from T1w_BBT_template_all beagle dogs to Nitzsche space
    if logic_num == 5:
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

    # from Nitzsche to T1w_BBT_template_all beagle dogs space
    if logic_num == 6:
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

    else:
        # ide valami olyan kell, amitől meghal
        return 'Invalid logic number.'


def logic_calc(x_in, y_in, z_in, deltax_in, deltay_in, deltaz_in, pitch_in, roll_in, yaw_in,
                                    resize_x_in, resize_y_in, resize_z_in):

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

    start_coordinate=np.array([x, y, z, 1])
    # translation

    tranlation_matrix = np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [deltax, deltay, deltaz, 1]])
    M2 = start_coordinate.dot(tranlation_matrix)

    #Rotation in radian

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

    yaw_matrix = np.array([[math.cos(yaw),math.sin(yaw), 0, 0],
                         [-(math.sin(yaw)),math.cos(yaw),0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    M5 = M4.dot(yaw_matrix)


    # zoom/scaling

    resize_matrix = np.array([[resize_x, 0, 0, 0],
                               [0, resize_y, 0, 0],
                               [0, 0, resize_z, 0],
                               [0, 0, 0, 1]])

    M6 = M5.dot(resize_matrix)

    x_out = M6[0]
    y_out = M6[1]
    z_out = M6[2]

    return x_out, y_out, z_out

    """
    # if you want to round them to integer
    print('output coordinates \nx:'+ str(np.rint(M6[0]).astype('int')))
    print('y:'+ str(np.rint(M6[1]).astype('int')))
    print('z:'+ str(np.rint(M6[2]).astype('int')))
    """