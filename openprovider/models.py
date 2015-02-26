# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class openprovider(models.Model):
#     _name = 'openprovider.openprovider'

#     name = fields.Char()

class Domain(models.Model):
    name = field.Char(required=True)
