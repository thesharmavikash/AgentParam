import requests
from bs4 import BeautifulSoup
from agentscope.service import ServiceResponse

def scrape_url(url: str) -> ServiceResponse:
    """
    Fetches and extracts text content from a live URL.
    Useful for reading live documentation or tutorials.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        text = soup.get_text(separator=' ', strip=True)
        
        # Truncate to save context window (roughly 2000 words)
        return ServiceResponse(
            status=ServiceResponse.SUCCESS, 
            content=text[:10000] + "\n...(truncated)" if len(text) > 10000 else text
        )
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Failed to scrape {url}: {str(e)}")
