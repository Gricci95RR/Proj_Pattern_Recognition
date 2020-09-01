from statistics import mean

class Representative:
    
    def Update(self,x,y,representatives):
            # __calcolo centroidi
            x_r_c=[]
            y_r_c=[]
            for i in range(0,len(x)):
                x_r_c.append([])
                y_r_c.append([])
                x_r_c[i]=mean(x[i])
                y_r_c[i]=mean(y[i])
            for i in range(0,len(x_r_c)):
                representatives[i][0]=x_r_c[i]
            for i in range(0,len(y_r_c)):
                representatives[i][1]=x_r_c[i] 
                
                return x_r_c, y_r_c, representatives

