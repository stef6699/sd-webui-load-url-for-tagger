import requests
import os
from urllib.parse import urlparse

def load_images_from_url(url_list, save_directory):
    
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for url in url_list:
        try:
            # Parse the URL to get the image name
            parsed_url = urlparse(url)
            image_name = os.path.basename(parsed_url.path)
            image_path = os.path.join(save_directory, image_name)

            # Download the image
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            # Save the image to the directory
            with open(image_path, 'wb') as f:
                f.write(response.content)

            print(f"Downloaded {image_name} to {save_directory}")

        except Exception as e:
            print(f"Failed to download {url}: {str(e)}")

# Example usage
if __name__ == '__main__':
    urls = ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']
    load_images_from_url(urls, 'downloaded_images')