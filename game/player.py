class Player:
    def __init__(self, name: str):
        self.player_id: int = 1
        self.name: str = name
        self.hp: int = 100
        self.max_hp: int = 100
        self.attack: int = 15
        self.level: int = 1
        self.gold: int = 0
        self.inventory = []  # list of Inventory objects

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def move(self, direction: str) -> str:
        return f"{self.name} moves {direction}"

    def pick_up_item(self, item) -> str:
        from game.inventory import Inventory
        entry = Inventory(player_id=self.player_id, item_id=item.item_id)
        self.inventory.append(entry)
        return f"Picked up {item.name}"

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.attack += 5
        self.hp = self.max_hp
        print(f"⬆️  Level Up! Now level {self.level} | ATK: {self.attack} | HP: {self.max_hp}")

    def get_unlocked_languages(self) -> list:
        languages = ["Python"]
        if self.level >= 5:
            languages.append("C")
        if self.level >= 10:
            languages.append("C++")
        languages.append("JavaScript")  # always bonus
        return languages

    def show_stats(self):
        print(f"\n{'='*30}")
        print(f"  {self.name}")
        print(f"{'='*30}")
        print(f"  HP:     {self.hp}/{self.max_hp}")
        print(f"  ATK:    {self.attack}")
        print(f"  Level:  {self.level}")
        print(f"  Gold:   {self.gold}")
        print(f"  Languages: {', '.join(self.get_unlocked_languages())}")
        print(f"{'='*30}")

    def to_dict(self) -> dict:
        return {
            "player_id": self.player_id,
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "level": self.level,
            "gold": self.gold
        }

    @classmethod
    def from_dict(cls, data: dict):
        p = cls(data["name"])
        p.player_id = data["player_id"]
        p.hp = data["hp"]
        p.max_hp = data["max_hp"]
        p.attack = data["attack"]
        p.level = data["level"]
        p.gold = data["gold"]
        return p

    def __repr__(self):
        return f"Player(name={self.name}, hp={self.hp}/{self.max_hp}, level={self.level})"
