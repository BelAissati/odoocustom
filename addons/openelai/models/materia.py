from odoo import models, fields, api 

class materia(models.Model):
    _name = 'openelai.materia'
    _description = 'curs oelai'
    
    name = fields.Char(string='Materia', required= True, index=True)
    description = fields.Text()
    curs_id = fields.Char()