from math import ceil
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

__author__ = 'Jervis Muindi'


def f(x):
    if 0 <= x <= 0.5:
        return x
    elif 0.5 <= x <= 1.0:
        return 1 - x
    else:
        print "Error: undefined input %f" % x
        return 0


def u(x, k, h, rho):
    return rho/2 * (f(x - h) + f(x + h)) + (1 - rho) * f(x)

def u_forward(x, t, k, h):
    """
     Let us move forward in time
     x - the current x point
     t - the current time
     k - the delta in time to go forwards
     h - the delta in x-pts (i.e. the x-spacing in use).
    """
    rho = (k/h)**2
    #print "INIT rho  = %f" %rho
    #print "------"

    tx = x-h
    tk = t
    if tx - tk < 0:
        print "x = %f"  % x
        print "h = %f" % h
        print "t = %f" % t

    return rho * (u(x - h, t, h, rho) + u(x + h, t, h, rho)) + 2 * (1 - rho) * u(x, t, h, rho) - u(x, t - k, h, rho)

def print_x_pts(x_pts):
    size = len(x_pts)
    for i in range(size):
        print "%d/%d %f" % (i,size, x_pts[i])

def print_two_x_pts(x_pts, x_pts2):
    size = len(x_pts)
    for i in range(size):
        print "%d/%d %f | %f" % (i,size, x_pts[i], x_pts2[i])
def get_starting_x_pts(h, rho):
    """
        Gets the initial array of x-pts at time t=0
        h - x spacing being used.
        rho - ratio of (h/k)^2
    """
    ans = []
    num_x_pts = int(ceil(1/ h))
    for i in xrange(num_x_pts + 1): # Plus one so that we also get the very last end point
        x = i * h
        new_val = u(x, 0, h, rho)
        ans.append(new_val)
    return ans

def get_func_x_pts(h, rho):
    """ Gets the points as represented by the function f(x)
        h - x spacing being used
    """
    ans = []
    num_x_pts = int(ceil(1/h))
    for i in xrange(num_x_pts + 1): # Plus one so that we also get the very last end point on line
        x = i * h
        val = f(x)
        ans.append(val)
    return ans



def move_x_pts_forward(x_pts, t, k, h):
    num_x_pts = len(x_pts)
    ans = []
    for i in range(num_x_pts):
        # The First and Last Point are always
        # Fixed.
        """if i == 0  or i == num_x_pts - 1:
            ans.append(0)
            continue"""
        curr_x = i * h
        new_x = u_forward(curr_x, t, k, h)
        ans.append(new_x)
    return ans

def plot_x_pts(y_points, h, num):

    size = len(y_points)
    x_points = []
    for i in range(size):
        val = i * h
        x_points.append(val)

    fig = figure()
    fig.suptitle('Visualizing X-Line', fontsize=14, fontweight='bold')
    plt.xlabel('X')
    plt.ylabel('U')
    plt.ylim([0,0.5])
    plt.plot(x_points, y_points, 'ro')
    #plt.show()
    fig.savefig('graph%d.png' % num)

def simulate(h, k, run_time, p):
    num_steps_forward = int(ceil(run_time / k))
    pts_array = []
    rho = (h/k) ** 2
    initial_x_pts = get_starting_x_pts(h, rho)

    pts_array.append(initial_x_pts)

    for i in range(num_steps_forward):
        curr_x_pts = pts_array[i]
        curr_time = i * k
        new_x_pts = move_x_pts_forward(curr_x_pts, curr_time, k, h)
        pts_array.append(new_x_pts)
    return pts_array

def do_all_plots(points, h):
    counter = 0
    for x_pts in points:
        print "doing graph # %d" % counter
        plot_x_pts(x_pts, h, counter)
        counter += 1

def test():
    print 'hi'
    h = k = 10**(-2)
    run_time = 2
    p = 10
    pts_array = simulate(h,k,run_time,p)
    print "We have this many steps : %d " % len(pts_array)
    print_two_x_pts(pts_array[0], pts_array[1])
    print "We have this many steps : %d " % len(pts_array)
    print "plotting..."
    do_all_plots(pts_array, h)
    print "All plots done"


def main():
    test()


if __name__ == '__main__':
    main()