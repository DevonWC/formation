import math

#re1 = [38, 42, 50, 56, 59, 63, 70, 80, 95, 110]
#re2 = [350, 325, 297, 270, 256, 246, 238, 223, 215, 208]
#re1 = [5, 8, 7, 10, 6, 7, 9, 3, 8 ,2]
#re2 = [6, 9, 8, 10, 5, 7, 8, 4, 6, 2]
re1 = [0.003, 0.004, 0.009, 0.021, 0.023, 0.030, 0.035, 0.037, 0.044, 0.051, 0.058, 0.058, 0.067, 0.080, 0.080, 0.083, 0.091, 0.092, 0.064, 0.028]
re2 = [5.6, 7.2, 8.1, 9.9, 6.0, 8.2, 6.3, 10.0, 8.5, 13.2, 8.4, 11.1, 11.1, 13.2, 13.4, 11.5, 9.8, 16.1, 7.0, 5.9]

class MainTable():

    def __init__(self, re1, re2):
        self.re1 = re1 # xi
        self.re2 = re2 # yi
        self.n = len(self.re1)

        if type(self.re1) != type([]) or type(self.re2) != type([]) or (len(self.re1)+len(self.re2)) < 2 or len(self.re1) != len(self.re2):
            print("Dados incompletos ou com formatos errados, o script não irá funcionar corretamente...")

    def xi(self):
        self.x_dict = {
            'xi': re1,
            'sum' : 0,
            'xi2': [],
            'xi2sum': 0,
        }

        for i in self.re1:
            self.x_dict['sum'] += i
            self.x_dict['xi2'].append(i*i)
            self.x_dict['xi2sum'] += i*i
        
        self.x_dict['xiavg'] = self.x_dict['sum']/len(self.re1)


    def yi(self):
        self.y_dict = {
            'yi': re1,
            'sum' : 0,
            'yi2': [],
            'yi2sum': 0,
            'yiavg': 0,
        }

        for i in self.re2:
            self.y_dict['sum'] += i
            self.y_dict['yi2'].append(i*i)
            self.y_dict['yi2sum'] += i*i
        
        self.y_dict['yiavg'] = self.y_dict['sum']/len(self.re2)


    def xiyi(self):
        self.xy_dict = {
            'xiyi': [],
            'sum': 0
        }

        for i in range(0, len(self.re1)):
            self.xy_dict['xiyi'].append(self.re1[i] * self.re2[i])
            self.xy_dict['sum'] += self.re1[i] * self.re2[i]
            
    
    def pearson(self):
        self.r = 0
        self.a = (self.n*self.xy_dict['sum']) - (self.x_dict['sum']*self.y_dict['sum'])
        self.b = math.sqrt( ((self.n*self.x_dict['xi2sum']) - (self.x_dict['sum']*self.x_dict['sum'])) * ((self.n*self.y_dict['yi2sum']) - (self.y_dict['sum']*self.y_dict['sum'])))
        self.r = self.a/self.b

        x = self.r

        self.tc = [
        (x >= 0.9) or (x <= -0.9), # Correlação Muito forte
        (x >= 0.7 and x < 0.9) or (x <= -0.7 and x > -0.9), # Correlação forte
        (x >= 0.5 and x < 0.7) or (x <= -0.5 and x > -0.7), # correlação Moderada
        (x >= 0.3 and x < 0.5) or (x <= -0.3 and x > -0.5), # Correlação Fraca
        (x >= 0 and x < 0.3) or (x > -0.3), # Correlação Desprezivel
          ]

        self.co = ['muito forte', "forte", "moderada", "fraca", "desprezivel"]
        
        if(self.r > 0):
            self.sig = "positiva"
        else:
            self.sig = "negativa"

        for i, k in enumerate(self.tc):
            if k:
                self.rel = self.co[i]
                break

        return "Correlação de Pearson: {0} | indica uma correlação {1} {2}".format(self.r, self.sig, self.rel)

    def reta(self):
        self.reta = 0
        self.ra = (self.n*self.xy_dict['sum']) - (self.x_dict['sum']*self.y_dict['sum'])
        self.rb = (self.n*self.x_dict['xi2sum']) - (self.x_dict['sum']*self.x_dict['sum'])
        self.reta = self.ra/self.rb

        self.cb = self.y_dict['yiavg'] - (self.reta*self.x_dict['xiavg'])

        return "Equação de reta: y = {0}x + {1}".format(self.reta, self.cb)

    def yCoordinates(self, x):
        
        return (self.reta*x) + self.cb
    

m = MainTable(re1, re2)

m.xi()
m.yi()
m.xiyi()
print(m.pearson())
print(m.reta())
print(m.yCoordinates(0.070))