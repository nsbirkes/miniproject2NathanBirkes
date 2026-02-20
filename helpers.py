import os
import random
import pandas as pd
import matplotlib.pyplot as plt
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
                "age": round(random.uniform(20, 40), 2), # Range = 20 - 40 years old
            }
        )

    df = pd.DataFrame(rows)

    return df


def create_charts(df: pd.DataFrame) -> None:
    """
    Creates 3 charts based on the dataframe data we generated.

    Params
    --------
    df: pd.DataFrame
        Dataframe with the fake data that gets created from the `get_fake_data(n)` function.
    """

    os.makedirs("charts", exist_ok=True)

    # ***** Scatter plot of ave vs salary *****
    plt.figure(figsize=(10, 6))

    # Plotting data on the scatter, for each league
    for league in df["league"].unique():
        subset = df[df["league"] == league]
        plt.scatter(subset["age"], subset["salary"], label=league, alpha=0.7)

    # labels and titles
    plt.title("Athlete Salary vs Age")
    plt.xlabel("Age")
    plt.ylabel("Salary (Millions USD)")
    plt.legend()
    plt.tight_layout()

    # saving
    plt.savefig("charts/salary_vs_age_scatter.png", dpi=200)
    plt.close()

    # ***** Pie chart - share of total salary between leagues *****
    salary_by_league = df.groupby("league")["salary"].sum()

    plt.figure(figsize=(10, 6))
    
    # Making the chart cleaner
    salary_by_league.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=140,
        colors=["#1f77b4", "#ff7f0e", "#2ca02c"],
        wedgeprops={"edgecolor": "white", "linewidth": 1}
    )

    # labels and titles
    plt.title("Total Salary Share by League")
    plt.ylabel("")
    plt.tight_layout()
    
    # saving
    plt.savefig("charts/league_salary_share_pie.png", dpi=200)
    plt.close()

    # ***** Bar chart — average salary by league *****
    avg_salary = df.groupby("league")["salary"].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    
    # Making the chart cleaner
    avg_salary.plot(
        kind="bar",
        color=["#1f77b4", "#ff7f0e", "#2ca02c"],
        edgecolor="black",
        linewidth=0.5
    )
    
    # labels and titles
    plt.title("Average Salary by League")
    plt.xlabel("League")
    plt.ylabel("Salary (Millions USD)")
    plt.tight_layout()

    # saving
    plt.savefig("charts/avg_salary_by_league.png", dpi=200)
    plt.close()
