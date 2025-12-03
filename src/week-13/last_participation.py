# if you see any T's drop the entire row
# Read CSV put it in a database
# part 2 make some cool data visualization!


import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


def put_data_into_sqlite_db():
    conn = sqlite3.connect("temperatures.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Temperatures")

    cur.execute("""
    CREATE TABLE Temperatures (date DATE, max_temp FLOAT, min_temp FLOAT, precipitation FLOAT, snow FLOAT, snow_depth FLOAT)""")

    fh = open("DataDownloadCSV.csv")

    next(fh)

    for line in fh:
        pieces = line.rstrip().split(",")
        cleaned_pieces = [piece.strip('"') for piece in pieces]

        date = cleaned_pieces[0]
        max_temp = cleaned_pieces[1]
        min_temp = cleaned_pieces[2]
        precipitation = cleaned_pieces[3]
        snow = cleaned_pieces[4]
        snow_depth = cleaned_pieces[5]

        # avoid any bad values:
        if precipitation == "T" or snow == "T" or snow_depth == "T":
            continue

        cur.execute(
            "SELECT * FROM Temperatures WHERE date = ? ", (date,)
        )  # parameterize
        row = cur.fetchone()
        if row is None:
            cur.execute(
                """INSERT INTO Temperatures (date, max_temp, min_temp, precipitation, snow, snow_depth)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    date,
                    max_temp,
                    min_temp,
                    precipitation,
                    snow,
                    snow_depth,
                ),
            )
        conn.commit()

    cur.close()


def read_from_db_to_df_visualize():
    conn = sqlite3.connect("temperatures.sqlite")
    df = pd.read_sql_query("SELECT * FROM Temperatures", conn)
    conn.close()

    print(df.head())
    print(f"\nDataFrame successfully loaded with {len(df)} rows.")

    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # Create a figure with 3 subplots (3 rows, 1 column)
    # sharex=True ensures all plots use the same date axis
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    fig.suptitle(
        "Daily Weather Metrics Analysis (Combined Plots)", fontsize=16
    )

    # --- Plot 1: Temperatures ---
    df[["max_temp", "min_temp"]].plot(ax=ax1, marker="o")
    ax1.set_title("Temperature Trends")
    ax1.set_ylabel("Temperature (C°)")
    ax1.legend(loc="upper left")
    ax1.grid(True)
    ax1.set_xlabel("")

    # --- Plot 2: Precipitation ---
    df["precipitation"].plot(ax=ax2, marker="o", color="green")
    ax2.set_title("Daily Precipitation")
    ax2.set_ylabel("Precipitation (mm)")
    ax2.legend(loc="upper left")
    ax2.grid(True)
    ax2.set_ylim(bottom=0)
    ax2.set_xlabel("")

    # --- Plot 3: Snow and Snow Depth ---
    df[["snow", "snow_depth"]].plot(ax=ax3, marker="o")
    ax3.set_title("Daily Snowfall and Snow Depth")
    ax3.set_ylabel("Depth/Amount (cm)")
    ax3.legend(loc="upper left")
    ax3.grid(True)
    ax3.set_ylim(bottom=0)

    # Final Touches
    ax3.set_xlabel("Date")  # Only label the bottom X-axis
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout for main title
    plt.savefig("combined_weather_plots.png")


if __name__ == "__main__":
    # put_data_into_sqlite_db()
    read_from_db_to_df_visualize()
