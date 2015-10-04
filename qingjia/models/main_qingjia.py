# -*- encoding: utf-8 -*-

from openerp import models,fields,_,api
#import osv
#from osv import osv,fields
#from openerp.osv import fields,osv
#class qingjia_qingjia(models.Model):
#  _name="demo.tb.demo"
#  demoname=fields.Char('箐假单')

import logging

#class qingjia_qingjia(osv.osv):
class Tiaoxiu(models.Model):
    _name='qingjia.tiaoxiu'
    #_description="请假单"
    
    name = fields.Many2one('hr.employee', string="申请人", required=True)
    manager = fields.Many2one('hr.employee', string="主管", required=True)
    
    beginning = fields.Datetime(string="开始时间", required=True, default=fields.Datetime.now())
    ending = fields.Datetime(string="结束时间", required=True)
    
    #days = fields.Float(string="天数", required=True)
    #startdate = fields.Date(string="开始日期", required=True)
    reason = fields.Text(string="请假事由", required=True)
    accept_reason = fields.Text(string="同意理由", default="同意")
    
    #compute 没有写入数据库 on the fly 可以被workflow的condition调用
    current_name = fields.Many2one('hr.employee', string="当前登录人",compute="_get_current_name")
    is_manager = fields.Boolean(compute='_get_is_manager')
    
    state = fields.Selection([('draft',"草稿"),('confirmed',"待审核"),('accepted',"批准"),('rejected','拒绝'),
    ], string="状态",default='draft', readonly=True)
    
    #
    @api.model
    def _get_default_name(self):
        uid = self.env.uid
        print "self.env.uid ", self.env.uid
        res = self.env['res.users'].search([('id','=',uid)])
        name = res.login
        employee = self.env['hr.employee'].search([('name_related','=',name)])
        
        print name,employee
        return employee
    @api.model
    def _get_default_manager(self):
        uid = self.env.uid
        print "self.env.uid ", self.env.uid
        res = self.env['res.users'].search([('id','=',uid)])
        name = res.login
        employee = self.env['hr.employee'].search([('name_related','=',name)])
        
        logging.info("myinfo {}".format(employee.parent_id))
        
        print employee
        print name,employee.parent_id
        return employee.parent_id
        
    _defaults = {
        'name' : _get_default_name,
        'manager' : _get_default_manager,
        }

    def _get_is_manager(self):
        print('------------- test')
        print(self.current_name, self.manager, self.env.uid)
        if self.current_name == self.manager:
            self.is_manager = True
        else:
            self.is_manager = False

    def _get_current_name(self):
        uid = self.env.uid
        print "self.env.uid ", self.env.uid
        #res = self.env['resource.resource'].search([('user_id','=',uid)])
        #name = res.name
        #name = res[0].name 提示越界
        #res = self.pool['res.users'].browse(cr, uid, uid, context=context)提示cr等未定义
        res = self.env['res.users'].search([('id','=',uid)])
        name = res.login
        employee = self.env['hr.employee'].search([('name_related','=',name)])
        
        self.current_name = employee        
        print self.current_name,name
        
    def draft(self, cr,uid,ids,context=None):
        if context is None:
            context={}
        self.write(cr,uid,ids,{'state':'draft'},context=context)
        return True
    
    def confirm(self,cr,uid,ids,context=None):
        if context is None:
            context={}
        self.write(cr,uid,ids,{'state':'confirmed'},context=context)
        return True
        
    def accept(self,cr,uid,ids,context=None):
        if context is None:
            context={}
        self.write(cr,uid,ids,{'state':'accepted'},context=context)
        print('你的请假单被批准了')
        return True

    def reject(self,cr,uid,ids,context=None):
        if context is None:
            context={}
        self.write(cr,uid,ids,{'state':'rejected'},context=context)
        print('抱歉，你的请假单没有被批准')
        return True
'''  
    @api.one
    def send_qingjd(self):
        self.sended = True
        return self.sended
    
    @api.one
    def confirm_qingjd(self):
        self.state = 'confirmed'
        return self.state
'''