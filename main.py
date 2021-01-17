import requests

HEADERS = {"Authorization": "OAuth "}

resp = requests.get(
    "https://cloud-api.yandex.net/v1/disk/resources/upload",
    params={"path": "/imp.txt"},
    headers=HEADERS)
data = resp.status_code
d = resp.json()
print(d)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        self.file_path = file_path

        href = d["href"]
        with open(file_path, "r") as f:
            resp1 = requests.put(href, files={"file": f})
        return resp1.raise_for_status()


if __name__ == '__main__':
    uploader = YaUploader(' ')
    file_path = uploader.upload('C:/Users/Ольга/Desktop/imp.txt')

