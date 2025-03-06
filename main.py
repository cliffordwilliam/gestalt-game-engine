from dataclasses import dataclass

from beartype import beartype
from beartype.roar import BeartypeCallHintParamViolation


class Player:
    @beartype
    def __init__(self, name: str, health: int):
        self._name = name
        self._health = health

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @beartype
    def name(self, value: str) -> None:
        self._name = value

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    @beartype
    def health(self, value: int) -> None:
        if value < 0:
            raise ValueError("Health cannot be negative")
        self._health = value

    @beartype
    def take_damage(self, damage: int) -> None:
        self.health -= damage


def main() -> None:
    print("Running Type Safety Tests...\n")

    try:
        player = Player("Knight", 100)
        print("OK Player created successfully!\n")

        player.health = 50
        print("OK Health updated successfully!\n")

        player.take_damage(20)
        print("OK Damage applied successfully!\n")

        print("BAD Trying to set invalid health (-10)...")
        player.health = -10  # Should raise ValueError
    except ValueError as e:
        print(f"OK Caught ValueError: {e}\n")

    try:
        print("BAD Trying to set invalid name (int instead of str)...")
        player = Player("Knight", 100)
        player.name = 123  # Should raise BeartypeCallHintParamViolation
    except BeartypeCallHintParamViolation as e:
        print(f"OK Caught BeartypeCallHintParamViolation: {e}\n")

    try:
        print('BAD Trying to pass string "a lot" as damage...')
        player = Player("Knight", 100)
        player.take_damage("a lot")  # Should raise BeartypeCallHintParamViolation
    except BeartypeCallHintParamViolation as e:
        print(f"OK Caught BeartypeCallHintParamViolation: {e}\n")

    try:
        print("BAD Trying to create player with invalid health (str instead of int)...")
        Player("Warrior", "full")  # Should raise BeartypeCallHintParamViolation
    except BeartypeCallHintParamViolation as e:
        print(f"OK Caught BeartypeCallHintParamViolation: {e}\n")

    print("All tests completed!")


@beartype
@dataclass
class UserDto:
    name: str
    age: int


@beartype  # type: ignore
def create_user(data: dict) -> UserDto:  # type: ignore
    return UserDto(**data)  # OK Type safety enforced at runtime


def test_user_creation() -> None:
    print("\nRunning Dictionary-to-Class Type Safety Tests...\n")

    try:
        data = {"name": "Alice", "age": 25}
        user = UserDto(**data)  # OK Works
        print(f"OK UserDto created successfully! {user}")
    except Exception as e:
        print(f"BAD Unexpected error: {e}")

    try:
        data = {"name": "Alice", "age": "twenty-five"}  # BAD Invalid type for age
        user = UserDto(**data)
    except BeartypeCallHintParamViolation as e:
        print(f"OK Caught BeartypeCallHintParamViolation: {e}")

    try:
        data = {"age": 25}  # BAD Missing 'name' field
        user = UserDto(**data)
    except TypeError as e:
        print(f"OK Caught TypeError: {e}")

    try:
        data = {
            "name": "Alice",
            "age": 25,
            "email": "alice@example.com",
        }  # BAD Extra field
        user = UserDto(**data)
    except TypeError as e:
        print(f"OK Caught TypeError: {e}")

    print("\nAll tests completed!")


test_user_creation()

if __name__ == "__main__":
    main()
    test_user_creation()
