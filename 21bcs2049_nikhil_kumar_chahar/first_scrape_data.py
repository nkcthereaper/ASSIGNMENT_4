import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all article elements
    articles = []
    for item in soup.find_all('article'):
        # Extract the title
        title_tag = item.find('h2')
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            continue
        
        # Extract the link
        link_tag = item.find('a', href=True)
        if link_tag:
            link = link_tag['href']
        else:
            continue
        
        # Ensure the link is a full URL
        if not link.startswith('http'):
            link = 'https://www.spiegel.de' + link
        
        articles.append({'title': title, 'link': link})
    
    return articles

def save_to_text_file(articles, filename):
    full_path = r'C:\Users\nikhilchahar\Desktop\NLP CLASS\\' + filename
    with open(full_path, 'w', encoding='utf-8') as f:
        for article in articles:
            f.write(f"Title: {article['title']}\n")
            f.write(f"Link: {article['link']}\n")
            f.write("-" * 80 + "\n")

if __name__ == "__main__":
    url = 'https://www.spiegel.de/international/'
    articles = scrape_articles(url)
    
    # Save the scraped articles to a text file in the specified directory
    save_to_text_file(articles, 'assignment_5_data.txt')

    print(f"Saved {len(articles)} articles to C:\\Users\\nikhilchahar\\Desktop\\NLP CLASS\\assignment_5_data.txt")
