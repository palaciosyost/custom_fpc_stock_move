{
    'name': 'Fecha programacion - validacion de estado',
    'version': '1.0',
    'description': 'Actualizacion de fecha de entrega cuando valides para optimizar el tiempo de modificacion y no cometer errores al generar la guia de remision',
    'summary': '',
    'author': 'FPC Technology',
    'website': 'https://fpc-technology.com/',
    'license': 'LGPL-3',
    'category': 'stock',
    'depends': [
        'base', "stock", "sale"
    ],
    'data': [
        "view/init_view.xml",
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'view/kanban_res_partner.xml',
        # 'view/aceleradores_form.xml',
        # 'view/comisiones_empleado.xml',
        # 'data/comision_data.xml',
        # 'wizard/wizard_comision.xml',
        # 'view/inherit_from_nomina.xml',
        # 'view/reportes/comision_report.xml'

    ],
    'auto_install': False,
    'application': True,
}