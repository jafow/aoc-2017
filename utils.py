def split_strip(line):
    """ map a line from a file object to a list of 'words' split on (not
    necessarily uniform!) spaces """
    return filter(lambda x: x != '', line.strip().split(' '))


def list_lines(file_object):
    """ return a 2D list of split lines """
    return list(map(split_strip, file_object))


def strip_readlines(file_object):
    """ read all lines of a file into a list; like list lines but 1D """
    return [line.strip() for line in file_object.readlines()]


def slice_len(L, start_index, slice_len):

    """ slices a chunk from list L of at index `start_index` of length
    `slice_len` and wraps the slice around to 0 if it """

    diff = len(L) - start_index
    if slice_len > diff:
        # wrap
        wrapped = L[start_index: start_index + diff]
        rem = slice_len - diff
        return wrapped + L[0: rem]
    else:
        return list(L[start_index: start_index + slice_len])
