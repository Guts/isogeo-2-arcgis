from json import dumps, load
import json
import time


#récupération du time 
date = time.clock()



def remplir(id,idu,path,update):
    file = open("file.json", "a") 
    line={'date': date,'line':{'ID':id, 'IDU':idu,'local_Path':path,'Last_update':update}}
    json.dump(line, file, indent=4)
    file.close()

remplir(arcpy.GetParameterAsText(0),arcpy.GetParameterAsText(1),arcpy.GetParameterAsText(2),'test')
