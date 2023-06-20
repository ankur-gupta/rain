# We can use relative/local imports too. This prevents pollution of global package namespace.
from .variables import X_MIN, X_MAX, X_STEP


def demo_use_of_local_imports():
    return range(X_MIN, X_MAX, X_STEP)
