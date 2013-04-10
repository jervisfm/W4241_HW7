from math import ceil

__author__ = 'Jervis Muindi'


def f(x):
    if 0 <= x <= 0.5:
        return x
    elif 0.5 <= x <= 1.0:
        return 1 - x
    else:
        print "Error: undefined input %f" % x
        return 0


def u(x, k):
    return 0.5 * (f(x - k) + f(x + k))

def u_forward(x, t, k, h):
    """
     Let us move forward in time
     x - the current x point
     t - the current time
     k - the delta in time to go forwards
     h - the delta in x-pts (i.e. the x-spacing in use).
    """
    rho = k*k / h*h
    return rho * (u(x - h, t) + u(x + h, t)) + 2 * (1 - rho) * u(x, t) - u(x, t - k)

def print_x_pts(x_pts):
    size = len(x_pts)
    for i in range(size):
        print "%d/%d %f" % (i,size, x_pts[i])

def print_two_x_pts(x_pts, x_pts2):
    size = len(x_pts)
    for i in range(size):
        print "%d/%d %f | %f" % (i,size, x_pts[i], x_pts2[i])
def get_initial_x_pts(h):
    """
        Gets the initial array of x-pts at time t=0
        h - x spacing being used.
    """
    ans = []
    num_x_pts = int(ceil(1/ h))
    print "Not integer : %f" %num_x_pts
    for i in range(num_x_pts + 1): # Plus one so that we also get the very last end point
        x = i * h
        new_val = u(x,0)
        ans.append(new_val)
    return ans

def move_x_pts_forward(x_pts, t, k, h):
    num_x_pts = len(x_pts)
    ans = []
    for i in range(num_x_pts):
        # Skip the First and Last Point as the ends
        # are fixed
        if i == 0  or i == num_x_pts - 1:
            continue
        curr_x = x_pts[i]
        new_x = u_forward(curr_x, t, k, h)
        ans.append(new_x)
    return ans


def simulate(h, k, run_time, p):
    rho = k * k / h * h
    num_steps_forward = int(ceil(run_time / k))
    pts_array = []
    initial_x_pts = get_initial_x_pts(h)
    pts_array.append(initial_x_pts)

    for i in range(num_steps_forward):
        curr_x_pts = pts_array[i]
        curr_time = i * k
        new_x_pts = move_x_pts_forward(curr_x_pts, curr_time, k, h)
        pts_array.append(new_x_pts)
    return pts_array

def test():
    print 'hi'
    h = k = 10**(-2)
    run_time = 2
    p = 10
    pts_array = simulate(h,k,run_time,p)
    print "We have this many steps : %d " % len(pts_array)
    print_two_x_pts(pts_array[0], pts_array[1])


def main():
    test()


if __name__ == '__main__':
    main()