Hacker News data.

Analyzed because Show HN seems to be increasing recently(late 2025).

Data (`hn.csv` used in `main.py`) was retrieved from [BigQuery](https://console.cloud.google.com/marketplace/product/y-combinator/hacker-news) using this query:

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
