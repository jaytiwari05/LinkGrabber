# Link Grabber for Bug Hunters

This Python script is a tool designed specifically for bug hunters and penetration testers. It helps in identifying URLs of interest on a target website and verifying their status, making it an essential asset during the reconnaissance phase of a security assessment.

## Features
- **Recursive Crawling**: Automatically traverses all linked pages on a target domain.
- **Keyword Filtering**: Outputs only URLs containing a specific keyword, helping focus on areas of interest.
- **Duplicate Avoidance**: Uses a `set` to ensure the same URL is not visited multiple times.
- **Robust Error Handling**: Handles unreachable URLs gracefully.
- **URL Validation and Filtering**: Validates a list of URLs and saves the valid ones to a file.

## Prerequisites

Ensure you have the following installed before running the script:

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

Install the required libraries with:

```bash
pip install requests beautifulsoup4
```

## Usage

### 1. Link Crawler with Keyword Filtering

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python3 linkGrabber.py
```

3. Input the target URL and the keyword to filter URLs:

```
Enter the URL you want to scrap: https://example.com
Enter the keyword to search for in the URL provided: login
```

4. The script will recursively scrape URLs and print only those containing the keyword:

```
https://example.com/login
https://example.com/admin/login
https://example.com/user/login
```

### 2. URL Validation and Filtering

You can use the additional functionality to validate a list of URLs and save the valid ones:

1. Provide a list of URLs through standard input (e.g., by piping or redirecting from a file):

```bash
echo -e "https://example.com\nhttps://invalid.url" | python3 probe.py
```

2. The script will:
   - Check the HTTP status of each URL.
   - Save URLs with a status code of 200 to a file named `filtered_url.txt`.

3. Example output:

```
Saved URLs to filtered_url.txt
```

## Code Overview

### Modules Used
- **`requests`**: Sends HTTP GET and HEAD requests to the target site.
- **`BeautifulSoup` (from `bs4`)**: Parses and extracts HTML elements from the page.
- **`urljoin` (from `urllib.parse`)**: Resolves relative URLs to absolute ones.
- **`sys`**: Handles command-line input and output.

### Key Functions

#### `link_urls(url, keyword)`
- Checks if the target URL is reachable.
- Extracts all `<a>` tags and retrieves their `href` attributes.
- Recursively crawls linked pages while filtering URLs based on the keyword.
- Avoids revisiting previously crawled URLs using a `set`.

#### `url(out_file)`
- Reads a list of URLs from standard input.
- Validates each URL using an HTTP HEAD request.
- Saves URLs with a status code of 200 to the specified output file.

## Example Output

### Crawling and Filtering

For the target `https://example.com` with the keyword `admin`, the script may output:

```
https://example.com/admin
https://example.com/admin/login
https://example.com/admin/dashboard
```

### URL Validation

Input:
```
https://example.com
https://invalid.url
```

Output:
```
Saved URLs to filtered_url.txt
```

Contents of `filtered_url.txt`:
```
https://example.com
```

## Notes for Ethical Use
- Always ensure you have permission to test the target domain.
- Abide by the rules set in the `robots.txt` file of the target website.
- Be cautious to avoid overwhelming the target server with excessive requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Bug hunters and security enthusiasts are welcome to contribute. Feel free to fork the repository and submit pull requests for new features or bug fixes.

## References

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [URL Parsing with `urljoin`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin)

<img width="1218" alt="Screenshot 2024-12-13 at 2 36 29 AM" src="https://github.com/user-attachments/assets/1a4c1d09-0f49-45b7-b4c0-4a80842fb07e" />
