import requests
from bs4 import BeautifulSoup

start = 21850
dataInFile = ""
numberInfo = 1
while(start <= 30000):
    try:
        source = requests.get("http://bismainformatika.com/sertifikasi/cetak/cetak_form_pendaftaran.php?id=" + str(start))
    except KeyboardInterrupt or requests.ConnectionError:
        with open("lanjutan.txt", 'w') as wr:
            wr.write(dataInFile)
            wr.write("\n\n\nCheck point --> " + str(start))
        exit()
    # source = requests.get("http://bismainformatika.com/sertifikasi/cetak/cetak_form_pendaftaran.php?id=21757")
    soup = BeautifulSoup(source.content,'lxml')
    tables = soup.select_one('table[style="margin-left: 50px;"]')
    rows = tables.find_all('td')
    name = "".join(str(rows[2].text).split())

    # check data empty or not
    if name == "":
        start +=1
        print("\rkosong data ke-" + str(start),end="")
        continue
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
    print("\r\nData didapat " + str(numberInfo),end="")
    start +=1
    numberInfo +=1
with open("lanjutan.txt",'w') as wr:
    wr.write(dataInFile)