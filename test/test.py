from Algoritmo import potencia
import pytest

@pytest.mark.parametrize(
    ["lo", "hi", "k", "resultado"],
    [
        (3,6,4,6)
    ]
)
def test_sort(lo: int, hi: int, k: int, resultado: int):
    assert potencia.getKth(lo, hi, k)==resultado