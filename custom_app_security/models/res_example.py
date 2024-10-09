from odoo import models, fields, api, _



class ResExample(models.Model):
    _name = 'res.example'
    _description = 'Res Example'

    name = fields.Char(string='Name')
    
