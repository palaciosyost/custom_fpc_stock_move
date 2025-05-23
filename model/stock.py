from odoo import models, api, fields, _
from datetime import datetime, timedelta


class StockDate(models.Model):
    _inherit = "stock.picking"
    _description = "Aumentar fecha programada de entrega automáticamente"

    def write(self, vals):
        res = super(StockDate, self).write(vals)
        self.update_fecha()
        return res

    def update_fecha(self):
        for record in self:
            if record.scheduled_date:
                fecha_hoy = datetime.now().replace(second=0, microsecond=0)
                scheduled = record.scheduled_date.replace(second=0, microsecond=0)

                if fecha_hoy >= scheduled:
                    record.scheduled_date = fecha_hoy + timedelta(hours=2)
                else:
                    print("La fecha de hoy es menor a la fecha programada.")

    def button_validate(self):
        self.update_fecha()  # Actualiza antes de validar
        res = super(StockDate, self).button_validate()
        return res
