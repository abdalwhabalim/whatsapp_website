# -*- coding: utf-8 -*-

{   'name': 'WhatsApp Website',
    'version': '16.0',
    'author': "SOFT GUIDE TECH",
    'description': """
        Chat with your customers through WhatsApp / Whatsapp integration / website whatsapp integration""",
    'category': 'website',
    'website': "https://softguidetech.com/",
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_whatsapp_views.xml',
        'views/templates.xml',
        'data/website_whatsapp_data.xml'
    ],

    'assets': {
        'web.assets_frontend': [
            'website_mail/static/src/js/follow.js',
            'website_mail/static/src/css/website_mail.scss',
        ],
    },
    'images': [
        'static/description/logo.png',
    ],
 
    'license': 'AGPL-3',

}
