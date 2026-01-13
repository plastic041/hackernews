from datetime import datetime
import polars as pl

df = pl.read_csv("hn.csv")

df = df.with_columns([pl.from_epoch(pl.col("time"), time_unit="s").alias("datetime")])

df = df.with_columns([pl.col("datetime").dt.strftime("%Y-%m").alias("year_month")])

df = df.with_columns(
    [
        pl.col("title")
        .str.to_lowercase()
        .str.starts_with("show hn: ")
        .alias("is_show_hn")
    ]
)


result = (
    df.group_by("year_month")
    .agg(
        [
            pl.col("is_show_hn").sum().alias("show_hn_count"),
            pl.len().alias("stories_count"),
            (pl.len() - pl.col("is_show_hn").sum()).alias(
                "stories_without_show_hn_count"
            ),
            (pl.col("is_show_hn").sum() / pl.len()).alias("show_hn_ratio"),
            pl.col("score")
            .filter(pl.col("is_show_hn"))
            .mean()
            .alias("average_show_hn_score"),
            pl.col("score")
            .filter(~pl.col("is_show_hn"))
            .mean()
            .alias("average_non_show_hn_score"),
            pl.col("score").mean().alias("average_story_score"),
        ]
    )
    .sort("year_month")
)


# keep months that have no data
min_date = result.select(pl.col("year_month").min()).item()
max_date = result.select(pl.col("year_month").max()).item()

all_months = (
    pl.date_range(
        datetime.strptime(min_date, "%Y-%m"),
        datetime.strptime(max_date, "%Y-%m"),
        interval="1mo",
        eager=True,
    )
    .dt.strftime("%Y-%m")
    .alias("year_month")
)

all_months_df = pl.DataFrame({"year_month": all_months})

result = all_months_df.join(result, on="year_month", how="left").with_columns(
    [
        pl.col("show_hn_count").fill_null(0),
        pl.col("stories_count").fill_null(0),
        pl.col("stories_without_show_hn_count").fill_null(0),
        pl.col("show_hn_ratio").fill_null(0.0),
    ]
)

result = result.with_columns(
    [
        pl.col("show_hn_ratio").round(4),
        pl.col("average_show_hn_score").round(2),
        pl.col("average_non_show_hn_score").round(2),
        pl.col("average_story_score").round(2),
    ]
)

result.write_csv("output.csv")
