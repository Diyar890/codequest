from game import (
    Player, Enemy, Boss, Task, TASK_BANK,
    Battle, Judge0Result, Inventory, Item,
    ITEM_CATALOG, GameSave
)

def test_all():
    print("\n" + "="*50)
    print("  CodeQuest — OOP Phase 2 Test")
    print("="*50)

    # ── 1. PLAYER ──────────────────────────────────
    print("\n[1] PLAYER")
    hero = Player("Arlan")
    hero.show_stats()

    # ── 2. ENEMY ───────────────────────────────────
    print("\n[2] ENEMY")
    slime = Enemy("Two-Sum Slime", hp=40, attack=10,
                  gold_reward=15, difficulty="Easy")
    slime.show_stats()

    # ── 3. BOSS ────────────────────────────────────
    print("\n[3] BOSS (inherits Enemy)")
    dragon = Boss("Tree-Sum Monster", hp=150, attack=25,
                  gold_reward=80, difficulty="Medium",
                  time_limit=60, memory_limit=256)
    dragon.show_stats()

    # ── 4. TASK ────────────────────────────────────
    print("\n[4] TASK")
    task = TASK_BANK[0]  # Two Sum
    task.show()

    # ── 5. JUDGE0_RESULT ───────────────────────────
    print("\n[5] JUDGE0_RESULT")
    result_ok = Judge0Result(
        battle_id=1,
        verdict=Judge0Result.ACCEPTED,
        tests_passed=5,
        tests_total=5,
        exec_time=0.042
    )
    result_ok.show()
    print(f"   Damage to enemy: {result_ok.damage_to_enemy(hero.attack)}")
    print(f"   Damage to player: {result_ok.damage_to_player(slime.attack)}")

    result_tle = Judge0Result(
        battle_id=1,
        verdict=Judge0Result.TIME_LIMIT,
        tests_passed=2,
        tests_total=5,
        exec_time=61.0
    )
    result_tle.show()
    print(f"   Damage to enemy: {result_tle.damage_to_enemy(hero.attack)}")
    print(f"   Damage to player: {result_tle.damage_to_player(slime.attack)}")

    # ── 6. BATTLE ──────────────────────────────────
    print("\n[6] BATTLE (Core)")
    battle = Battle(hero, slime, task, language_used="Python")
    print(f"   Language valid: {battle.validate_language()}")
    battle.show_status()

    # Simulate accepted submission
    print("\n   Submitting correct solution...")
    outcome = battle.submit_code(
        code="def two_sum(nums, target): pass",
        judge0_result=result_ok
    )
    print(f"   Battle over: {outcome['battle_over']}")
    print(f"   Result: {battle.result}")
    print(f"   {battle}")

    # ── 7. ITEM + INVENTORY ────────────────────────
    print("\n[7] ITEM + INVENTORY")
    potion = ITEM_CATALOG[0]  # Clean Code Potion
    shield = ITEM_CATALOG[1]  # Compilation Shield
    print(f"   {potion.get_description()}")
    print(f"   {shield.get_description()}")
    print(f"   Equippable: {shield.is_equippable()}")

    hero.take_damage(40)
    print(f"   HP before potion: {hero.hp}")
    msg = potion.use(hero)
    print(f"   {msg}")
    print(f"   HP after potion: {hero.hp}")

    # ── 8. GAME_SAVE ───────────────────────────────
    print("\n[8] GAME_SAVE")
    save = GameSave(player_id=hero.player_id)
    save.save_game(hero)

    hero2 = Player("Empty")
    save.load_game(hero2)
    print(f"   Loaded: {hero2}")

    print("\n" + "="*50)
    print("  ✅ All 8 classes tested successfully!")
    print("="*50)


if __name__ == "__main__":
    test_all()
