# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:37:03 2018

@author: 李弘一萌
"""

#from .Commodities.A.A_Factory import A_Factory
from .Commodities.AL.AL_Factory import AL_Factory
#from .Commodities.B.B_Factory import B_Factory
from .Commodities.BU.BU_Factory import BU_Factory
from .Commodities.CF.CF_Factory import CF_Factory
from .Commodities.CU.CU_Factory import CU_Factory
from .Commodities.HC.HC_Factory import HC_Factory
from .Commodities.I.I_Factory import I_Factory
from .Commodities.J.J_Factory import J_Factory
from .Commodities.JM.JM_Factory import JM_Factory
from .Commodities.L.L_Factory import L_Factory
from .Commodities.M.M_Factory import M_Factory
from .Commodities.MA.MA_Factory import MA_Factory
from .Commodities.NI.NI_Factory import NI_Factory
from .Commodities.OI.OI_Factory import OI_Factory
from .Commodities.P.P_Factory import P_Factory
from .Commodities.PP.PP_Factory import PP_Factory
from .Commodities.RB.RB_Factory import RB_Factory
from .Commodities.RU.RU_Factory import RU_Factory
from .Commodities.SR.SR_Factory import SR_Factory
from .Commodities.TA.TA_Factory import TA_Factory
from .Commodities.Y.Y_Factory import Y_Factory
from .Commodities.ZC.ZC_Factory import ZC_Factory
from .Commodities.ZN.ZN_Factory import ZN_Factory




class Global_Factory(object):
    @staticmethod
    def getobj(col, cmt_name):
        factory_class = eval(cmt_name + "_Factory")
        obj = factory_class.getobj(col)
        return obj

    @staticmethod
    def getBaseObj(cmt_name):
        factory_class = eval(cmt_name + "_Factory")
        obj = factory_class.getBaseObj()
        return obj    
