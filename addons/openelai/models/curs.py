from odoo import models, fields, api 

class curs(models.Model):
    _name = 'openelai.curs'
    _description = 'curs oelai'
    name = fields.Char()
    nivell=fields.Selection([('eso','ESO'),('batx','BATX'),('GM', 'CFGM'),('GS', 'CFGS')])
    materia_ids = fields.Char()
    
  