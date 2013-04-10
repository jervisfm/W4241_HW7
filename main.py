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
    return rho * (u(x - h, t) + u(x + h, t)) + 2(1 - rho) * u(x, t) - u(x, t - k)


def get_initial_x_pts(h):
    """
        Gets the initial array of x-pts at time t=0
        h - x spacing being used.
    """
    ans = []
    num_x_pts = 1/ h
    for i in range(num_x_pts):
        x = i * h
        ans[i] = u(x,0)
    return ans

def move_x_pts_forward(x_pts, t, k, h):
    num_x_pts = len(x_pts)
    ans = []
    for i in range(num_x_pts):
        curr_x = x_pts[i]
        new_x = u_forward(curr_x, t, k, h)
        ans[i] = new_x
    return ans


def simulate(h, k, run_time, p):
    rho = k * k / h * h
    num_x_pts = 1 / h
    num_steps_forward = run_time / k
    pts_array = []
    initial_x_pts = get_initial_x_pts(h)
    pts_array.append(initial_x_pts)

    for i in range(num_steps_forward):
        curr_x_pts = pts_array[i]
        curr_time = i * k
        arr = [];
        new_x_pts = move_x_pts_forward(curr_x_pts, curr_time, k, h)
        pts_array.append(new_x_pts)
    return pts_array

def test():
    print 'hi'


def main():
    test()


if __name__ == '__main__':
    main()