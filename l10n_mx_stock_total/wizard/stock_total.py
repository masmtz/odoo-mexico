# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Angelica Barrios angelicaisabelb@gmail.com
#              Humberto Arocha humberto@openerp.com.ve
#    Planified by: Humberto Arocha
#    Finance by: LUBCAN COL S.A.S http://www.lubcancol.com
#    Audited by: Humberto Arocha humberto@openerp.com.ve
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

from osv import fields, osv
import tools
from tools.translate import _


ESTADO =   [('desarrollo' , 'En Desarrollo')    ,
            ('produccion', 'En Produccion')     ,
            ('fin', 'Fin del Ciclo de Vida')    ,
            ('obsoleto', 'Obsoleto')            ,
            ('none', 'None')                    ,
           ]
TIPO =   [('almacenable' , 'Almacenable')       ,
            ('consumible', 'Consumible')        ,
            ('servicio', 'Servicio')            ,
           ]
SUMINISTRO =   [('comprar' , 'Comprar')         ,
                ('producir', 'Producir')        ,
           ]

class stock_total(osv.osv_memory):
    """
    Conteo del Stock
    """
    _name = "stock.total"
    _columns = {
        'tipo':fields.selection(TIPO, 'Tipo')                                   , 
        'categoria': fields.many2one('product.category', 'Categorias')          ,
        'estado':fields.selection(ESTADO, 'Estado')                             , 
        'suministro':fields.selection(SUMINISTRO, 'Metodo de Suministro')       , 
        'vendible': fields.boolean("Vendible")                                  ,
        'comprable': fields.boolean("Comprable")                                ,
        'alquilable': fields.boolean("Alquilable")                              ,
    }

stock_total()
