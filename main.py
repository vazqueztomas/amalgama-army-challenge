from helpers.exceptions import InsufficientGold
from models.army import Army


def run_demo():
    print("--- Armies ---")

    red = Army(name="Red", civilization="English")
    blue = Army(name="Blue", civilization="Chinese")

    print(red.summary())
    print(blue.summary())

    print("\nRed attacks Blue...")
    outcome = red.attack(blue)
    print(f"Battle outcome: {outcome}")

    print(red.summary())
    print(blue.summary())

    print("\nTraining Red's first unit...")
    try:
        red.train_unit(0)
        print("Training successful!")
    except InsufficientGold:
        print("Red does not have enough gold to train this unit.")

    print(red.summary())

    print("\nTransforming Red's first unit...")
    try:
        red.transform_unit(0)
        print("Transformation successful!")
    except Exception as e:
        print(f"Transformation failed: {e}")

    print(red.summary())


if __name__ == "__main__":
    run_demo()
