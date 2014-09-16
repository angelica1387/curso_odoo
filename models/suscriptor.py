# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class suscriptor(osv.osv):
	_name = 'co.suscriptor'
	_description = 'CO SUSCRIPTOR'

	_columns = {
		'name': fields.char('Nombre Completo'),
		'identification': fields.char('Cédula'),
		'address': fields.text('Dirección'),
	}

suscriptor()