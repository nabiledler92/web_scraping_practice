# web_scraping_practice

Web scraping practice in Python: fetching pages with `requests`, parsing HTML with BeautifulSoup, and turning the result into pandas DataFrames.

## Notebooks

| Notebook | What it does |
| --- | --- |
| [`notebooks/Web-Scraping/Web Scraping Tutorial.ipynb`](notebooks/Web-Scraping/Web%20Scraping%20Tutorial.ipynb) | A step-by-step tutorial: HTML structure, Chrome DevTools, then scraping IMDb's homepage (titles, side bar, articles, links) and a Box Office Mojo table into a cleaned DataFrame. |
| [`googlemap_webscrape_pyb.ipynb`](googlemap_webscrape_pyb.ipynb) | Practice on a public Google My Maps page: finding the elements that hold the map's place list and extracting them. |

## What I practised

- Reading HTML and finding elements with Chrome DevTools
- `requests.get` and `BeautifulSoup` with `find` and `find_all`
- Pulling table rows into pandas, fixing headers and replacing missing values
- Collecting and de-duplicating links on a page

## Run it

Each notebook has an **Open in Colab** badge, or you can run it locally in Jupyter. Install the packages first:

```bash
pip install requests beautifulsoup4 pandas numpy matplotlib
```

Websites change their HTML over time, so some selectors in these notebooks may no longer match the live pages.

## Credit

The tutorial notebook is adapted from the [Nesta Innovation Mapping tutorials](https://github.com/nestauk/im-tutorials) (YSI web scraping tutorial).
