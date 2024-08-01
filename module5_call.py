from module5_mod import NumberList

def main():
    num_list = NumberList()

    n = int(input("Enter a positive integer N: "))
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        num_list.insert(num)

    x = int(input("Enter the number X to search for: "))
    result = num_list.search(x)
    
    print(result)

if __name__ == "__main__":
    main()
