import requests
def  saveToFile(url,path):
  r = requests.get(url)
  with open(path,"w") as f:
     f.write(r.text)

url = ("http://eduko.spikotech.com")
saveToFile(url,'F:\ThirdSemesterMaterials\DSA-LAB\Lab-5\Eduko.html')