Show HN percentage. Read https://snubi.net/posts/Show-HN for more detailed analysis.

## Charts

Left axis: `show_hn_ratio`(`show_hn / story * 100`)

Right axis: `average_show_hn_score` and `average_story_score`

![Chart](images/without.jpg)

With LLM timeline

![Chart with LLM timeline](images/with.jpg)

## Data and codes

I exported [BigQuery hacker news data](https://console.cloud.google.com/marketplace/product/y-combinator/hacker-news) to csv using this query:

```sql
SELECT
  `time`,
  `title`,
  `type`,
  `score`,
  `id`
FROM
  `bigquery-public-data.hacker_news.full`
WHERE
  (`type` IN ('story')) and title IS NOT NULL;
```

The `type` field in BigQuery does not have a `show_hn` attribute like the Algolia API, so I lowercased titles and filtered using [`starts_with("show_hn: ")`](https://docs.pola.rs/api/python/dev/reference/expressions/api/polars.Expr.str.starts_with.html) to determine if a post is a Show HN story.

I didn't commit to the repo the original CSV because it was too big (~400 MB) but you can download it from BigQuery for free (I didn't set billing account). I ran SQL above, exported it to google drive, and downloaded it.
