from null_bug import cause_null_bug
from unreachable_bug import cause_unreachable_bug
from type_bug import cause_type_bug
from logic_bug import is_even
from loop_bug import run_infinite_loop

if __name__ == "__main__":
    print("Running null bug...")
    cause_null_bug()

    print("Running unreachable bug...")
    cause_unreachable_bug()

    print("Running type bug...")
    cause_type_bug()

    print("Running logic bug...")
    print(f"Is 3 even? {is_even(3)}")  # Bu hatalı sonuç verir

    print("Running infinite loop bug (skip to avoid lock)...")
    # run_infinite_loop()  # Yoruma alındı, kilitlenmesin
