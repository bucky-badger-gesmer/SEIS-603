import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("Player Shooting.csv")

# Ensure 'fg_percent' is numeric and handle potential missing values
df["fg_percent"] = pd.to_numeric(df["fg_percent"], errors="coerce")
df.dropna(subset=["fg_percent"], inplace=True)

# Filter out players with very low minutes (MP)
df_filtered = df[df["mp"] >= 200].copy()

# Simplify positions
valid_positions = ["C", "PF", "SF", "SG", "PG"]
df_filtered["pos"] = df_filtered["pos"].apply(
    lambda x: x.split("-")[0] if isinstance(x, str) else x
)
df_filtered = df_filtered[df_filtered["pos"].isin(valid_positions)]

# Sort by position
pos_order = ["C", "PF", "SF", "SG", "PG"]
df_filtered["pos"] = pd.Categorical(
    df_filtered["pos"], categories=pos_order, ordered=True
)
df_filtered.sort_values("pos", inplace=True)

# Create the interactive box plot with Plotly
fig = px.box(
    df_filtered,
    x="pos",
    y="fg_percent",
    color="pos",
    points="all",  # show all data points (outliers + others)
    hover_data={
        "player": True,
        "team": True,
        "season": True,
        "fg_percent": ":.3f",
        "pos": False,  # Hide redundant position info in tooltip
    },
    title="Distribution of Field Goal Percentage (FG%) by Player Position",
)

# Add a horizontal line for median FG%
median_fg = df_filtered["fg_percent"].median()
fig.add_hline(
    y=median_fg,
    line_dash="dash",
    line_color="red",
    annotation_text=f"Overall Median FG%: {median_fg:.3f}",
    annotation_position="bottom right",
)

# Adjust axis labels
fig.update_layout(
    xaxis_title="Player Position",
    yaxis_title="Field Goal Percentage (FG%)",
    yaxis_range=[0.2, 0.75],
    template="plotly_white",
)

# Show the plot
fig.show()

# --- Identify high-end outliers (same as before) ---
Q1 = df_filtered["fg_percent"].quantile(0.25)
Q3 = df_filtered["fg_percent"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

high_fg_outliers = df_filtered[df_filtered["fg_percent"] > upper_bound]
high_fg_outliers_sorted = high_fg_outliers.sort_values(
    by="fg_percent", ascending=False
)

print("\n--- Top High-End Outliers (Players with exceptionally high FG%) ---")
print(
    high_fg_outliers_sorted[
        ["player", "season", "team", "pos", "fg_percent", "mp"]
    ]
    .head(10)
    .to_markdown(index=False)
)
