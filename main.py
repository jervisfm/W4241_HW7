from math import ceil
try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure
    import sys
except ImportError:
    print('Dependency MatplotLib Is Missing. Please Install it and try again Exiting ...')
    exit(-1)


__author__ = 'Jervis Muindi'
# Date: April 2013
# Numerical Analysis and Algorithms

def f(x):
    """
        This is the function describing the initial state of system.
        You can change it something else (i.e. redefine it) if you'd like to solve a different problem.
    """
    if 0 <= x <= 0.5:
        return x
    elif 0.5 <= x <= 1.0:
        return 1 - x
    else:
        print "Error: undefined input %f" % x
        return 0


def u(x, k, h, rho):
    return rho/2 * (f(x - h) + f(x + h)) + (1 - rho) * f(x)


def print_x_pts(x_pts):
    """
        Debug method.
        Outputs all values in array.
    """
    size = len(x_pts)
    for i in range(size):
        print "%d/%d %f" % (i,size, x_pts[i])

def print_two_x_pts(x_pts, x_pts2):
    """
        Debug method.
        Outputs all points in two arrays side by side.
    """
    size = len(x_pts)
    print "x_pts = %d | %d" %(len(x_pts), len(x_pts2))
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
    for i in xrange(num_x_pts + 1): # Plus one to include the very last x-point.
        x = i * h
        new_val = u(x, 0, h, rho)
        ans.append(new_val)
    return ans

def get_func_x_pts(h):
    """ Gets the points as represented by the function f(x)
        h - x spacing being used
    """
    ans = []
    num_x_pts = int(ceil(1/h))
    for i in xrange(num_x_pts + 1): # Plus one to include the very last x-point
        x = i * h
        val = f(x)
        ans.append(val)
    return ans



def move_x_pts_forward(prev_x_pts, curr_x_pts, k, h):
    """
        Moves forward from the current line to the next one in time.
        prev_x_pts - all the values at the prior time step
        curr_x_pts - all the values at the current time
        k - the delta/amount in time to go forwards by
        h - the delta in x-pts (i.e. the x-spacing value).
    """
    num_x_pts = len(curr_x_pts)
    rho = (h/k) ** 2
    ans = []
    for i in xrange(num_x_pts):
        if  i == 0 or i == num_x_pts - 1: # First/Last Points are fixed and always at 0.
            ans.append(0)
            continue
        #    We apply/use the formula for u(x,t+k) which lets us move forward in time.
        #    The formula is :
        #        u(x,t+k) = rho * [u(x+h,t) + u(x-h,t)] + 2(1-p)*u(x,t) - u(x,t-k)
        new_val = rho * (curr_x_pts[i+1] + curr_x_pts[i-1]) + 2*(1-rho)*curr_x_pts[i] - prev_x_pts[i]
        ans.append(new_val)
    return ans

def plot_x_pts(y_points, h, num):
    """
        Plots the given Points and saves it to a file called 'graph.png' appended with the given 'num' value.
    """
    size = len(y_points)
    x_points = []
    for i in range(size):
        val = i * h
        x_points.append(val)

    fig = figure()
    fig.suptitle('Visualizing String', fontsize=14, fontweight='bold')
    plt.xlabel('X - Space')
    plt.ylabel('U - Height/Magnitude')
    plt.ylim([0,0.5])
    plt.plot(x_points, y_points, 'ro')
    fig.savefig('graph%d.png' % num)

def simulate(h, k, run_time):
    """
        Solves the PDE for a vibrating string by using the explicit method.
        It returns all the y-values of the string throughout duration specified.

        run_time - For How Long we are supposed simulate the string motion. It should be an integer > 0.
        h - the delta in x-points (i.e. the x-point spacing) to be used.
        k - the delta in time. (i.e. how much we go ahead in time in one step).
    """
    num_steps_forward = int(ceil(run_time / k))
    pts_array = []
    rho = (h/k) ** 2
    initial_x_pts = get_starting_x_pts(h, rho)
    prev_x_pts = get_func_x_pts(h)

    pts_array.append(initial_x_pts)

    for i in range(num_steps_forward):
        curr_x_pts = pts_array[i]
        new_x_pts = move_x_pts_forward(prev_x_pts,curr_x_pts, k, h)
        pts_array.append(new_x_pts)
        prev_x_pts = curr_x_pts

    return pts_array

def do_all_plots(points, h, graph_rate):
    counter = 0
    for x_pts in points:
        if counter % graph_rate == 0:
            print "Plotting graph # %d" % counter
            plot_x_pts(x_pts, h, counter)
        counter += 1

def do_main(h,k,run_time,graph_rate):
    pts_array = simulate(h,k,run_time,graph_rate)
    print "We have this many steps : %d " % len(pts_array)
    print_two_x_pts(pts_array[0], pts_array[0])
    print "We have this many steps : %d " % len(pts_array)
    print "plotting..."
    do_all_plots(pts_array, h)
    print "All plots done"

def usage():
    print '**************'
    print 'Partial ODE solver and grapher for the model problem of a vibrating string: '
    print 'Usage: '
    print 'python main.py [x-width] [t-width] [total_time] [graph_rate] '
    print '     x-width : amount of x-spacing between points'
    print '     t-width: delta in time to be applied in a single step forward'
    print '     total_time: amount of time be used in simulating the system'
    print '     graph_rate: A graph should be drawn/plotted every "graph_rate" steps'
    print '\nExample: python main.py 0.01 0.01 2 10\n'
    print 'Note: 1) All input values should be positive numeric values. '
    print '      2) Graphing ability is dependent on MatplotLib being installed'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def valid_inputs(h,k,total_time, graph_rate):
    if (not is_number(h) or h < 0):
        'h value must be a positive number : %s' % str(h)
        return False
    if (not is_number(k) or k < 0):
        'k value must be a positive number: %s' % str(k)
        return False
    if (not is_number(total_time) or total_time < 0):
        'Time T must be a positive number: %s' % str(total_time)
        return False
    if (not is_number(graph_rate) or graph_rate < 0) :
        'Graph Rate p must be a positive number: %s' % graph_rate
        return False
    return True

def main():
    arg_count = len(sys.argv) - 1
    if arg_count != 4:
        usage()
    else:
        h = sys.argv[1]
        k = sys.argv[2]
        total_time = sys.argv[3]
        graph_rate = sys.argv[3]
        if not valid_inputs(h,k,total_time,graph_rate):
            print 'Invalid Inputs detected'
            print '************************'
            usage()
            exit(-1)
        else:
            do_main(h,k,total_time,graph_rate)


if __name__ == '__main__':
    main()