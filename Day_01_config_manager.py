from dataclasses import dataclass

@dataclass(frozen=True)
class DatasetConfig:
    dataset_name: str
    train_path: str
    batch_size: int
    num_classes: int

ai_config = DatasetConfig(
    dataset_name =  "Cat Vs Dog",
    train_path="/data/train",
    batch_size=32,
    num_classes=2
)

print("AI config Loaded Successfully.")
print(ai_config)