from pydatastructs import SparseTable
from pydatastructs.utils.raises_util import raises


def test_st():
    array = [0, 1, 2, 3, 4, 5]
    st = SparseTable(array)
    assert st.query(0, 2) == 0
    queries = [{'L': 0, 'R': 2}, {'L': 1, 'R': 3}, {'L': 3, 'R': 5}]
    assert st.rmq(queries) == [0, 1, 3]
    array = [4, 6, 1, 5, 7, 3]
    st = SparseTable(array)
    assert st.query(0, 1) == 4
    queries = [{'L': 0, 'R': 2}, {'L': 1, 'R': 3}, {'L': 3, 'R': 5}]
    assert st.rmq(queries) == [1, 1, 3]
    assert raises(TypeError, lambda: SparseTable())
    assert raises(TypeError, lambda: st.rmq([1, 2]))
