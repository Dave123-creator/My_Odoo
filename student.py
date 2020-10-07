from odoo import models,fields
from odoo import time
class SaleOrderInherit(models.Model):
      _inherit='sale.order'
      name=fields.Char(string='Authorized Person')
      date_creation = fields.Date('Authentication Date', required=True, default=fields.Date.today())

class SaleQuotationInherit(models.Model):
      _inherit='sale.order'
      w_name=fields.Many2one('res.users', string='Withdrawal Person')

class CustomersDetailsInherit(models.Model):
      _inherit='res.partner'
      name=fields.Char(string="HO")

class SchoolStudent(models.Model):
      _name='school.student'
      _description="Student Table"

      name=fields.Char(string="Name", required=True)
      age=fields.Integer(string="Age")
      guardian=fields.Char(string="Guardian")
      note=fields.Text(string="Notes")
      gender=fields.Selection(
          [   ('male', 'Male'),
              ('female', 'Female'),
              ('other', 'Other'),
          ], string='Gender', default='male')
      date = fields.Datetime(default=fields.Date.today())
      end_date=fields.Date("End Date", readonly=True)
      act_name=fields.Char(string="Activity Name", required=True)
      act_status=fields.Selection(
          [   ('pending', 'Incomplete'),
               ('done', 'Complete'),  
               ('no', 'Yet to Start'),
          ], string='Activity Status', store=True, readonly=True)

