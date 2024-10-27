import requests
from bs4 import BeautifulSoup

def search_query(query):
    # Construct the search URL
    search_url = f"https://www.google.com/search?q={query}"
    
    # Send the GET request to the search URL
    response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"})
    
    # Check if the request was successful
    if response.status_code != 200:
        return "Error: Unable to fetch search results."
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the search result snippets
    snippets = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    
    # Extract and return the text of the first snippet
    if snippets:
        return snippets[0].get_text()
    else:
        return "No results found."

# Example usage
if __name__ == "__main__":
    query = input("Enter your query: ")
    result = search_query(query)
    print(f"Search result: {result}")
