# Returns True if any value in the list a is True, and False otherwise.
def any(a):
    if True in a:
        return True
    else:
        return False


# Returns True if all values in the list a are True, and False otherwise.
def all(a):
    if False not in a:
        return True
    else:
        return False


# Returns True if exactly k values in the list a are True, and False otherwise.
def exactly(a, k):
    count = 0
    for i in range(len(a)):
        if a[i] is True:
            count += 1
        else:
            continue
    if count == k:
        return True
    else:
        return False


# Returns the number of True values in the list a.
def count(a):
    count = 0
    for i in range(len(a)):
        if a[i] is True:
            count += 1
        else:
            continue
    return count


# Unit tests the library.
def _main():
    import stdio

    a = [False, False, True, False, True, True, True]
    stdio.writeln('a             = ' + str(a))
    stdio.writeln('any(a)        = ' + str(any(a)))
    stdio.writeln('all(a)        = ' + str(all(a)))
    stdio.writeln('exactly(a, 3) = ' + str(exactly(a, 3)))
    stdio.writeln('count(a)      = ' + str(count(a)))


if __name__ == '__main__':
    _main()
