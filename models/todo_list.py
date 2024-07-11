# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'To-do List'

    name = fields.Char(string='Name', required=True)
    completed = fields.Boolean(string='Completed')
    color = fields.Char(string='Color')
