# -*- coding: utf-8 -*-
{
    'name': "dh_city_contact_crm",

    'summary': """
        Load the city data from the CSV file when the module is installed. 
        """,

    'description': """
        This will load the city data from the CSV file when the module is installed. 
        The city field in the res.partner and crm.lead models will now be a dropdown selection field 
        populated with the cities from the CSV file.
    """,

    'author': "Dino Herlambang",
    'website': "http://www.instagram.com/_dinoherlambang_/",
    'version': '13.0',
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/res.kabupaten.csv',
        'data/res.country.state.csv',
    ],
	"installable": True,
	"auto_install": False,
	"application": True,
	"namespace": "dh_city"
}
