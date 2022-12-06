schemas = {
    "components": {
        "first-button": {
            "id": "first-button",
            "type": "object",
            "properties": {
                "link": {"type": "string"},
                "text": {"type": "string"},
                "crmId": {"type": "string"},
                "actionLink": {"type": "boolean"}
            }
        },

        "second-button": {
            "id": "second-button",
            "type": "object",
            "properties": {
                "link": {"type": "string"},
                "text": {"type": "string"},
                "crmId": {"type": "string"},
                "active": {"type": "boolean"},
                "actionLink": {"type": "boolean"}
            }
        },

        "category": {
            "id": "category",
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },

        "city": {
            "id": "city",
            "type": "array",
            "items": {
                "type": "string"
            }
        },

        "filter-fields": {
            "id": "filter-fields",
            "type": "object",
            "properties": {
                "grade": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "showAll": {"type": "boolean"},
                        "priority": {"type": "number"},
                        "nameMobile": {"type": "string"},
                        "showAllTitle": {"type": "string"}
                    }
                },
                "format": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "multi": {"type": "boolean"},
                        "showAll": {"type": "boolean"},
                        "priority": {"type": "number"},
                        "nameMobile": {"type": "string"},
                        "showAllTitle": {"type": "string"}
                    }
                },
                "additional": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "multi": {"type": "boolean"},
                        "showAll": {"type": "boolean"},
                        "priority": {"type": "number"},
                        "nameMobile": {"type": "string"},
                        "showAllTitle": {"type": "string"}
                    }
                },
                "discipline": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "multi": {"type": "boolean"},
                        "showAll": {"type": "boolean"},
                        "priority": {"type": "number"},
                        "nameMobile": {"type": "string"},
                        "showAllTitle": {"type": "string"}
                    }
                }
            },
        },

        "labels": {
            "id": "labels",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "item": {"type": "string"},
                    "important": {"type": "boolean"}
                }
            }
        },

        "title-description": {
            "id": "title-description",
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"}
            }
        },

        "links": {
            "id": "links",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "linkText": {"type": "string"},
                    "link": {"type": "string"},
                    "priority": {"type": "string"}
                }
            }
        },

        "array-of-strings": {
            "id": "array-of-strings",
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },

    "schemas": {
        "banners": {
            "id": "banners",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "bannerPosition": {"type": "string"},
                "title": {"type": ["string", "null"]},
                "active": {"type": "boolean"},
                "text": {"type": ["string", "null"]},
                "firstButton": {
                    "$anchor": "first-button"
                },
                "secondButton": {
                    "$anchor": "second-button"
                },
                "backgroundImage": {"type": ["string", "null"]},
                "image": {"type": ["string", "null"]},
                "backgroundColor": {"type": ["string", "null"]},
                "category": {
                    "$anchor": "category"
                },
                "city": {
                    "$anchor": "city"
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "header": {
            "id": "header",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "text": {"type": "string"},
                "crmId": {"type": ["string", "null"]},
                "link": {"type": ["string", "null"]},
                "outline": {"type": ["boolean", "null"]},
                "actionLink": {"type": ["boolean", "null"]},
                "categoryTemplates": {
                    "type": "array",
                    "items": {
                        "$anchor": "header-category",
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "header-banners": {
            "id": "header_banners",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "title": {"type": "string"},
                "text": {"type": "string"},
                "backgroundImage": {"type": ["string", "null"]},
                "link": {"type": ["string", "null"]},
                "crmId": {"type": ["string", "null"]},
                "backgroundColor": {"type": ["string", "null"]},
                "actionLink": {"type": ["boolean", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "header-category": {
            "id": "header-category",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "promo": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "item": {"type": "string"},
                            "link": {"type": "string"}
                        }
                    }
                },
                "visible": {"type": ["boolean", "null"]},
                "priority": {"type": "string"},
                "isClickable": {"type": "boolean"},
                "bottomMenu": {"type": "boolean"},
                "crmId": {"type": ["string", "null"]},
                "actionLink": {"type": ["boolean", "null"]},
                "link": {"type": ["string", "null"]},
                "categoryColor": {"type": ["string", "null"]},
                "categoryImage": {"type": ["string", "null"]},
                "bannerTemplates": {
                    "$anchor": "header_banners"
                },
                "subcategories": {
                    "type": "array",
                    "items": {
                        "$anchor": "header-subcategory",
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "header-subcategory": {
            "id": "header-subcategory",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "title": {"type": "string"},
                "priority": {"type": "string"},
                "isShowTitle": {"type": "boolean"},
                "isClickable": {"type": "boolean"},
                "crmId": {"type": ["string", "null"]},
                "actionLink": {"type": ["boolean", "null"]},
                "link": {"type": ["string", "null"]},
                "isFullType": {"type": "boolean"},
                "links": {
                    "type": ["array", "null"],
                    "items": {
                        "properties": {
                            "link": {"type": "string"},
                            "isBold": {"type": "boolean"},
                            "linkText": {"type": "string"},
                            "priority": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "product-card-labels": {
            "id": "product-card-labels",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "label": {"type": "string"},
                "labelCMS": {"type": ["string", "null"]},
                "basicPrice": {"type": ["number", "string", "null"]},
                "basicPriceDiscount": {"type": ["string", "null"]},
                "first": {
                    "$anchor": "first-button"
                },
                "second": {
                    "$anchor": "second-button"
                },
                "additionalPrice": {"type": ["number", "string", "null"]},
                "additionalPriceDiscount": {"type": ["string", "null"]},
                "discount": {"type": ["number", "string", "null"]},
                "labels": {
                    "$anchor": "labels",
                },
                "texts": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "item": {"type": "string"}
                        }
                    }
                },
                "isPresales": {"type": ["string", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "product-cards": {
            "id": "product-cards",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "titleCard": {"type": "string"},
                "titleCMS": {"type": ["string", "null"]},
                "subtitleCard": {"type": "string"},
                "priority": {"type": ["number", "string"]},
                "image": {"type": ["string", "null"]},
                "backgroundColor": {"type": ["string", "null"]},
                "labelTemplates": {
                    "$anchor": "product-card-labels",
                },
                "first": {
                    "$anchor": "first-button"
                },
                "second": {
                    "$anchor": "second-button"
                },
                "isUndefinedResultCard": {"type": ["boolean", "null"]},
                "isDefaultCard": {"type": ["boolean", "null"]},
                "city": {
                    "$anchor": "city"
                },
                "categories": {
                    "$anchor": "category"
                },
                "category": {"type": ["string", "null"]},
                "visible": {"type": ["boolean", "null"]},
                "filters": {
                    "$anchor": "filter-fields"
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "summer-product-cards": {
            "id": "summer-product-cards",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "button": {
                    "$anchor": "first-button"
                },
                "buttonReg": {
                    "$anchor": "first-button"
                },
                "description": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "theme": {"type": "string"},
                        "title": {"type": "string"}
                    }
                },
                "discountedPrice": {"type": "string"},
                "fullPrice": {"type": ["string", "null"]},
                "labels": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "backgroundColor": {"type": "string"}
                        }
                    }
                },
                "lmsId": {"type": ["string", 'null']},
                "groupId": {"type": ["string", 'null']},
                "priority": {"type": "string"},
                "title": {"type": "string"},
                "titleCMS": {"type": ["string", 'null']},
                "visible": {"type": "boolean"},
                "schedule": {
                    "type": "object",
                    "properties": {
                        "start": {"type": "string"},
                        "scheduleList": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "day": {"type": ["string", 'null']},
                                    "time": {"type": ["string", 'null']}
                                }
                            }
                        }
                    }
                },
                "discipline": {"type": ["string", 'null']},
                "grade": {"type": ["string", 'null']},
                "crmEntityId": {"type": ["string", 'null']},
                "filters": {
                    "$anchor": "filter-fields",
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "store-subject-templates": {
            "id": "store-subject-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "list": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "item": {"type": "string"},
                            "groupId": {"type": ["number", "string"]},
                            "courseId": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "store-text-templates": {
            "id": "store-text-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "label": {"type": "string"},
                "points": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "title": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "store-page-templates": {
            "id": "store-page-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "courseName": {"type": ["string", "null"]},
                "courseFormat": {"type": ["string", "null"]},
                "url": {"type": "string"},
                "title": {"type": "string"},
                "subtitle": {"type": "string"},
                "selectSubjectStep": {
                    "id": "step",
                    "type": ["object", "null"],
                    "properties": {
                        "label": {"type": ["string", "null"]},
                        "text": {"type": ["string", "null"]},
                        "title": {"type": ["string", "null"]}
                    }
                },
                "typePaymentStep": {
                    "$anchor": "step"
                },
                "paymentSectionStep": {
                    "$anchor": "step"
                },
                "textTemplates": {
                    "$anchor": "store-text-templates"
                },
                "thankTemplates": {
                    "$anchor": "store-thanks-page-templates"
                },
                "subjectTemplate": {
                    "$anchor": "store-subject-templates"
                },
                "preselectedSubject": {"type": ["string", "null"]},
                "preselectedPaymentType": {"type": "string"},
                "once": {
                    "type": "object",
                    "properties": {
                        "active": {"type": "boolean"},
                        "discount": {"type": ["number", "string"]},
                        "fullPrice": {"type": ["number", "string"]},
                        "discountedPrice": {"type": ["number", "string"]}
                    }
                },
                "recurrent": {
                    "type": "object",
                    "properties": {
                        "active": {"type": "boolean"},
                        "duration": {"type": ["number", "string"]},
                        "fullPrice": {"type": ["number", "string"]},
                        "discountedPrice": {"type": ["number", "string"]},
                        "firstPayDiscount": {"type": ["number", "string"]},
                        "followingPaysPrice": {"type": ["number", "string"]}
                    }
                },
                "crmId": {"type": "string"},
                "dropCartCrmId": {"type": ["string", "null"]},
                "successCartCrmId": {"type": ["string", "null"]},
                "issueYear": {"type": ["number", "null"]},
                "promo": {"type": ["boolean", "null"]},
                "schedule": {"type": ["boolean", "null"]},
                "monthlyPayment": {"type": ["boolean", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "store-thanks-page-templates": {
            "id": "store-thanks-page-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "isForm": {"type": "boolean"},
                "topBlock": {
                    "$anchor": "title-description",
                },
                "bottomBlock": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "promocode": {"type": "string"},
                        "description": {"type": "string"}
                    }
                },
                "button": {
                    "type": "object",
                    "properties": {
                        "link": {"type": "string"},
                        "title": {"type": "string"}
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "filters": {
            "id": "filters",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": ["string", "null"]},
                "url": {"type": "string"},
                "fields": {
                    "$anchor": "filter-fields",
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "teachers": {
            "id": "teachers",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "image": {"type": "string"},
                "subject": {"type": "string"},
                "description": {"type": "string"},
                "quote": {"type": "string"},
                "promoText": {"type": ["string", "null"]},
                "easy": {"type": ["boolean", "null"]},
                "details": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "value": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "trial-lessons": {
            "id": "trial-lessons",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "digestName": {"type": ["string", "null"]},
                "grade": {"type": "string"},
                "subject": {"type": "string"},
                "dateTime": {"type": "string"},
                "companyId": {"type": ["string", "null"]},
                "express": {"type": ["boolean", "null"]},
                "tags": {
                    "type": ["array", "null"],
                    "items": {"type": "string"}
                },
                "online": {"type": ["boolean", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "free-lessons": {
            "id": "free-lessons",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "url": {"type": "string"},
                "blockColor": {"type": ["string", "null"]},
                "firstScreen": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "btnText": {"type": "string"},
                        "imageUrl": {"type": "string"},
                        "subtitle": {"type": "string"}
                    }
                },
                "meta": {
                    "$anchor": "title-description",
                },
                "videoTitle": {"type": "string"},
                "videos": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "labels": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "imageLink": {"type": "string"},
                            "videoLink": {"type": "string"},
                            "description": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "vacancies": {
            "id": "vacancies",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "department": {"type": "string"},
                "area": {"type": "string"},
                "name": {"type": "string"},
                "experience": {"type": "string"},
                "city": {
                    "$anchor": "city"
                },
                "salary": {"type": ["string", "null"]},
                "video": {"type": ["string", "null"]},
                "skills": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        }
                    }
                },
                "recruiterEmail": {"type": "string"},
                "descriptionBlocks": {
                    "type": "array",
                    "items": {
                        "$anchor": "title-description",
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "accordion": {
            "id": "accordion",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "title": {"type": ["string", "null"]},
                "name": {"type": ["string", "null"]},
                "category": {"type": "string"},
                "items": {
                    "type": "array",
                    "items": {
                        "$anchor": "title-description",
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "info-about-course": {
            "id": "info-about-course",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "title": {"type": ["string", "null"]},
                "name": {"type": ["string", "null"]},
                "blocks": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "image": {"type": "string"},
                            "title": {"type": "string"},
                            "description": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "lead-forms": {
            "id": "lead-forms",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "visible": {"type": ["boolean", "null"]},
                "position": {"type": "string"},
                "title": {"type": "string"},
                "buttonText": {"type": "string"},
                "subtitle": {"type": "string"},
                "crmId": {"type": ["string", "null"]},
                "urls": {
                    "type": ["array", "null"],
                    "items": {"type": "string"}
                },
                "zeroContract": {"type": ["boolean", "null"]},
                "userType": {"type": ["boolean", "null"]},
                "selectedInputs": {
                    "type": ["array", "null"],
                    # "items": {
                    #     "type": "object",
                    #     "properties": {
                    #         "name": {"type": "string"},
                    #         "isActive": {"type": "boolean"},
                    #         "priority": {"type": "number"},
                    #         "isRequired": {"type": "boolean"},
                    #         "studentIsActive": {"type": "boolean"},
                    #         "studentPriority": {"type": "number"},
                    #         "studentIsRequired": {"type": "boolean"}
                    #     }
                    # }
                },
                "agreements": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "checkbox": {"type": "boolean"},
                            "description": {"type": "string"}
                        }
                    }
                },
                "lmsId": {"type": ["string", "null"]},
                "thankYouPopup": {
                    "$anchor": "title-description",
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "regions": {
            "id": "regions",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "programType": {"type": "string"},
                "isSubjectPage": {"type": "boolean"},
                "metaTitle": {"type": "string"},
                "metaDescription": {"type": "string"},
                "title": {"type": ["string", "null"]},
                "description": {"type": ["string", "null"]},
                "info": {"type": ["string", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "catalog": {
            "id": "catalog",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "noIndex": {"type": ["boolean", "null"]},
                "metaTitle": {"type": "string"},
                "metaDescription": {"type": "string"},
                "title": {"type": "string"},
                "description": {"type": ["string", "null"]},
                "urls": {
                    "$anchor": "array-of-strings"
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        # "pc/constructor-templates": {
        #     "id": "pc/constructor-templates"
        #     "type": "object",
        #     "properties": {
        #         "id": {"type": "string"},
        #         "name": {"type": "string"},
        #         "url": {"type": "string"},
        #         "noIndex": {"type": ["boolean", "null"]},
        #         "metaTitle": {"type": "string"},
        #         "metaDescription": {"type": "string"},
        #         "blocks": {
        #             "type": "array",
        #             "items": {
        #                 "priority": {"type": "number"},
        #                 "scrollId": {"type": "string"},
        #                 "blockType": {"type": "string"},
        #                 "blockTemplateId": {"type": "string"}
        #             }
        #         },
        #         "createdAt": {"type": "string"},
        #         "updatedAt": {"type": "string"}
        #     }
        # },

        "page-constructor/bullet-templates": {
            "id": "page-constructor/bullet-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "title": {"type": "string"},
                "bullets": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        # "properties": {
                        #     "text": "string"
                        # }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "page-constructor/first-screen-templates": {
            "id": "page-constructor/first-screen-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "title": {"type": "string"},
                "description": {"type": "string"},
                "image": {"type": ["string", "null"]},
                "buttons": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "style": {"type": ["string", "null"]},
                            "active": {"type": "boolean"},
                            "actionType": {"type": "string"},
                            "actionValue": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "page-constructor/iframe-templates": {
            "id": "page-constructor/iframe-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "url": {"type": "string"},
                "breakpoints": {
                    # "type": ["array", "null", "object"]
                    # "items": {
                    #     "breakpointMaxWidth": {"type": "string"},
                    #     "breakpointHeight": {"type": "string"}
                    # }
                },
                "ignoreContainer": {"type": "boolean"},
                "height": {"type": ["string", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "page-constructor/text-block-templates": {
            "id": "page-constructor/text-block-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "text": {"type": "string"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "page-constructor/html-block-templates": {
            "id": "page-constructor/html-block-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "htmlData": {"type": "string"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "page-constructor/why-us-block-templates": {
            "id": "page-constructor/why-us-block-templates",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"},
                "title": {"type": "string"},
                "subtitle": {"type": "string"},
                "info": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "subtitle": {"type": "string"}
                        }
                    }
                },
                "image": {
                    "type": "object",
                    "properties": {
                        "alt": {"type": "string"},
                        "src": {"type": "string"}
                    }
                }
            }
        },

        "web-events": {
            "id": "web-events",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "title": {"type": "string"},
                "keyWords": {
                    "type": ["array", "null"],
                    "items": {
                        "type": ["string", "null"],
                    }
                },
                "filter": {
                    "$anchor": "array-of-strings"
                },
                "class": {"type": ["string", "null"]},
                "description": {"type": "string"},
                "image": {"type": ["string", "null"]},
                "buttonText": {"type": ["string", "null"]},
                "page": {"type": "string"},
                "formatOnline": {"type": ["boolean", "null"]},
                "classes": {
                    "$anchor": "array-of-strings"
                },
                "date": {"type": ["string", "null"]},
                "crmId": {"type": ["string", "null"]},
                "actionLink": {"type": ["boolean", "null"]},
                "address": {"type": ["string", "null"]},
                "link": {"type": ["string", "null"]},
                "examType": {"type": ["string", "null"]},
                "price": {"type": ["string", "null"]},
                "oldPrice": {"type": ["string", "null"]},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "web-event-filters": {
            "id": "web-event-filters",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "filterElement": {"type": "string"},
                "subFilterElements": {
                    "$anchor": "array-of-strings"
                },
                "page": {"type": "string"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "web-event-page": {
            "id": "web-event-page",
            "type": "object",
            "filters": {
                "$anchor": "web-event-filters"
            },
            "cards": {
                "$anchor": "web-events"
            }
        },

        "webhooks/marquiz": {
            "id": "webhooks/marquiz",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "quizId": {"type": "string"},
                "campaignCode": {"type": "string"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "handbooks": {
            "id": "handbooks",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "type": {"type": "string"},
                "value": {"type": "string"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "footer": {
            "id": "footer",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "sections": {
                    "$anchor": "footer-sections"
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "footer-sections": {
            "id": "footer-sections",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "title": {"type": "string"},
                "priority": {"type": "string"},
                "isShowTitle": {"type": "boolean"},
                "links": {
                    "$anchor": "links",
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "static-pages-first-screen": {
            "id": "static-pages-first-screen",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "category": {"type": "string"},
                "title": {"type": "string"},
                "subtitle": {"type": "string"},
                "formTitle": {"type": "string"},
                "image": {"type": ["string", "null"]},
                "subjectsInfo": {"type": "string"},
                "firstButton": {
                    "type": ["object", "null"],
                    "properties": {
                        "text": {"type": "string"},
                        "action": {"type": "string"}
                    }
                },
                "secondButton": {
                    "type": ["object", "null"],
                    "properties": {
                        "text": {"type": "string"},
                        "action": {"type": "string"}
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "static-pages-group-info": {
            "id": "static-pages-group-info",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "category": {"type": "string"},
                "cards": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "text": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "static-pages-guarantee-info": {
            "id": "static-pages-guarantee-info",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "category": {"type": "string"},
                "paragraphs": {
                    "$anchor": "array-of-strings"
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "static-pages-course-program": {
            "id": "static-pages-course-program",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "category": {"type": "string"},
                "classes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "class": {"type": "string"},
                            "courseProgram": {
                                "$anchor": "labels",
                            }
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "static-pages-benefits-info": {
            "id": "static-pages-benefits-info",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "category": {"type": "string"},
                "title": {"type": "string"},
                "subtitle": {"type": "string"},
                "statBlocks": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "text": {"type": "string"}
                        }
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "static-pages-content": {
            "id": "static-pages-content",
            "type": "object",
            "properties": {
                "firstScreen": {"type": ["string", "null"]},
                "groupInfo": {"type": ["string", "null"]},
                "benefitsInfo": {"type": ["string", "null"]},
                "guaranteeInfo": {"type": ["string", "null"]},
                "courseProgram": {"type": ["string", "null"]}
            }
        },

        "cities": {
            "id": "cities",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "country": {"type": "string"},
                "city": {"type": "string"},
                "actualAddress": {
                    "id": "adress",
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "metro": {"type": "string"},
                        "phone": {"type": "string"},
                        "address": {"type": "string"},
                        "workTime": {"type": "string"},
                        "abbreviation": {"type": "string"},
                        "isPhoneCalltracking": {"type": "boolean"}
                    }
                },
                "requisites": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "value": {"type": "string"}
                        }
                    }
                },
                "multiAddress": {"type": "boolean"},
                "secondaryAddresses": {
                    "type": "array",
                    "items": {
                        "$anchor": "adress"
                    }
                },
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        },

        "uchebnik/seo-settings": {
            "id": "uchebnik/seo-settings",
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "url": {"type": "string"},
                "propagation": {"type": "boolean"},
                "metaTitle": {"type": "string"},
                "metaDescription": {"type": "string"},
                "noIndex": {"type": "boolean"},
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            }
        }
    },

    "mass_schemas": {
        "mass/product-card-labels": {
            "$anchor": "product-card-labels"
        },

        "mass/product-cards": {
            "type": "object",
            "$anchor": "product-card"
        }
    },

    "file_schemas": {
        "files": {
            "id": "banners",
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "url": {"type": "string"},
                "key": {"type": "string"},
                "name": {"type": "string"},
                "path": {"type": "string"}
            }
        }
    }
}