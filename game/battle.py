from game.judge0_result import Judge0Result


class Battle:
    def __init__(self, player, enemy, task, language_used: str = "Python"):
        self.battle_id: int = id(self)
        self.player = player
        self.enemy = enemy
        self.task = task
        self.language_used: str = language_used
        self.submitted_code: str = ""
        self.result: str = "pending"        # "win", "lose", "ran"
        self.damage_dealt: int = 0
        self.time_limit_sec: int = task.time_limit_sec
        self.memory_limit_mb: int = task.memory_limit_mb
        self.rounds: int = 0
        self.judge0_results: list = []      # list of Judge0Result

    def validate_language(self) -> bool:
        """Check if player has unlocked this language"""
        unlocked = self.player.get_unlocked_languages()
        if self.language_used not in unlocked:
            print(f"🔒 {self.language_used} is locked! Reach required level first.")
            return False
        return True

    def submit_code(self, code: str, judge0_result: Judge0Result) -> dict:
        """
        Process a code submission.
        judge0_result comes from Judge0 API (api/judge0.py)
        """
        self.submitted_code = code
        self.rounds += 1
        self.judge0_results.append(judge0_result)

        judge0_result.show()

        # Calculate damage
        dmg_to_enemy = judge0_result.damage_to_enemy(self.player.attack)
        dmg_to_player = judge0_result.damage_to_player(self.enemy.attack)

        # Apply damage
        if dmg_to_enemy > 0:
            self.enemy.take_damage(dmg_to_enemy)
            self.damage_dealt += dmg_to_enemy
            print(f"⚔️  You deal {dmg_to_enemy} damage to {self.enemy.name}! "
                  f"({self.enemy.hp}/{self.enemy.max_hp} HP)")

        if dmg_to_player > 0:
            self.player.take_damage(dmg_to_player)
            print(f"💥 {self.enemy.name} deals {dmg_to_player} damage to you! "
                  f"({self.player.hp}/{self.player.max_hp} HP)")

        # Check battle outcome
        if not self.enemy.is_alive():
            self._on_win()
        elif not self.player.is_alive():
            self._on_lose()

        return {
            "verdict": judge0_result.verdict,
            "dmg_to_enemy": dmg_to_enemy,
            "dmg_to_player": dmg_to_player,
            "battle_over": not self.enemy.is_alive() or not self.player.is_alive()
        }

    def player_runs(self):
        self.result = "ran"
        print("🏃 You ran away from the battle!")

    def _on_win(self):
        self.result = "win"
        loot = self.enemy.drop_loot()
        self.player.gold += loot["gold"]
        print(f"\n🏆 Victory! You defeated {self.enemy.name}!")
        print(f"💰 +{loot['gold']} gold | Total: {self.player.gold}")
        # Level up every 3 wins (simple logic)
        if self.player.gold % 30 == 0:
            self.player.level_up()

    def _on_lose(self):
        self.result = "lose"
        print(f"\n💀 You were defeated by {self.enemy.name}... Game Over.")

    def is_over(self) -> bool:
        return self.result != "pending"

    def show_status(self):
        print(f"\n--- Round {self.rounds} ---")
        print(f"  {self.player.name}: {self.player.hp}/{self.player.max_hp} HP")
        print(f"  {self.enemy.name}: {self.enemy.hp}/{self.enemy.max_hp} HP")
        print(f"  Language: {self.language_used}")

    def to_dict(self) -> dict:
        return {
            "battle_id": self.battle_id,
            "player_id": self.player.player_id,
            "enemy_id": self.enemy.enemy_id,
            "task_id": self.task.task_id,
            "language_used": self.language_used,
            "submitted_code": self.submitted_code,
            "result": self.result,
            "damage_dealt": self.damage_dealt,
            "time_limit_sec": self.time_limit_sec,
            "memory_limit_mb": self.memory_limit_mb,
            "rounds": self.rounds
        }

    def __repr__(self):
        return (f"Battle(player={self.player.name}, "
                f"enemy={self.enemy.name}, "
                f"result={self.result})")
