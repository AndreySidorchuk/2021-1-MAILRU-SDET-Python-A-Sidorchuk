import requests
import json
from urllib.parse import urljoin


class CantFoundSegmentException(Exception):
    pass

class RequestErrorException(Exception):
    pass

class MyTargetClient:
    LIMIT = '500'
    LEFT = 365
    RIGHT = 0
    BAD = 0
    
    def __init__(self, username, password):
        self.main_url = 'https://target.my.com/'
        self.session = requests.Session()

        self.username = username
        self.password = password

        self.auth()
        self.csrf_token = self.get_csrf()

    def _request(self, method, url=None, location=None, headers=None, params=None, data=None, json=False,
                 allow_redirects=False):
        """Настройка для метода request"""
        if location is not None and url is None:
            url = urljoin(self.main_url, location)

        res = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            allow_redirects=allow_redirects
            )

        if json:
            return res.json()
        else:
            return res

    def auth(self):
        """Метод авторизации клиента"""
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }
        data = {
            'email': self.username,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1#email'
        }

        response = self._request(
            'POST', url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0', headers=headers, data=data
        )

        while response.status_code == 302:
            location = response.headers['Location']
            response = self._request('GET', location)

        return response

    def get_csrf(self):
        """Возвращает csrf токен"""
        csrf_headers = {
            'Referer': 'https://target.my.com/auth/mycom?state=target_login%3D1',
        }
        log = self._request('GET', location='csrf', headers=csrf_headers)

        return log.headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def create_segment(self, name):
        """Создает сегмент с именем name"""
        header = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.csrf_token
        }

        url_params = {
            'fields': 'relations__object_type,relations__object_id,relations__params,relations_count,id,name,'
                      'pass_condition,created,campaign_ids,users,flags',
        }

        data = {
            'name': name,
            'pass_condition': 1,
            'relations': [{
                'object_type': 'remarketing_player',
                'params': {
                    'type': 'positive',
                    'left': self.LEFT,
                    'right': self.RIGHT,
                }
            }],
            'logicType': 'or',
        }
        response = self._request(
            method='POST',
            location='api/v2/remarketing/segments.json',
            params=url_params,
            data=json.dumps(data),
            headers=header)

        if response.status_code != 200:
            raise RequestErrorException(f'Неверный код {response.status_code} {response.reason}')
        return response

    def _get_segment_id(self, name=None):
        """Возвращает id сегмента, иначе 0"""
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token
        }
        url_params = {
            'limit': self.LIMIT
        }
        segments = self._request(
            method='GET',
            location='api/v2/remarketing/segments.json',
            params=url_params,
            headers=headers,
            json=True
        )['items']
        segment_id = self.BAD
        for segment in segments:
            if segment['name'] == name:
                segment_id = segment['id']
        return segment_id

    def delete_segment(self, name):
        """Удаляет сегмент и возвращает код ответа, иначе 0"""
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token
        }
        id = self._get_segment_id(name)
        response = self._request(
            method='DELETE',
            location=f'api/v2/remarketing/segments/{id}.json',
            headers=headers)
        if response.status_code != 204:
            raise RequestErrorException(f'Неверный код {response.status_code} {response.reason}')
        return response


    def check_segment_exists(self, name):
            check = self._get_segment_id(name)
            return check

    def create_campaign(self, name):
        """Создает кампанию с именем name"""
        header = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/campaign/new',
            'X-CSRFToken': self.csrf_token
        }

        url_params = {
            'fields': 'relations__object_type,relations__object_id,relations__params,relations_count,id,name,'
                      'pass_condition,created,campaign_ids,users,flags',
        }

        data = {
            'name': name,
            'pass_condition': 1,
            'relations': [{
                'object_type': 'remarketing_player',
                'params': {
                    'type': 'positive',
                    'left': self.LEFT,
                    'right': self.RIGHT,
                }
            }],
            'logicType': 'or',
        }

        response = self._request(
            method='POST',
            location='api/v2/campaign_rules.json',
            params=url_params,
            data=json.dumps(data),
            headers=header)
        if response.status_code != 204:
            raise RequestErrorException(f'Неверный код {response.status_code} {response.reason}')
        return response

    def delete_campaign(self, name):
        """Удаляет кампанию"""
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token
        }
        id = self._get_segment_id(name)
        response = self._request(
            method='DELETE',
            location=f'api/v2/campaign_rules{id}.json',
            headers=headers)
        if response.status_code != 204:
            raise RequestErrorException(f'Неверный код {response.status_code} {response.reason}')
        return response

    def check_campaign(self, name):
        try:
            self._get_campaign_id(name)
            return True
        except CantFoundSegmentException:
            return False

    def _get_campaign_id(self, name=None):
        """Возвращает id каспании, иначе 0"""
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token
        }
        url_params = {
            'limit': self.LIMIT
        }
        campaigns = self._request(
            method='GET',
            location='api/v2/campaign_id.json',
            params=url_params,
            headers=headers,
            json=True
        )['items']
        campaign_id = self.BAD
        for campaign in campaigns:
            if campaign['name'] == name:
                campaign_id = campaign['id']
        return campaign_id