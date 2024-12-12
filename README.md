# Web Crawler with Keyword Filtering

This Python script is a simple web crawler that recursively scrapes URLs from a given starting point and filters them based on a provided keyword. It uses the `requests` and `BeautifulSoup` libraries to fetch and parse HTML content and avoids visiting duplicate URLs.

## Features
- Recursively finds and prints URLs from a starting webpage.
- Filters URLs based on a user-specified keyword.
- Avoids revisiting already visited URLs to improve efficiency.
- Handles invalid or unreachable URLs gracefully.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python3 crawler.py
```

3. Enter the target URL and the keyword to search for when prompted:

```
Enter the URL you want to scrap: https://example.com
Enter the keyword to search for in the URL provided: blog
```

4. The script will recursively crawl the provided URL, find all links, and print links containing the keyword:

```
https://example.com/blog
https://example.com/blog/post1
```

## Code Overview

### Modules Used
- `requests`: To send HTTP GET requests.
- `BeautifulSoup` (from `bs4`): To parse and extract HTML elements.
- `urljoin` (from `urllib.parse`): To resolve relative URLs into absolute ones.

### Key Functions

#### `link_urls(url, keyword)`
- Accepts a URL and a keyword as input.
- Checks if the target URL is reachable.
- Uses BeautifulSoup to extract all `<a>` tags and their `href` attributes.
- Recursively follows links, filtering based on the provided keyword.
- Avoids revisiting previously visited URLs using a `set`.

## Example Output

When crawling `https://example.com` for the keyword `blog`, the script will print:

```
https://example.com/blog
https://example.com/blog/about
https://example.com/blog/post
```

## Notes

- Ensure the provided URL includes the protocol (`http` or `https`).
- Use responsibly: avoid overloading websites with frequent or large-scale crawling.
- The script does not currently handle JavaScript-rendered content or robots.txt restrictions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## References

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [URL Parsing with `urljoin`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin)

