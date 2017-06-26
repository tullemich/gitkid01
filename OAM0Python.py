import urllib.request, urllib.error, json, csv, os

url = 'https://api.oadoi.org/'
mail = '?email=lajh@kb.dk'
file_name = 'lookup.csv'
json_name = 'json.js'

def pullDataAPI(url):
    req = urllib.request.Request(url)
    try:
       response = urllib.request.urlopen(req)
       data = json.loads(response.read())
       writeJson2CSV(json_name, data)
       print(data)


    except urllib.error.HTTPError as e:
        print(e.reason)

def openCSV():
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        next(f)
        for row in reader:
            pullDataAPI(url + row[0] + mail)

def writeJson2CSV(json_name, data):
    #with open(json_name, 'w') as outfile:
    #    json.dump(data, outfile)
    #with open (json_name, mode="r+") as file:
    with open (json_name, mode="a") as file:
        #file.seek(os.stat(json_name).st_size -1)
        #file.write( ",{}]".format(json.dumps(data)) )
        file.write(json.dumps(data))

def main():
    openCSV()



if __name__ == '__main__':
    main()
