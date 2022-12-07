from maximumtest.utils.helpers.abs_path import to_resource as path


class GatewayData:
    @staticmethod
    def get_data():
        data = {
            "health": {
                "url": "health"
            },

            "email/vacancy": {
                "url": "email/vacancy",
                "request": {
                    'fullName': (None, 'Вася Пупкин'),
                    'city': (None, 'Москва'),
                    'phone': (None, '+7 999 999 99 99'),
                    'email': (None, 'test@mail.com'),
                    'file': ('for_test_txt.txt', open(path('for_test_txt.txt'), 'rb'))
                }
            },

            "post_registrations": {
                "url": "registrations",
                "request": {
                    "country": "ru",
                    "firstName": "Удали если видишь это",
                    "lastName": "Удали если видишь это",
                    "email": "user@example.com",
                    "phone": "+7 (999) 999-99-99",
                    "parentName": "Удали если видишь это",
                    "parentEmail": "user@example.com",
                    "parentPhone": "+7 999 999 99 99",
                    "city": "string",
                    "companyId": "CMP-000-000",
                    "crmId": "string",
                    "place": "string",
                    "school": "string",
                    "type": "student",
                    "grade": 11,
                    "year": 0,
                    "additionalInfo": "string",
                    "gaCid": "string",
                    "product": "string",
                    "lmsId": "string",
                    "utm": {
                        "utm_campaign": "string",
                        "utm_content": "string",
                        "utm_medium": "string",
                        "utm_source": "string",
                        "utm_term": "string"
                    },
                    "examType": "ege",
                    "month": 8,
                    "webformId": "string",
                    "products": None
                }
            },

            "get_registrations": {
                "url": "registrations"
            },
        }

        return data
