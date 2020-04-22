import requests


def download_all(input_path='../../data/raw/urls.csv', output_path='../../data/raw/'):
    with open(input_path) as f:
        urls = f.read().splitlines()
    for url in urls:
        req = requests.get(url)
        url_content = req.content
        csv_file = open(output_path+url.split("/")[-1].lower(), 'wb')
        csv_file.write(url_content)
        csv_file.close()


if __name__ == '__main__':
    download_all()
