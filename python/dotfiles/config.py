from dataclasses import dataclass


@dataclass
class Config:
    
    container_dir: str = "./data"
    tracked_file: str = "./tracked.lst"


config = Config()
