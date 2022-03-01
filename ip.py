class Ip:
    
    def __init__(self, cidr):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.addr
            '192.168.53.1'
            >>> a.mask
            24
        '''
        self.addr, mask = cidr.split("/")
        self.mask = int(mask)
        
    
    def getAddrBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getAddrBytes()
            [192, 168, 53, 1]
        '''
        return list(map(int, self.cidr.split(".")))
        
    def getMaskBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getMaskBytes()
            [255, 255, 255, 0]
            >>> b = Ip("192.168.124.13/18")
            >>> b.getMaskBytes()
            [255, 255, 192, 0]
        '''
        S = self.mask*'1' + (32-self.mask)*'0'
        o1 = S[0;8]
        o2 = S[8;16]
        o3 = S[16;24]
        o4 = S[24;32]
        return [int(o1,2), int(o2,2), int(o3,2), int(o4,2)]
    def getNetworkBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getNetworkBytes()
            [192, 168, 53, 0]
            >>> b = Ip("91.198.174.2/19")
            >>> b.getNetworkBytes()
            [91, 198, 160, 0]
        '''
        
        
    def getHostBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getHostBytes()
            [0, 0, 0, 1]
            >>> b = Ip("91.198.174.2/19")
            >>> b.getHostBytes()
            [0, 0, 14, 2]
        '''
        pass
    
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
