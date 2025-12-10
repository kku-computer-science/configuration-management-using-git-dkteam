from quick_sort import quick_sort
from bubble_sort import bubble_sort

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
choice = input("Choose algorithm (quick / bubble): ").lower()

if choice == "quick":
    result = quick_sort(numbers)
    print("Sorted result:", result)
elif choice == "bubble":
    result = bubble_sort(numbers)
    print("Sorted result:", result)
else:
    print("Invalid choice")
