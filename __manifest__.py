# -*- coding: utf-8 -*-

{    
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Trainning""",
    'description': """
                    Academy Module to manage Trainning:
                    -Courses
                    -Sessions
                    -Attendees
    """,
    'author':'Odoo',
    'website':'https://www.odoo.com',
    'category': 'Trainning',
    'version':'0.1',
    'depends': ['base'],
    'data': [
        'views/vistacourse.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv'
    
    ],
    'demo': [

    ],
    
}
