def is_number(num: str):
    """check string is number"""
    return num.replace("-", "").replace(".", "").isdigit()


def calc(expression: str):
    """Calculator function"""
    expression = expression.replace(" ", "").replace("--", "+").replace("++", "+")
    if (
        expression.count("/+")
        + expression.count("*+")
        + expression.count("*/")
        + expression.count("/*")
        + expression.count("+/")
        + expression.count("+*")
    ):
        return "ERROR"
    expression = expression.replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ")
    expression = expression.replace("/  - ", "/ -").replace("*  - ", "* -").replace("+  - ", "+ -")
    if expression[0:2] in [" -", " +"]:
        expression = "0" + expression

    expression = expression.split()

    if not all(map(lambda x: (x in "-+*/" or is_number(x)), expression)):
        return "ERROR"
    if len(expression) == 0 or expression[-1] in "*-+/" or expression[0] in "-+":
        return "ERROR"

    lst = [expression[0]]
    for i in expression[1:]:
        if i in "+-*/":
            lst.append(i)
        elif is_number(i) and lst[-1] in "+-":
            lst.append(i)
        elif is_number(i) and lst[-1] in "*" and is_number(lst[-2]):
            del lst[-1]
            lst[-1] = str(float(lst[-1]) * float(i))
        elif is_number(i) and lst[-1] in "/" and is_number(lst[-2]):
            if int(i) == 0:
                return "ERROR"
            del lst[-1]
            lst[-1] = str(float(lst[-1]) / float(i))
        else:
            return "ERROR"
    lst = (
        "".join(lst)
        .replace("-+", "-")
        .replace("--", "+")
        .replace("-", " -")
        .replace("+", " ")
        .split()
    )
    return sum(map(float, lst))


if __name__ == "__main__":
    print("Калькулятор работает с операциями -+*/")
    print("Пример ввода:\n1-8*17+13\nВывод: -122")
    print(calc(input()))
