class Env(object):
"""
    Strawry environment ...
"""
    def __init__(self):
        self.n_action=16
        self.n_state=500
    def get_state(self):        
        x1=cap(self.temp, 10, 25, 5)
        x2=cap(self.humi, 10, 100, 5)
        x3=cap(self.co2, 300, 3000, 5)
        x4=self.light
        x5=self.watp
        return x1*5*5*2*2 + x2*5*5*2*2 + x3*2*2 + x4*2 +x5
    
    def reset(self, temp=25, humi=80, co2=200, light=0, watp=0):        
        self.temp=temp
        self.humi=humi
        self.co2=co2
        self.light=light
        self.watp=watp
        return self.get_state()
    
    def set_target(self, temp=25, humi=80, co2=200, light=0, watp=0):
        self.t_temp=temp
        self.t_humi=humi
        self.t_co2=co2
        self.t_light=light
        self.t_watp=watp
        return self.get_state()
    
    def get_reward(self):
        if self.t_temp-1<self.temp and self.temp<=self.t_temp+1:
            if self.t_humi-5<self.humi and self.humi<=self.t_humi+5:
                return 1
        return -0.1
    
    def code2int(self,code):
        #(comp,mist,light,watp)
        return code[0]*8 + code[1]*4 + code[2]*2 + code[3]
    
    def int2code(self,a=0):
        b=bin(16+a)
        return int(b[-4]),int(b[-3]),int(b[-2]),int(b[-1])
    
    def step(self,a):
        comp,mist,light,watp = self.int2code(a)
        if comp==1:
            self.humi-=5
            self.temp-=1
        if mist==1:
            self.humi+=5
        if light==1:
            self.humi+=1
            self.temp+=1
        if watp==1:
            self.humi+=1
        return self.get_state(), self.get_reward(), 0, 0
    
    def render(self):
        print( "temp:{}, humi:{}, co2:{}, light:{}, watp{}".format(
             self.temp, self.humi, self.co2, self.light, self.watp))