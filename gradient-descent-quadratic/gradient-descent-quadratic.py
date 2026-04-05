def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for i in range(steps):
        grad = (2 * a * x0 + b) * lr
        x0 = x0 - grad
    return x0
