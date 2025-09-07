#!/usr/bin/env python3
"""
Documentation Crawler for Search and Filter
Crawls documentation pages and extracts main content for Claude project knowledge
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import time
import re
from urllib.parse import urljoin, urlparse
from pathlib import Path

class DocumentationCrawler:
    def __init__(self, base_url="https://searchandfilter.com/documentation/"):
        self.base_url = base_url
        self.visited_urls = set()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def get_page_content(self, url):
        """Fetch page content with error handling"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_main_content(self, html, url):
        """Extract main documentation content from HTML"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Common selectors for main content (adjust based on site structure)
        content_selectors = [
            'main',
            '.documentation-content',
            '.doc-content',
            '.content',
            'article',
            '.post-content',
            '#content'
        ]
        
        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break
        
        # Fallback: remove common unwanted elements
        if not main_content:
            main_content = soup
            
        # Remove unwanted elements
        unwanted_selectors = [
            'nav', 'header', 'footer', '.sidebar', '.menu',
            '.navigation', '.breadcrumb', 'script', 'style',
            '.social-share', '.comments', '.advertisement'
        ]
        
        for selector in unwanted_selectors:
            for element in main_content.select(selector):
                element.decompose()
        
        return main_content
    
    def get_all_doc_links(self, start_url):
        """Get all documentation page links"""
        html = self.get_page_content(start_url)
        if not html:
            return []
            
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        
        # Find all links that appear to be documentation pages
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(start_url, href)
            
            # Filter for documentation URLs
            if (self.base_url in full_url and 
                full_url not in self.visited_urls and
                not any(skip in full_url for skip in ['#', 'mailto:', 'tel:', '.pdf', '.zip'])):
                links.add(full_url)
        
        return list(links)
    
    def crawl_documentation(self, output_dir="docs_output"):
        """Main crawling function"""
        Path(output_dir).mkdir(exist_ok=True)
        
        print(f"Starting crawl of {self.base_url}")
        
        # Get initial list of documentation pages from the main docs page
        doc_links = self.get_all_doc_links(self.base_url)
        doc_links.append(self.base_url)  # Include the main docs page
        
        # Parse the main page to find specific documentation links from the organized sections
        main_html = self.get_page_content(self.base_url)
        if main_html:
            soup = BeautifulSoup(main_html, 'html.parser')
            
            # Find links in the organized documentation sections
            for post_title_link in soup.select('.wp-block-post-title a'):
                href = post_title_link.get('href')
                if href and self.base_url.replace('/documentation/', '') in href:
                    full_url = urljoin(self.base_url, href)
                    if '/documentation/' in full_url:
                        doc_links.append(full_url)
            
            # Also check for any other documentation links in the content
            for link in soup.select('a[href*="/documentation/"]'):
                href = link.get('href')
                if href:
                    full_url = urljoin(self.base_url, href)
                    doc_links.append(full_url)
        
        # Remove duplicates and filter
        doc_links = list(set(doc_links))
        
        # Discover more links by following a few key pages
        print("Discovering additional documentation pages...")
        additional_links = set()
        for link in doc_links[:15]:  # Limit to avoid too many requests
            time.sleep(1)
            more_links = self.get_all_doc_links(link)
            additional_links.update(more_links)
        
        doc_links.extend(list(additional_links))
        doc_links = list(set(doc_links))  # Remove duplicates again
        
        print(f"Found {len(doc_links)} documentation pages")
        
        extracted_docs = []
        
        for i, url in enumerate(doc_links, 1):
            if url in self.visited_urls:
                continue
                
            print(f"Processing ({i}/{len(doc_links)}): {url}")
            
            html = self.get_page_content(url)
            if not html:
                continue
                
            # Extract main content
            main_content = self.extract_main_content(html, url)
            
            if main_content:
                # Clean up the HTML
                content_html = str(main_content)
                
                # Extract title
                soup = BeautifulSoup(html, 'html.parser')
                title_elem = soup.select_one('h1, .wp-block-post-title, .entry-title, title')
                title = title_elem.get_text(strip=True) if title_elem else urlparse(url).path
                
                # Create filename from URL
                path_parts = urlparse(url).path.strip('/').split('/')
                if len(path_parts) > 1:
                    filename = '_'.join(path_parts[1:])  # Skip 'documentation'
                else:
                    filename = 'index'
                filename = re.sub(r'[^\w\-_]', '_', filename) + '.html'
                
                # Save individual file
                file_path = Path(output_dir) / filename
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f'<!-- URL: {url} -->\n')
                    f.write(f'<!-- Title: {title} -->\n')
                    f.write(content_html)
                
                # Store for combined output
                extracted_docs.append({
                    'url': url,
                    'title': title,
                    'filename': filename,
                    'content': content_html
                })
                
                self.visited_urls.add(url)
                time.sleep(1)  # Be respectful to the server
        
        # Create combined markdown file for Claude
        self.create_combined_output(extracted_docs, output_dir)
        
        # Create metadata file
        self.create_metadata(extracted_docs, output_dir)
        
        print(f"\nCrawling complete! Extracted {len(extracted_docs)} pages")
        print(f"Files saved to: {output_dir}/")
        print(f"Combined file for Claude: {output_dir}/search_filter_docs_combined.md")
        
    def create_combined_output(self, docs, output_dir):
        """Create a single combined file for Claude project knowledge"""
        combined_path = Path(output_dir) / "search_filter_docs_combined.md"
        
        with open(combined_path, 'w', encoding='utf-8') as f:
            f.write("# Search and Filter Documentation\n\n")
            f.write("This is a combined documentation file for the Search and Filter WordPress plugin.\n\n")
            f.write("---\n\n")
            
            for doc in docs:
                f.write(f"## {doc['title']}\n")
                f.write(f"**Source:** {doc['url']}\n\n")
                
                # Convert HTML to more readable format for Claude
                soup = BeautifulSoup(doc['content'], 'html.parser')
                
                # Convert HTML to markdown-like format
                text_content = soup.get_text(separator='\n', strip=True)
                
                # Clean up excessive whitespace
                text_content = re.sub(r'\n\s*\n', '\n\n', text_content)
                text_content = re.sub(r' +', ' ', text_content)
                
                f.write(text_content)
                f.write("\n\n---\n\n")
    
    def create_metadata(self, docs, output_dir):
        """Create metadata file"""
        metadata = {
            'crawl_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_pages': len(docs),
            'base_url': self.base_url,
            'pages': [
                {
                    'url': doc['url'],
                    'title': doc['title'],
                    'filename': doc['filename']
                }
                for doc in docs
            ]
        }
        
        with open(Path(output_dir) / 'metadata.json', 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

def main():
    crawler = DocumentationCrawler()
    crawler.crawl_documentation()

if __name__ == "__main__":
    main()