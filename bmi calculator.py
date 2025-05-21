import os

def calculate_bmi():
    try:
        height = float(input("Enter height in meters (e.g., 1.75): "))
        weight = float(input("Enter weight in kilograms (e.g., 70): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if height <= 0 or weight <= 0:
        print("Height and weight must be positive numbers.")
        return

    bmi = weight / (height ** 2)
    category = ""

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    result = f"Height: {height} m\nWeight: {weight} kg\nBMI: {bmi:.2f}\nCategory: {category}\n"

    dir_path = input("Enter the directory where you want to save the result (e.g., /path/to/folder): ").strip()
    if not os.path.isdir(dir_path):
        print("Invalid directory path.")
        return

    output_path = os.path.join(dir_path, "bmi_result.txt")
    with open(output_path, "w") as file:
        file.write(result)

    print(f"BMI result saved at: {output_path}")

if __name__ == "__main__":
    calculate_bmi()