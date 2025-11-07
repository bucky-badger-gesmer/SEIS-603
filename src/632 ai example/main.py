import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the dataset
df = pd.read_csv("Player Shooting.csv")

# Ensure 'fg_percent' is numeric and handle potential missing values
df["fg_percent"] = pd.to_numeric(df["fg_percent"], errors="coerce")
df.dropna(subset=["fg_percent"], inplace=True)

# Filter out players with very low minutes (MP) to focus on those with a meaningful sample size
# Using a threshold of at least 200 minutes played
df_filtered = df[df["mp"] >= 200].copy()

# Create a list of the primary positions to include for cleaner visualization
# Drop rows where 'pos' is not one of the main 5 or a combo, simplifying to C, PF, SF, SG, PG
valid_positions = ["C", "PF", "SF", "SG", "PG"]
df_filtered["pos"] = df_filtered["pos"].apply(
    lambda x: x.split("-")[0] if isinstance(x, str) else x
)
df_filtered = df_filtered[df_filtered["pos"].isin(valid_positions)]

# Sort the data by 'pos' for a better visual order (Center to Guard)
pos_order = ["C", "PF", "SF", "SG", "PG"]
df_filtered["pos"] = pd.Categorical(
    df_filtered["pos"], categories=pos_order, ordered=True
)
df_filtered.sort_values("pos", inplace=True)

# Initialize the plot
plt.figure(figsize=(12, 8))

# Create the box plot using Seaborn to highlight outliers
# Outliers are the individual points (dots) that lie beyond the whiskers
sns.boxplot(
    x="pos",
    y="fg_percent",
    data=df_filtered,
    palette="viridis",
    showfliers=True,  # Ensure outliers are shown
)

# Add titles and labels
plt.title(
    "Distribution of Field Goal Percentage (FG%) by Player Position",
    fontsize=16,
)
plt.xlabel("Player Position", fontsize=14)
plt.ylabel("Field Goal Percentage (FG%)", fontsize=14)

# Enhance the plot appearance
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.ylim(0.2, 0.75)  # Set limits to focus on the common range and outliers
plt.axhline(
    df_filtered["fg_percent"].median(),
    color="red",
    linestyle="--",
    linewidth=1,
    label=f"Overall Median FG%: {df_filtered['fg_percent'].median():.3f}",
)

# Add a legend
plt.legend()

# Display the plot
plt.show()

# --- Identifying the specific outliers for context ---
# The IQR method (used in boxplots) for outlier detection: Q3 + 1.5 * IQR or Q1 - 1.5 * IQR

# Calculate general upper threshold for FG% outliers
Q1 = df_filtered["fg_percent"].quantile(0.25)
Q3 = df_filtered["fg_percent"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

# Find the players who are high-end outliers in FG%
high_fg_outliers = df_filtered[df_filtered["fg_percent"] > upper_bound]
high_fg_outliers_sorted = high_fg_outliers.sort_values(
    by="fg_percent", ascending=False
)

print(
    "\n--- Top High-End Outliers (Players with exceptionally high FG% relative to the overall distribution) ---"
)
print(
    high_fg_outliers_sorted[
        ["player", "season", "team", "pos", "fg_percent", "mp"]
    ]
    .head(10)
    .to_markdown(index=False)
)
