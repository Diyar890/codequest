import json
import os
from datetime import datetime


class GameSave:
    SAVE_PATH = "saves/save.json"

    def __init__(self, player_id: int):
        self.save_id: int = id(self)
        self.player_id: int = player_id
        self.timestamp: str = ""
        self.game_state: dict = {}

    def save_game(self, player) -> bool:
        """Save player state to JSON file"""
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.game_state = player.to_dict()

        data = {
            "save_id": self.save_id,
            "player_id": self.player_id,
            "timestamp": self.timestamp,
            "game_state": self.game_state
        }

        os.makedirs("saves", exist_ok=True)
        with open(self.SAVE_PATH, "w") as f:
            json.dump(data, f, indent=2)

        print(f"💾 Game saved! [{self.timestamp}]")
        return True

    def load_game(self, player) -> bool:
        """Load player state from JSON file"""
        try:
            with open(self.SAVE_PATH, "r") as f:
                data = json.load(f)

            state = data["game_state"]
            player.name = state["name"]
            player.hp = state["hp"]
            player.max_hp = state["max_hp"]
            player.attack = state["attack"]
            player.level = state["level"]
            player.gold = state["gold"]
            self.timestamp = data["timestamp"]

            print(f"✅ Game loaded! [{self.timestamp}]")
            return True

        except FileNotFoundError:
            print("❌ No save file found.")
            return False
        except (KeyError, json.JSONDecodeError) as e:
            print(f"❌ Save file corrupted: {e}")
            return False

    def delete_save(self) -> bool:
        """Delete save file"""
        if os.path.exists(self.SAVE_PATH):
            os.remove(self.SAVE_PATH)
            print("🗑️  Save deleted.")
            return True
        print("No save file to delete.")
        return False

    def to_dict(self) -> dict:
        return {
            "save_id": self.save_id,
            "player_id": self.player_id,
            "timestamp": self.timestamp,
            "game_state": self.game_state
        }

    def __repr__(self):
        return f"GameSave(player_id={self.player_id}, timestamp={self.timestamp})"
