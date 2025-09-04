import httpx
from bs4 import BeautifulSoup

async def extract_text_from_url(url: str) -> str:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            # Basic: extract all paragraph text
            paragraphs = soup.find_all("p")
            text = "\n".join(p.get_text() for p in paragraphs if p.get_text())
            return text
    except Exception as e:
        return ""
