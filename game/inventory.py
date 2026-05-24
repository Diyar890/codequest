class Item:
    def __init__(self, name: str, item_type: str,
                 effect_value: int, required_level: int = 1,
                 price: int = 10):
        self.item_id: int = id(self)
        self.name: str = name
        self.type: str = item_type      # "potion", "shield", "language"
        self.effect_value: int = effect_value
        self.required_level: int = required_level
        self.price: int = price

    def use(self, player) -> str:
        if self.type == "potion":
            player.heal(self.effect_value)
            return f"🧪 Used {self.name}! Restored {self.effect_value} HP."
        elif self.type == "shield":
            return f"🛡️  {self.name} is ready to block next Compilation Error!"
        elif self.type == "language":
            return f"🔓 Unlocked language: {self.name}"
        return f"Used {self.name}"

    def get_description(self) -> str:
        return (f"{self.name} [{self.type}] — "
                f"Effect: {self.effect_value} | "
                f"Required Level: {self.required_level} | "
                f"Price: {self.price}g")

    def is_equippable(self) -> bool:
        return self.type in ["shield", "language"]

    def to_dict(self) -> dict:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "type": self.type,
            "effect_value": self.effect_value,
            "required_level": self.required_level,
            "price": self.price
        }

    def __repr__(self):
        return f"Item(name={self.name}, type={self.type})"


class Inventory:
    def __init__(self, player_id: int, item_id: int, quantity: int = 1):
        self.inventory_id: int = id(self)
        self.player_id: int = player_id
        self.item_id: int = item_id
        self.quantity: int = quantity
        self._item = None  # reference to actual Item object

    def add_item(self, item: Item):
        self._item = item
        self.item_id = item.item_id
        self.quantity += 1
        return f"Added {item.name} to inventory (x{self.quantity})"

    def remove_item(self) -> bool:
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def show_inventory(self):
        if self._item:
            print(f"  [{self.quantity}x] {self._item.get_description()}")

    def to_dict(self) -> dict:
        return {
            "inventory_id": self.inventory_id,
            "player_id": self.player_id,
            "item_id": self.item_id,
            "quantity": self.quantity
        }

    def __repr__(self):
        return f"Inventory(item_id={self.item_id}, qty={self.quantity})"


# Default items in the game
ITEM_CATALOG = [
    Item("Clean Code Potion", "potion", effect_value=50, required_level=1, price=20),
    Item("Compilation Shield", "shield", effect_value=1, required_level=1, price=30),
    Item("Python Gem", "language", effect_value=0, required_level=1, price=0),
    Item("C Gem", "language", effect_value=0, required_level=5, price=50),
    Item("C++ Gem", "language", effect_value=0, required_level=10, price=100),
]
