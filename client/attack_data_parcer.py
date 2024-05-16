import requests 

class Attack_Data:
    def __inti__(self , url , subarray):
        self.url = url
        self.subarray = subarray
    def parce(self):
        data = requests.get(self.url)
        data.json()

        service = data[self.subarray]
        ips = service.keys()
        flags = [[]]
        for ip in ips:
            flags[ip] = service[ip]
        return flags