import timeit
import hellotext


if __name__ == "__main__":
    reps = 100000
    t = timeit.timeit(
        stmt="{}(i)".format("helloworld_pythonic_func"),
        setup="from hellotext import helloworld_pythonic_func; i = 1000",
        number=reps,
    )
    print(f"helloworld_pythonic_func for {reps} times: {t:.6f}")

    t = timeit.timeit(
        stmt="{}(s)".format("helloworld_derived_cfunc"),
        setup="from hellotext import helloworld_derived_cfunc; s = ['hello', 'to', 'the', 'world']",
        number=reps,
    )
    print(f"helloworld_derived_cfunc for {reps} times: {t:.6f}")
