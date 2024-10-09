{
    'name': 'Custom App Security',
    'category': 'Stock',
    "author": "arisnew",
    "website": "https://github.com/arisnew",
    'description': """
Example security data (access rights, record rules) in odoo
    """,
    'depends': ['stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_example_views.xml',
    ],
    'license': 'OEEL-1',
}
