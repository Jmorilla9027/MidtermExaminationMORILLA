print("=" * 39)
print("    SALES RECORD MANAGEMENT SYSTEM   ")
print("1. Add Sale Record")
print("2. View All Records & Summary Statistics")
print("3. Clear All Sales Data")
print("4. Exit System")
print("=" * 39)


choice = input("Select and option (1-4:)")

if choice == "1":
    input("Enter Item Name: ")
    int(input("Enter Item Quantity Sold: "))
    float(input("Enter Item Price /unit: "))

elif choice == "2":
    exit()

elif choice == "4":
    print("Thank you for using the Sales Record Management System.")
    exit()

