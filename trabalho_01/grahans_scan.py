from functools import cmp_to_key
from matplotlib import pyplot as plt
from util import fetch_input


def plot(original_input, sup_ec, inf_ec):
    f1 = plt.figure(1)
    plt.scatter(x=[ element[0] for element in original_input ], y=[ element[1] for element in original_input ])
    f1.show()

    f2 = plt.figure(2)
    plt.scatter(x=[ element[0] for element in sup_ec ], y=[ element[1] for element in sup_ec ], c='red')
    plt.scatter(x=[ element[0] for element in inf_ec ], y=[ element[1] for element in inf_ec ], c='blue')
    f2.show()

def vetorial_product(arr):
    (x1, y1), (x2, y2), (x3, y3) = arr[0], arr[1], arr[2]
    result = ((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1))
    return result

def is_curve_to_the_right(arr):
    return vetorial_product(arr) < 0.000001

def is_curve_to_the_left(arr):
    return vetorial_product(arr) > 0.000001

def grahans_scan(inpt):
    sorted_input = sorted(inpt, key=cmp_to_key(lambda i1, i2: i1[0] - i2[0] if i1[0] - i2[0] is not 0 else i1[1] - i2[1]))

    sup_ec = [ sorted_input[0], sorted_input[1] ]
    for i in range(2, len(sorted_input), 1):
        sup_ec.append(sorted_input[i])
        while len(sup_ec) > 2 and is_curve_to_the_left([ sup_ec[-3], sup_ec[-2], sup_ec[-1] ]):
            del sup_ec[-2]
    
    inf_ec = [ sorted_input[-1], sorted_input[-2] ]
    for i in range(len(sorted_input) - 3, -1, -1):
        inf_ec.append(sorted_input[i])
        while len(inf_ec) > 2 and is_curve_to_the_left([ inf_ec[-3], inf_ec[-2], inf_ec[-1] ]):
            del inf_ec[-2]
    
    del sup_ec[-1]
    del inf_ec[-1]
    
    plot(sorted_input, sup_ec, inf_ec)
    
    return inf_ec + sup_ec


input_arr = fetch_input('input_data')
for inpt in input_arr:
    grahans_scan_result = grahans_scan(inpt)
    print('Output: {}'.format('N' if len(grahans_scan_result) is len(inpt) else 'S'))
    input('Press enter to continue...')
