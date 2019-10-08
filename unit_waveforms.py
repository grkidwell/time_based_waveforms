# -*- coding: utf-8 -*-




class Three_state:
    
    def __init__(self,t1,t2,t3=0):
      
        self.t1,self.t2,self.t3 = t1,t2,t3
        self.Ts = self.t1+self.t2+self.t3
    
    def step(self,t):
        if t<0:
            kd=0.0
        elif t==0:
            kd=0.0
        else:
            kd=1.0
        return kd
            
    def t1_unit_pulse(self,t):
        if t<0:
            k=1.0
        else:
            k=self.step(self.t1-t)
        return k
      
    def t3_unit_pulse(self,t):
        return self.step(t-self.t1-self.t2)
      
    def t2_unit_pulse(self,t):
        return 1-self.t1_unit_pulse(t)-self.t3_unit_pulse(t)
    
    
    def repeating(self,t):
        period=self.Ts
        return t-(t//period)*period

