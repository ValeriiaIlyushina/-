import requests
from datetime import datetime
import os
import json
pip install python-dotenv

class API_VK:
    API_URL = 'https://api.vk.com/method'
    URL_Y = 'https://cloud-api.yandex.net/v1/disk/resources'
    URL_Y2 = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token, owner_id, Y_TOKEN):
        self.token = token
        self.owner_id = owner_id
        self.Y_TOKEN = Y_TOKEN
        self.photos_info = []

        if not os.path.exists('images'):
            os.makedirs('images')

    def params(self, extra_params=None):
        base_params = {
            'access_token': self.token,
            'v': '5.131',
            'extended': '1',
            'owner_id': self.owner_id,
            'album_id': 'profile',
        }
        if extra_params:
            base_params.update(extra_params)
        return base_params

    def get_photos(self):
        try:

            url = f"{self.API_URL}/photos.get"
            params = self.params()
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            if 'error' in data:
                print(f"Ошибка VK API: {data['error']['error_msg']}")
                return

            if 'response' not in data or 'items' not in data['response']:
                print("Нет данных о фотографиях")
                return

            name_list = []
            url_list = []

            headers = {'Authorization': self.Y_TOKEN}
            create_folder_response = requests.put(self.URL_Y, params={'path': 'Photos_VK'}, headers=headers)

            if create_folder_response.status_code not in [200, 201, 409]:
                print(f"Ошибка при создании папки на Яндекс.Диске: {create_folder_response.json()}")
                return

            for photo in data['response']['items']:
                try:
                    max_size = max(photo['sizes'], key=lambda x: x['width'] * x['height'])
                    photo_url = max_size['url']

                    likes = photo['likes']['count']
                    date_str = datetime.fromtimestamp(photo['date']).strftime('%Y-%m-%d')

                    filename = f"{likes}.jpg"
                    if filename in name_list:
                        filename = f"{likes}_{date_str}.jpg"
                    self.photos_info.append({
                        "file_name": filename,
                        "size": max_size['type']
                    })
                    local_filename = f"images/{filename}"
                    photo_response = requests.get(photo_url)
                    photo_response.raise_for_status()

                    with open(local_filename, 'wb') as f:
                        f.write(photo_response.content)

                    upload_params = {'path': f'Photos_VK/{filename}', 'overwrite': 'true'}
                    upload_response = requests.get(self.URL_Y2, params=upload_params, headers=headers)

                    if upload_response.status_code == 200:
                        href = upload_response.json()['href']
                        with open(local_filename, 'rb') as f:
                            requests.put(href, files={'file': f})
                        print(f"Файл {filename} успешно загружен на Яндекс.Диск")
                    else:
                        print(f"Ошибка при получении ссылки для загрузки: {upload_response.json()}")

                    name_list.append(filename)
                    url_list.append(photo_url)

                except Exception as photo_error:
                    print(f"Ошибка при обработке фото: {photo_error}")
                    continue
            with open('photos_info.json', 'w') as f:
                json.dump(self.photos_info, f, indent=4)
        except requests.exceptions.RequestException as req_error:
            print(f"Ошибка при выполнении запроса: {req_error}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == '__main__':
    vk_cl = API_VK(TOKEN, 'ВК ID', 'ТОКЕН ЯНДЕКС ДИСКА')
    vk_cl.get_photos()