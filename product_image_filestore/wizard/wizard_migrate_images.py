# -*- encoding: utf-8 -*-
#
#Created on Aug 16, 2019
#
#@author: dogan
#

from openerp import models, fields, api


class WizardMigrateImages(models.TransientModel):
    _name = 'product_image_filestore.wizard_migrate'
    
    @api.multi
    def action_confirm(self):
        image_obj = self.env['base_multi_image.image']
        for product_tmpl in self.env['product.template'].search([('image_attachment_id','!=', False)]):
            image_obj.create({'name':product_tmpl.display_name,
                              'owner_id':product_tmpl.id,
                              'owner_model':'product.template',
                              'storage':'attachment',
                              'attachment_id':product_tmpl.image_attachment_id.id})
            
        for product in self.env['product.product'].search([('image_variant_attachment_id','!=', False)]):
            image_obj.create({'name':product.display_name,
                              'owner_id':product.product_tmpl_id.id,
                              'owner_model':'product.template',
                              'storage':'attachment',
                              'attachment_id':product.image_variant_attachment_id.id,
                              'product_variant_ids':[(6,False,[product.id])]})
   
        return {}