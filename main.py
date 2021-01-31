import requests
from bs4 import BeautifulSoup

start = 21124
dataInFile = ""
while(start <= 30000):
    source = requests.get("http://bismainformatika.com/sertifikasi/cetak/cetak_form_pendaftaran.php?id=" + str(start))
    soup = BeautifulSoup(source.content,'lxml')
    tables = soup.select_one('table[style="margin-left: 50px;"]')
    rows = tables.find_all('td')
    name = "".join(str(rows[2].text).split())
    # check data empty or not
    if name == "":
        start +=1
        continue;
    # make each one row entered
    number_space = 0
    data = f"-------{str(start)}-------\n"
    for row in rows :
        if number_space == 3:
            data += "\n"
            number_space =0
        # clearing \t,\n,\r
        data += " ".join(row.text.split())
        number_space += 1
    dataInFile += data +"\n\n"
    start +=1
with open("Data3.txt",'w') as wr :
    wr.write(dataInFile)