from bs4 import BeautifulSoup

class sinif():

    def __init__(self):
        print(1)

    def getHtmlList(self,url):
        #url = "E:\İndirilenlerDevam\s.html"
        jsonList = [[[] for i in range(8)] for j in range(17)]
        with open(url, encoding='utf8') as infile:
            soup = BeautifulSoup(infile.read(), "html.parser")
            tableTag = soup.find("table", {})
            trList = tableTag.findAll("tr")

            i = 0;
            j = 0;
            for tr in trList:
                j = 0
                tdList = tr.findAll("td")
                print('i' + str(i))
                for td in tdList:
                    print(td)
                    print('j' + str(j))

                    if td.b is None:
                        jsonList[i][j] = td.contents

                    else:
                        if td.b.i is None:
                            jsonList[i][j] = td.b.contents
                        else:
                            jsonList[i][j] = td.b.i.contents
                    j = j + 1
                i = i + 1
            print('######################################################')



        print(jsonList)

        f1 = open('kou1.html', 'w')
        #f1.write(str(json.dumps(jsonList)))
        f1.write(str(jsonList))
        f1.close()
        return jsonList

