import time

while True:
  try:
    print("""  
1- Get the GCD using prime numbers method.
2- Get the GCD using reminder numbers method.
3- Get the LCM.
0- End the program.
""")

    first_choice = int(input("\nEnter the operation you wish..... \n"))


    if first_choice in range(0,11):

        if first_choice == 1:
            def gcd_prime(a, b):

                prime_factors_a = []
                prime_factors_b = []

                print(f"Prime Factorization of {a}:")
                while a % 2 == 0:
                    prime_factors_a.append(2)
                    print(f"\tDivisible by 2: {a} // 2 = {a // 2}")
                    a //= 2
                i = 3
                while i * i <= a:
                    while a % i == 0:
                        prime_factors_a.append(i)
                        print(f"\tDivisible by {i}: {a} // {i} = {a // i}")
                        a //= i
                    i += 2

                if a > 1:
                    prime_factors_a.append(a)
                    print(f"\tPrime: {a}")

                print(f"\nPrime Factorization of {b}:")
                while b % 2 == 0:
                    prime_factors_b.append(2)
                    print(f"\tDivisible by 2: {b} // 2 = {b // 2}")
                    b //= 2
                i = 3
                while i * i <= b:
                    while b % i == 0:
                        prime_factors_b.append(i)
                        print(f"\tDivisible by {i}: {b} // {i} = {b // i}")
                        b //= i
                    i += 2

                if b > 1:
                    prime_factors_b.append(b)
                    print(f"\tPrime: {b}")

                intersection = set(prime_factors_a) & set(prime_factors_b)

                gcd = 1
                for prime in intersection:
                    gcd *= prime

                return gcd


            while True:
                try:
                    num1 = int(input("Enter the first positive integer: "))
                    num2 = int(input("Enter the second positive integer: "))
                    if num1 <= 0 or num2 <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter positive integers only.")

            gcd = gcd_prime(num1, num2)

            print(f"\nThe GCD of {num1} and {num2} is: {gcd}")


        elif first_choice == 2:
            def gcd(a, b):

                print(f"Step 1: Initial values - a = {a}, b = {b}")
                while b != 0:
                    remainder = a % b
                    print(f"Step 2: Remainder - a = {a}, b = {b}, remainder = {remainder}")
                    a = b
                    b = remainder
                    print(f"Step 3: Update values - a = {a}, b = {b}")
                    print("_")
                return a


            while True:
                try:
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter integers only.")

            gcd_result = gcd(num1, num2)
            print(f"Step 4: GCD - The greatest common divisor of {num1} and {num2} is: {gcd_result}")


        elif first_choice == 3:
            def gcd(a, b):

                print(f"Step 1: Initial values - a = {a}, b = {b}")
                while b != 0:
                    remainder = a % b
                    print(f"Step 2: Remainder - a = {a}, b = {b}, remainder = {remainder}")
                    a = b
                    b = remainder
                    print(f"Step 3: Update values - a = {a}, b = {b}")
                    print("_")
                return a


            def lcm(a, b):

                gcd_result = gcd(a, b)
                lcm_result = (a * b) // gcd_result
                print(f"\nStep 4: LCM - The least common multiple of {a} and {b} is: {lcm_result}")
                return lcm_result


            while True:
                try:
                    num1 = int(input("Enter the first number: \n "))
                    num2 = int(input("Enter the second number: \n "))
                    if num1 <= 0 or num2 <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter positive integers only.")

            gcd_result = gcd(num1, num2)
            lcm_result = lcm(num1, num2)

            print(f"\n**Note:** The GCD is used in the LCM calculation as LCM(a, b) = (a * b) / GCD(a, b).")




        elif first_choice == 0:
            break

    else:
      print("Invalid input. Please enter from the previos choices")
    print("""
        the program will start in 3 seconds
        """)
    for abc in range(1,4):
        print(abc)
        time.sleep(1)

  except ValueError:

    print("Invalid input. Please enter a number.")



  if first_choice in range(0,1000000000000000000000000000000000000000000000000) and first_choice != 0:
    print("Do you want to enter another option? (yes/no)")

    answer = input().lower()
    if answer != 'yes':
      break
print("Thank you for using this tool !!")


