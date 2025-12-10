from quick_sort import quick_sort

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
choice = input("Choose algorithm (quick / bubble): ").lower()

if choice == "quick":
    result = quick_sort(numbers)
    print("Sorted result:", result)
elif choice == "bubble":
    print("Bubble sort not implemented yet by Kittipot.")
else:
    print("Invalid choice")
