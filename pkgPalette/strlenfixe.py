#!-coding:UTF-8
'''
Created on 3 oct. 2014

@author: gsuivre
'''


class Palette(object):
    """Classe definissant une palette caracterisée par :.
    -som N° SSCC
    -son nombre de carton
    -son ou ses articles
    -son ou ses N° Lot
    -son nombre de cartons 
    
    """
    nb_palette=0
    
#     def strlenfixe(self,lestr,longueur=25,car="0"):
#         lestr=str(lestr)
#         while len(lestr)<longueur:
#             lestr=car+lestr
#         return lestr

    def __init__(self):
        self._sscc="00000"
        self._dlc=""
        self._lot=""
        self._an = self._dlc [:4] 
        self._mois = self._dlc [4:6]
        self._jours = self._dlc [6:8]
        self._nbcarton=0
        Palette.nb_palette+=1
        
    @property
    def sscc(self):
        return self._sscc
    @property
    def dlc(self):
        return self._dlc
    @property
    def lot(self):
        return self._lot
    @property
    def jours(self):
        return self._dlc [6:8] 
    @property
    def mois(self):
        return self._dlc[4:6]
    @property
    def an(self):
        return self._dlc[:4]
    @property
    def nbcartons(self):
        return self._nbcarton
    
        
    @sscc.setter
    def sscc(self, value,longueur=5,car="0"):
        lestr=str(value)
        print lestr
        while len(lestr)<longueur:
            lestr=car+lestr
        self._sscc = lestr          
    @dlc.setter
    def dlc(self,value):
        self._dlc = value
    @lot.setter()
    def lot(self,value):
        
        self._lot=value
    @nbcarton.setter
    def nbcarton(self,value):
        self._nbcarton=value
       
 
    @sscc.deleter
    def sscc(self):
        print 'delete'
        self._sscc = None
    @dlc.deleter
    def dlc(self):
        print 'delete'
        self._dlc = None
    @lot.deleter
    def lot(self):
        self._lot = None 
    @nbcarton.deleter
    def nbcarton(self):
        self._nbcarton = None


            
if __name__ == '__main__':
    pal1=Palette()
#     pal1.sscc='1'
#     print pal1.sscc
    pal1.dlc="20140227"
    print pal1.dlc
    print pal1.jours
    print pal1.an 
    print pal1.mois
    

 
#  def __init__(self):
#         self._replique = 'OKAY'




    
    
#     def strlenfixe(lestr,longueur=25,car="0"):
#     lestr=str(lestr)
#     while len(lestr)<longueur:
#         lestr=car+lestr
#     return lestr

#print (strlenfixe("000iii51"))

