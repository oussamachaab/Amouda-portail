{
    'name' : 'ous_app',
    'category' : '',
    'author' : 'Oussama chaab',
    'version' : '1.0.0',
    'description' : 'My first app on odoo ',
    
    'depends' : [
           'web', 'mail', 'portal',
    ],
    
    'data' : [
        
        'views/portal_my_home_inehrit_view.xml',
         
        
    ],
    'assets': {
            '/new_app/static/src/css/custom_styles.css',
    },
    'application' : True,
    'installed' : True,
    'license': 'LGPL-3'
    
    
}
