import os
from pathlib import Path


def get_float_input(prompt: str) -> float:
    """Safely get a positive float number from user input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


def calculate_bmi_value(height: float, weight: float) -> float:
    """Calculate BMI."""
    return weight / (height ** 2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def format_result(height: float, weight: float, bmi: float, category: str) -> str:
    """Format result string."""
    return (
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {bmi:.2f}\n"
        f"Category: {category}\n"
    )


def get_valid_directory() -> Path:
    """Prompt user until a valid directory is provided."""
    while True:
        dir_path = input("Enter directory to save result: ").strip()
        path = Path(dir_path)
        if path.is_dir():
            return path
        print("Invalid directory path. Try again.")


def save_to_file(directory: Path, content: str, filename: str = "bmi_result.txt") -> Path:
    """Save content to a file."""
    output_path = directory / filename
    try:
        output_path.write_text(content)
        return output_path
    except OSError as e:
        print(f"Error saving file: {e}")
        return None


def main():
    print("=== BMI Calculator ===")

    height = get_float_input("Enter height (meters): ")
    weight = get_float_input("Enter weight (kg): ")

    bmi = calculate_bmi_value(height, weight)
    category = classify_bmi(bmi)

    result = format_result(height, weight, bmi, category)

    directory = get_valid_directory()
    output_path = save_to_file(directory, result)

    if output_path:
        print(f"\nResult saved at: {output_path}")
    else:
        print("\nFailed to save result.")


if __name__ == "__main__":
    main()
