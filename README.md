Recently, I felt like I was seeing more "Show HN" stories, and many of which were generated with LLMs.

So I analyzed the data to see if that was true.

I included the average score per month to see if people enjoy seeing them(because I don't :P).

## Charts

`story` includes `show_hn`.

Left axis: `show_hn / story * 100`

Right axis: average scores

![Chart](https://github.com/user-attachments/assets/687db895-b99b-4fc0-aba3-681489473b7b)

With LLM timeline

![Chart with LLM timeline](https://github.com/user-attachments/assets/73f2b39f-1999-4194-a101-e44d722e1b51)

## Result

Disclaimer: I am neither a data scientist nor a statistician. Some nuances may have been lost in translation.

For about ten years (2012~2022), the percentage of Show HN stories was around 2-3%. Then, it has increased with the appearance of LLMs that can code. Even more since Claude Code and Cursor 1.0. As of December 2025, over 12% of all stories are Show HNs.

People can create things even if they don't know how to code. So I am pretty sure there is a correlation between the increase in Show HN posts and LLM.

However, their average scores are declining. Show HN stories used to receive similar scores (around 15-18) to those of all stories until 2023~2024. However, as of December 2025, the average Show HN score is 10 points lower (9.04 vs 19.53). Though I'm not sure it's because LLM-generated Show HNs are lower quality. Maybe people don't like/trust LLM-generated products, regardless of their quality.

## Data

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

I didn't commit the original CSV because it was too big (~400 MB) but you can download it from BigQuery free(I think?). I ran SQL, exported it to google drive, and downloaded it.

The "type" field in BigQuery does not have a "show_hn" attribute like the Algolia API, so I lowercased titles and filtered using [`starts_with("show_hn: ")`](https://docs.pola.rs/api/python/dev/reference/expressions/api/polars.Expr.str.starts_with.html) to determine if a post is a Show HN story.

Ideally, I would like to analyze the percentage of Show HN stories generated with LLMs. I couldn't find the way to do this, because many Show HN stories don't mention that they've used LLMs in their OP.

---

I used deepl write/translator to write this. If this text sounds like LLM-generated, I am sorry, I'm not just good at writing in English.
