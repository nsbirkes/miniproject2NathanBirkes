import os
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from faker import Faker


def get_fake_data(n: int) -> pd.DataFrame:
    """
    Generates a fake dataset of top pro sports athletes and their salaries in millions.
    
    Params
    --------
    n: int
        Amount of athletes to be listed
    
    Returns
    --------
    pd.Dataframe
        Dateframe object with a list of atheltes, their league, and their salary
    """

    # Start the faker library and attatch it to our variable
    fake = Faker()

    # 3 different leagues the athletes will be randimized too
    leagues = ["NFL", "NBA", "MLB"]

    rows = []
    
    # creating our n number of athletes
    for i in range(n):
        rows.append(
            {
                "name": f"{fake.first_name_male()} {fake.last_name()}", # First Last
                "league": random.choice(leagues), #  NFL, NBA, or MLB
                "salary": round(random.uniform(30, 120), 2), # Range = 30 - 120 mil
            }
        )

    df = pd.DataFrame(rows)
    
    return df
