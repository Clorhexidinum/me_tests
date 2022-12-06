class PaymentsModuleData:
    @staticmethod
    def get_data():
        data = {
            "payments": {
                "url": "payments",
                "request": {
                    "name": "string",
                    "lastName": "string",
                    "email": "user@example.com",
                    "phone": "+7 999 999 99 99",
                    "lmsGroup": "123",
                    "webformId": "string",
                    "duration": 0,
                    "grade": 11,
                    "type": "student",
                    "subject": "Математика",
                    "territory": "string",
                    "promoCode": "LOL",
                    "isPromoValid": True,
                    "promo": False,
                    "gaCid": "string",
                    "utm": {
                        "utm_campaign": "string",
                        "utm_content": "string",
                        "utm_medium": "string",
                        "utm_source": "string",
                        "utm_term": "string"
                    },
                    "additionalInfo": "string",
                    "thankPageName": "string"
                }
            },

            "payments/repeat": {
                "url": "payments/repeat",
                "request": {
                    "orderId": "6c79b34c-9c19-423d-a0db-6f3d06367a03",
                    "category": "string"
                }
            },

            "zero-contract": {
                "url": "zero-contract",
                "request": {
                    "country": "ru",
                    "firstName": "string",
                    "lastName": "string",
                    "email": "user@example.com",
                    "phone": "+7 (999) 999-99-99",
                    "parentName": "string",
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
                    "sendCrmRegId": True,
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
                    "products": None,
                    "shouldRegisterInAc": True
                }
            },
        }

        return data
