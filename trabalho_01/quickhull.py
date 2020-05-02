from util import fetch_input


def triangle_area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3 
    return abs(0.5 * (((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1))))

def quickhull(inpt):
    outpt = [ element for element in inpt ]

    top_futhest, bottom_furthest, right_furthest, left_furthest = inpt[0], inpt[0], inpt[0], inpt[0]
    for coord in inpt:
        if top_futhest[1] < coord[1]:
            top_futhest = coord
        elif bottom_furthest[1] > coord[1]:
            bottom_furthest = coord
        elif right_furthest[0] < coord[0]:
            right_furthest = coord
        elif left_furthest[0] > coord[0]:
            left_furthest = coord
    
    for i in range(len(inpt)):
        coord = outpt[i]
        if coord[1] < top_futhest[1] and coord[1] > bottom_furthest[1] and coord[0] > left_furthest[0] and coord[0] < right_furthest[0]:
            del outpt[i]
    
    q1 = points_in_quadrant_right_left(top_futhest, right_furthest, outpt)
    q3 = points_in_quadrant_left_right(top_futhest, left_furthest, outpt)
    q3 = points_in_quadrant_left_right(left_furthest, bottom_furthest, outpt)
    q4 = points_in_quadrant_right_left(right_furthest, bottom_furthest, outpt)


    t1 = biggest_triangle(top_futhest, right_furthest, q1)
    to_del = []
    for i in range(len(q1)):
        if is_point_inside_triangle(q1[i], t1[0], t1[1], t1[2]):
            to_del.append(i)
    for i in to_del:
        del t1[i]

def teste(p1, p2, ps):
    q1 = points_in_quadrant_right_left(p1, p2, ps)
    t1 = biggest_triangle(p1, p2, q1)
    to_del = []
    for i in range(len(q1)):
        if is_point_inside_triangle(q1[i], t1[0], t1[1], t1[2]):
            to_del.append(i)
    for i in to_del:
        del q1[i]
    
    return [ teste() t1[2]]
    
    

def is_point_inside_triangle(p, p1, p2, p3):
    sign = lambda pp1, pp2, pp3: (pp1[0] - pp3[0]) * (pp2[1] - pp3[1]) - (pp2[0] - pp3.x) * (pp1[1] - pp3[1])

    d1 = sign(p, p1, p2)
    d2 = sign(p, p2, p3)
    d3 = sign(p, p3, p1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0);
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0);

    return not (has_neg and has_pos);

def biggest_triangle(p1, p2, ps):
    fp = ps[0]
    bta = 0
    for p in ps:
        ta = triangle_area(p1, p2, p)
        if bta < ta:
            bta = ta
            fp = p
    return (p1, p2, fp)

def points_in_quadrant_right_left(p1, p2, ps):
    result = []
    for i in range(len(ps)):
        coord = ps[i]
        if coord[1] < p1[1] and coord[1] > p2[1] and coord[0] > p2[0] and coord[0] < p1[0]:
            result.append(coord)
    return result
    
def points_in_quadrant_left_right(p1, p2, ps):
    result = []
    for i in range(len(ps)):
        coord = ps[i]
        if coord[1] < p1[1] and coord[1] > p2[1] and coord[0] > p1[0] and coord[0] < p2[0]:
            result.append(coord)
    return result
        



# input_arr = fetch_input('input_data')
# for inpt in input_arr:
#     quickhull_result = quickhull(inpt)
#     print('Output: {}'.format('N' if len(quickhull_result) is len(inpt) else 'S'))
#     input('Press enter to continue...') 
