
def main():
    numbers = (1, 5, 7, 11, 14, 17, 45, 56 ,78, 90, 123)
    to_find = 67

    left = 0
    right = len(numbers) - 1
    print(right)
                        
    while (left <= right):
        if numbers[left] + numbers[right] < to_find:
            left += 1
        elif numbers[left] + numbers[right] > to_find:
            right -= 1
        else:
            print(f"{numbers[left]} + {numbers[right]} = {to_find}")
            break  

if __name__ == "__main__":
    main()
