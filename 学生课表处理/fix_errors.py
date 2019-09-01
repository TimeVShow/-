#encoding = 'utf-8'
import json
import os
file_dir = 'file/'
list = os.listdir(file_dir)
for eachone in list:
    origin_dir = os.path.join(file_dir, eachone)
    dir = os.path.join(origin_dir, "json")
    json_file_list = os.listdir(dir)
    for each in json_file_list:
        txt_file = open(os.path.join(origin_dir, eachone + ".txt"), "r")
        #path = os.path.join(dir, each)
        path ="file\haiyun\json\/1.json"
        json_file = open(path)
        file = json.load(json_file)
        for line in txt_file:
            if(len(line.strip())!=0):
                print(line.strip())
                if(file.__contains__(line.strip()) == False):
                    file[line[:-1]] = [{'flag':True,'time':'1-2','special':[]},
                                       {'flag':True,'time':'3-4','special':[]},
                                       {'flag':True,'time':'5-6','special':[]},
                                       {'flag':True,'time':'7-8','special':[]},
                                       {'flag':True,'time':'9-11','special':[]}]
        json_file.close()
        json_file = open(os.path.join(origin_dir,each),"w+")
        json_file.write(json.dumps(file,  indent=4, separators=(',', ': ')))
        json_file.close()
        txt_file.close()