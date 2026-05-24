class Judge0Result:
    # Verdict constants
    ACCEPTED = "Accepted"
    WRONG_ANSWER = "Wrong Answer"
    TIME_LIMIT = "Time Limit Exceeded"
    MEMORY_LIMIT = "Memory Limit Exceeded"
    COMPILATION_ERROR = "Compilation Error"
    RUNTIME_ERROR = "Runtime Error"

    def __init__(self, battle_id: int, verdict: str,
                 tests_passed: int, tests_total: int,
                 stderr: str = "", exec_time: float = 0.0):
        self.result_id: int = id(self)
        self.battle_id: int = battle_id
        self.verdict: str = verdict
        self.tests_passed: int = tests_passed
        self.tests_total: int = tests_total
        self.stderr: str = stderr
        self.exec_time: float = exec_time

    def is_accepted(self) -> bool:
        return self.verdict == self.ACCEPTED

    def damage_to_enemy(self, player_attack: int) -> int:
        """Calculate damage based on how many test cases passed"""
        if self.verdict == self.ACCEPTED:
            return player_attack * 2         # Full solution → big damage
        ratio = self.tests_passed / max(self.tests_total, 1)
        return int(player_attack * ratio)    # Partial → partial damage

    def damage_to_player(self, enemy_attack: int) -> int:
        """Enemy attacks player on wrong/error verdicts"""
        if self.verdict == self.ACCEPTED:
            return 0
        elif self.verdict == self.TIME_LIMIT:
            return enemy_attack * 2          # TLE → heavy punishment
        elif self.verdict == self.MEMORY_LIMIT:
            return enemy_attack + 10
        elif self.verdict == self.COMPILATION_ERROR:
            return enemy_attack // 2         # CE → reduced (shield can block)
        return enemy_attack

    def show(self):
        icon = "✅" if self.is_accepted() else "❌"
        print(f"\n{icon} Judge0 Result: {self.verdict}")
        print(f"   Tests: {self.tests_passed}/{self.tests_total} passed")
        print(f"   Time:  {self.exec_time:.3f}s")
        if self.stderr:
            print(f"   Error: {self.stderr[:100]}")

    def to_dict(self) -> dict:
        return {
            "result_id": self.result_id,
            "battle_id": self.battle_id,
            "verdict": self.verdict,
            "tests_passed": self.tests_passed,
            "tests_total": self.tests_total,
            "stderr": self.stderr,
            "exec_time": self.exec_time
        }

    def __repr__(self):
        return (f"Judge0Result(verdict={self.verdict}, "
                f"tests={self.tests_passed}/{self.tests_total})")
