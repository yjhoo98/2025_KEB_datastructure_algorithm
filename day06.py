def print_poly(f_x,t_x) -> str:
    # term = len(f_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)-1):
        coefficient = f_x[i]
        term=t_x[i]
        if coefficient!=0:
            if coefficient > 0:
                poly_expression = poly_expression + "+"
            # elif coefficient==0:
            #     poly_expression = poly_expression
            poly_expression = poly_expression + f'{coefficient}x^{term} '
            # term = term - 1
        elif coefficient==0:
            poly_expression = poly_expression
    if f_x[len(f_x)-1]==0:
       return poly_expression
    elif f_x[len(f_x)-1]>0:

        return poly_expression +"+"+str(f_x[len(f_x)-1])
    else:
        return poly_expression + str(f_x[len(f_x) - 1])

def calculation_poly(x_value, f_x,t_x) -> int:
    return_value = 0


    for i in range(len(fx)):
        coefficient = f_x[i]
        term = t_x[i]
        return_value += coefficient * pow(x_value, term)
        term = term - 1

    return return_value


fx = [2, 5,-9,11]
tx=[20,7,2,0]
if __name__ == "__main__":
    print(print_poly(fx,tx))

    print(calculation_poly(int(input("x 값 : ")), fx,tx))
