

# main function to solve linear regression
def solve(X, Y):
    # calculating the denominator as this is same for variable a and b
    # by minimizing E = sum((Y - Yhat)^2) w.r.t a and b
    deno = X.dot(X) - X.mean() * X.sum()

    # partial derivative of E w.r.t a dE/da
    a = ((X.dot(Y) - Y.mean() * X.sum()) / deno)
    # partial derivative of E w.r.t b dE/db
    b = ((Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / deno)
    # calculating predicted Y
    Yhat = a * X + b
    return Yhat
