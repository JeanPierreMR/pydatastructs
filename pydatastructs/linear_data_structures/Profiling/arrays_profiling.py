from pydatastructs.linear_data_structures import (
    OneDimensionalArray)
import timeit


def one_dimensional_array_profiling(load, times_to_test, margin):
    '''
    Calculates the time that takes to execute one time,
    as reference_time, and the time that actually takes.

    Parameters
    -------
    load -> size of the data structure
    times_to_test -> number of times to execute to get an average
    margin -> what difference is accepted

    Returns
    -------
    result -> [is_correct, difference_proportion)]
        is_correct -> boolean
        difference_proportion -> float (reference_time / time)
    '''

    def reference_action():
        array[half]
        array[half] = 32

    def actions():
        for x in range(load):
            array[x]
            array[x] = 32

    half = int(load / 2)  # used for reference time
    array = OneDimensionalArray(int, load)
    reference_time = timeit.timeit(reference_action, number=times_to_test) / times_to_test * load * (margin + 1)
    time = timeit.timeit(actions, number=times_to_test) / times_to_test

    if time < reference_time:
        return [True, reference_time / time]
    else:
        return [False, reference_time / time]


if __name__ == "__main__":
    load_v = 100000
    times_to_test_v = 100
    margin_v = 0.001
    print(one_dimensional_array_profiling(load_v, times_to_test_v, margin_v))
