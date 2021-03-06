# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Alumno(models.Model):
    
    _name = 'academy.alumno'
    _description = 'Alumno Info'
    
    name = fields.Char(string='Nombre', required=True)
    num_cuenta = fields.Integer(string='Cuenta', required=True)
    correo = fields.Char(string='correo', required=True)
    active = fields.Boolean(string='Active', default=True)
    carrera = fields.Selection(string='Carrera', 
                            selection=[('computacion','Computacio'),
                                    ('mecanica','Mecanica'),
                                    ('telecom','Telecomunicaciones')],
                                    copy=False)