import polars as pl


df = pl.read_csv("hn.csv")

df = df.with_columns(
    [
        # unfortunately I have to change booleans to `Y` and `N` to fit GitHub's 100mb size limit
        pl.when(pl.col("title").str.to_lowercase().str.starts_with("show hn: "))
        .then(pl.lit("y"))
        .otherwise(pl.lit("n"))
        .alias("is_show_hn")
    ]
)

df = df.sort("time")

df = df.with_columns(
    pl.from_epoch(pl.col("time"), time_unit="s")
    .dt.to_string("%Y-%m-%d")
    .alias("datetime")
)

df = df.drop("time")
df = df.drop("title")
df = df.drop("type")
df = df.drop("id")

df.write_csv("simple.csv")
