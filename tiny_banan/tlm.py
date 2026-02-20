import tiktoken
import os
import numpy as np
from tqdm.auto import tqdm
from datasets import load_dataset

ds = load_dataset("roneneldan/TinyStories")

