
__author__ = 'Jervis Muindi'


def f(x):
    if 0 <= x <= 0.5:
        return x
    elif 0.5 <= x <= 1.0:
        return 1-x
    else:
        print "Error: undefined input %f" % x
        return 0

def test():
    print 'hi'

def main():
    test()

if __name__ == '__main__':
    main()