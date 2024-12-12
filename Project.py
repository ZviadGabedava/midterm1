import math

def simple_calculator():
    print("კალკულატორი")
    print("ოპერაციები:")
    print("+ : მიმატება")
    print("- : გამოკლება")
    print("* : გამრავლება")
    print("/ : გაყოფა")
    print("^ : ახარისხება")
    print("sqrt : ფესვი")
    print("% : პროცენტი")
    print("exit : გამოდი კალკულატორიდან")

    while True:
        operation = input("ჩაწერე ოპერაცია (+, -, *, /, ^, sqrt, %, exit): ").strip()

        if operation == "exit":
            print("გამოსვლა კალკულატორიდან")
            break

        if operation in ["+", "-", "*", "/", "^", "%"]:
            try:
                num1 = float(input("ჩაწერე პირველი რიცხვი: "))
                num2 = float(input("ჩაწერე მეორე რიცხვი: "))

                if operation == "+":
                    print(f"Result: {num1 + num2}")
                elif operation == "-":
                    print(f"Result: {num1 - num2}")
                elif operation == "*":
                    print(f"Result: {num1 * num2}")
                elif operation == "/":
                    if num2 == 0:
                        print("Error: ნულზე გაყოფა ნამდვილ რიცხვთა სისტემაში არ შეიძლება.")
                    else:
                        print(f"Result: {num1 / num2}")
                elif operation == "^":
                    print(f"Result: {num1 ** num2}")
                elif operation == "%":
                    print(f"Result: {num1 % num2}")

            except ValueError:
                print("Error: არასწორი ცვლადი. გთხოვ, ჩაწერე რიცხვითი მნიშვნელობა.")

        elif operation == "sqrt":
            try:
                num = float(input("ჩაწერე რიცხვი, რომ იპოვო ფესვი: "))
                if num < 0:
                    print("Error: უარყოფითი რიცხვიდან ნამდვილ რიცხვთა სისტემაში ფესვი არ ამოდის.")
                else:
                    print(f"Result: {math.sqrt(num)}")
            except ValueError:
                print("Error: არასწორი ცვლადი. გთხოვ, ჩაწერე რიცხვითი მნიშვნელობა.")

        else:
            print("არასწორი ოპერაცია. ცადე თავიდან.")

simple_calculator()
