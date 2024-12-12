# Link Grabber for Bug Hunters

This Python script is a recursive web crawler designed specifically for bug hunters and penetration testers. It helps in identifying URLs of interest on a target website, filtered by a specified keyword. The script can be a valuable asset during the reconnaissance phase of a security assessment.

## Features
- **Recursive Crawling**: Automatically traverses all linked pages on a target domain.
- **Keyword Filtering**: Outputs only URLs containing a specific keyword, helping focus on areas of interest.
- **Duplicate Avoidance**: Uses a `set` to ensure the same URL is not visited multiple times.
- **Robust Error Handling**: Handles unreachable URLs gracefully.

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

## Use Cases for Bug Hunters

### 1. **Gathering Reconnaissance Data**
- Identify endpoints related to authentication, admin panels, or APIs.
- Narrow down the scope by focusing only on URLs matching specific keywords like `login`, `admin`, or `api`.

### 2. **Mapping the Attack Surface**
- Understand the structure of the target application.
- Discover hidden or less commonly accessed pages that could contain vulnerabilities.

### 3. **Automating Recon**
- Save time by automating the tedious task of manually finding links.
- Easily integrate this script into your reconnaissance pipeline.

## Code Overview

### Modules Used
- **`requests`**: Sends HTTP GET requests to the target site.
- **`BeautifulSoup` (from `bs4`)**: Parses and extracts HTML elements from the page.
- **`urljoin` (from `urllib.parse`)**: Resolves relative URLs to absolute ones.

### Key Function

#### `link_urls(url, keyword)`
- Checks if the target URL is reachable.
- Extracts all `<a>` tags and retrieves their `href` attributes.
- Recursively crawls linked pages while filtering URLs based on the keyword.
- Avoids revisiting previously crawled URLs using a `set`.

## Example Output

For the target `https://example.com` with the keyword `admin`, the script may output:

```
https://example.com/admin
https://example.com/admin/login
https://example.com/admin/dashboard
```
<img width="1218" alt="Screenshot 2024-12-13 at 2 36 29 AM" src="https://github.com/user-attachments/assets/1a4c1d09-0f49-45b7-b4c0-4a80842fb07e" />


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Bug hunters and security enthusiasts are welcome to contribute. Feel free to fork the repository and submit pull requests for new features or bug fixes.

## References

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [URL Parsing with `urljoin`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin)

