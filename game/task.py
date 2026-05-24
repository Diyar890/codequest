class Task:
    def __init__(self, title: str, description: str,
                 difficulty: str, test_input: str,
                 expected_output: str, topic: str,
                 time_limit_sec: int = 60,
                 memory_limit_mb: int = 256):
        self.task_id: int = id(self)
        self.title: str = title
        self.description: str = description
        self.difficulty: str = difficulty       # "Easy", "Medium", "Hard"
        self.test_input: str = test_input
        self.expected_output: str = expected_output
        self.topic: str = topic                 # "Arrays", "Strings", "Trees"
        self.time_limit_sec: int = time_limit_sec
        self.memory_limit_mb: int = memory_limit_mb

    def show(self):
        print(f"\n{'='*40}")
        print(f"  🧠 {self.title} [{self.difficulty}]")
        print(f"{'='*40}")
        print(f"  Topic: {self.topic}")
        print(f"  {self.description}")
        print(f"\n  Input:    {self.test_input}")
        print(f"  Expected: {self.expected_output}")
        print(f"\n  ⏱️  Time limit:   {self.time_limit_sec}s")
        print(f"  💾 Memory limit: {self.memory_limit_mb}MB")
        print(f"{'='*40}")

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "difficulty": self.difficulty,
            "test_input": self.test_input,
            "expected_output": self.expected_output,
            "topic": self.topic,
            "time_limit_sec": self.time_limit_sec,
            "memory_limit_mb": self.memory_limit_mb
        }

    def __repr__(self):
        return f"Task(title={self.title}, difficulty={self.difficulty})"


# Built-in task bank (Easy tasks to start)
TASK_BANK = [
    Task(
        title="Two Sum",
        description="Given a list of numbers and a target, return indices of two numbers that add up to target.",
        difficulty="Easy",
        test_input="nums = [2, 7, 11, 15], target = 9",
        expected_output="[0, 1]",
        topic="Arrays",
        time_limit_sec=60,
        memory_limit_mb=256
    ),
    Task(
        title="Reverse String",
        description="Write a function that reverses a string.",
        difficulty="Easy",
        test_input='"hello"',
        expected_output='"olleh"',
        topic="Strings",
        time_limit_sec=30,
        memory_limit_mb=128
    ),
    Task(
        title="FizzBuzz",
        description="Print numbers 1 to n. For multiples of 3 print Fizz, for 5 print Buzz, for both print FizzBuzz.",
        difficulty="Easy",
        test_input="n = 15",
        expected_output="1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz",
        topic="Loops",
        time_limit_sec=30,
        memory_limit_mb=128
    ),
    Task(
        title="Binary Search",
        description="Given a sorted array and target, return the index using binary search. Return -1 if not found.",
        difficulty="Medium",
        test_input="nums = [1, 3, 5, 7, 9], target = 5",
        expected_output="2",
        topic="Search",
        time_limit_sec=60,
        memory_limit_mb=256
    ),
]
