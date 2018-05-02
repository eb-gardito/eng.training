#  Ejemplos de suma usando diferentes metodos, para evaluar performance y uso de memoria de cada uno.
#  usando memory-profiler


def double_sum(limit):
    #  usar recursividad es una muy mala opcion.
    #  double_sum(1000000) >> RecursionError: maximum recursion depth exceeded in comparison
    if limit == 1:
        return 1
    return limit * 2 + double_sum(limit - 1)


def double_sum_inline(n):
    total = 0
    for n_i in range(1, n + 1):
        total = total + 2 * n_i
    return total


def double_sum_with_list(n):
    elements = []
    for i in range(1, n + 1):
        elements.append(2 * i)
    return sum(elements)


def double_sum_with_list_comprehension(n):
    return sum([
        i * 2
        for i in range(1, n + 1)
    ])


def double_sum_with_generator(n):
    return sum(
        i * 2
        for i in range(1, n + 1)
    )


def double_sum_with_math_formula(n):
    #  sum from j to n = n * (n+j)/2, in this example j=1
    return n * (n + 1)
