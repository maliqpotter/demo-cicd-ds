class Calculator:
    """Kelas kalkulator sederhana untuk demo unit testing"""

    def add(self, a, b):
        """Menambahkan dua angka"""
        return a + b

    def subtract(self, a, b):
        """Mengurangi dua angka"""
        return a - b

    def multiply(self, a, b):
        """Mengalikan dua angka"""
        return a * b

    def divide(self, a, b):
        """Membagi dua angka"""
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return a / b


def greet(name):
    """Fungsi untuk menyapa"""
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"


def main():
    """Fungsi utama aplikasi"""
    print("=== Demo CI/CD Python App ===")

    # Demo calculator
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

    # Demo greeting
    print(greet("CI/CD"))
    print(greet(""))


if __name__ == "__main__":
    main()
