from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag Model"

    name = fields.Char("Name", required = True)

    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique!"),
    ]
