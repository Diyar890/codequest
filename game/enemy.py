class Enemy:
    def __init__(self, name: str, hp: int, attack: int,
                 gold_reward: int, difficulty: str = "Easy"):
        self.enemy_id: int = id(self)
        self.name: str = name
        self.hp: int = hp
        self.max_hp: int = hp
        self.attack: int = attack
        self.gold_reward: int = gold_reward
        self.difficulty: str = difficulty  # "Easy", "Medium", "Hard"

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def drop_loot(self) -> dict:
        return {
            "gold": self.gold_reward,
            "xp": self.gold_reward * 2
        }

    def show_stats(self):
        bar = int((self.hp / self.max_hp) * 20)
        hp_bar = "█" * bar + "░" * (20 - bar)
        print(f"\n👾 {self.name} [{self.difficulty}]")
        print(f"   HP: [{hp_bar}] {self.hp}/{self.max_hp}")
        print(f"   ATK: {self.attack} | Gold: {self.gold_reward}")

    def to_dict(self) -> dict:
        return {
            "enemy_id": self.enemy_id,
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "gold_reward": self.gold_reward,
            "difficulty": self.difficulty
        }

    def __repr__(self):
        return f"Enemy(name={self.name}, hp={self.hp}, difficulty={self.difficulty})"


class Boss(Enemy):
    """Boss inherits Enemy — same structure but stronger with special attacks"""

    def __init__(self, name: str, hp: int, attack: int,
                 gold_reward: int, difficulty: str = "Hard",
                 time_limit: int = 60, memory_limit: int = 256):
        super().__init__(name, hp, attack, gold_reward, difficulty)
        self.is_boss: bool = True
        self.time_limit: int = time_limit       # TIME LIMIT Attack (seconds)
        self.memory_limit: int = memory_limit   # MEMORY LIMIT Attack (MB)

    def time_limit_attack(self, player) -> int:
        """If player exceeds time limit — boss attacks"""
        damage = self.attack * 2
        player.take_damage(damage)
        print(f"⏱️  TIME LIMIT Attack! {self.name} deals {damage} damage!")
        return damage

    def memory_limit_attack(self, player) -> int:
        """If player exceeds memory limit — boss attacks"""
        damage = self.attack + 10
        player.take_damage(damage)
        print(f"💾 MEMORY LIMIT Attack! {self.name} deals {damage} damage!")
        return damage

    def show_stats(self):
        super().show_stats()
        print(f"   ⏱️  Time Limit: {self.time_limit}s")
        print(f"   💾 Memory Limit: {self.memory_limit}MB")

    def __repr__(self):
        return f"Boss(name={self.name}, hp={self.hp}, difficulty={self.difficulty})"
