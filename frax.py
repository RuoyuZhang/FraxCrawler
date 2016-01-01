import urllib
import urllib2
import re
import sys
import time
import commands
import requests

def frax(name,loaddata):
    url='http://www.shef.ac.uk/FRAX/tool.aspx?country=2'
    errorfile="/mnt/mito/home/ruoyu/project/other/xuan/error.file"
    errorF=open(errorfile,"w")
    try:
        r=requests.get(url)
    except:
        errorF.write(name)
        return False
        
    head=r.headers['set-cookie']
    cook=head.split(';')[0]
    mycook='country=2; lang=en; _ga=GA1.3.1439185508.1448469857; '+cook+'; _gat=1'
#    print mycook    
    with open('/mnt/mito/home/ruoyu/project/other/xuan/auth.html', "w") as f:
        f.write(r.content)

    a,b=commands.getstatusoutput('sh /mnt/mito/home/ruoyu/project/other/xuan/auth.sh')
    loaddata['ctl00$ContentPlaceHolder1$hdnAuthCode']=b
#    print loaddata
#    print loaddata['ctl00$ContentPlaceHolder1$hdnAuthCode']
    time.sleep(10)
    headers={'Host':'www.shef.ac.uk',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Cookie':mycook,}
    postdata=urllib.urlencode(loaddata) 
    
    try:
        req = urllib2.Request(url,postdata,headers)
        result = urllib2.urlopen(req).read()
    except:
        errorF.write(name)
        return False
    outname=name+'.html'
    with open(outname, "w") as f:
        f.write(result)



def main():
    mycook='country=2; lang=en; _ga=GA1.3.1439185508.1448469857; ASP.NET_SessionId=gocfyuoqu1aen5aklow3uoss; _gat=1'
    auth='b803eb69c5b6b9d1d5b6a418d69e217a'
    infile='/mnt/mito/home/ruoyu/project/other/xuan/frax.noT'
    outdir='/mnt/mito/home/ruoyu/project/other/xuan/noT'
    fIn = open(infile, 'r')
    for line in fIn:
        a = line.split()
#        if len(a)==13:
        [idnum,age,sex,weight,height,previousfracture,pfracturehip,currentsmoker,glucocorticoids,arthritis,osteoporosis,alcohol,Tvalue]=a
#        else:
#            [idnum,age,sex,weight,height,previousfracture,pfracturehip,currentsmoker,glucocorticoids,arthritis,osteoporosis,alcohol]=a
#            Tvalue='N/A'
#        print Tvalue    
        hdnsex=("1" if sex=='female' else "0")
        fracture=("yes" if previousfracture==1 else "no")
        fracture_hip=("yes" if pfracturehip==1 else "no")
        smoking=("yes" if currentsmoker==1 else "no")
        glu=("yes" if glucocorticoids==1 else "no")
        rhe_art=("yes" if arthritis==1 else "no")
        sec_ost=("yes" if osteoporosis==1 else "no")
        alcohol2=("yes" if alcohol==1 else "no")
        dxa=('N/A' if Tvalue=='N/A' else "T")
        thescore=("undefined" if Tvalue=='N/A' else Tvalue)
        bmdinput=('' if Tvalue=='N/A' else Tvalue)

#        print dxa
        
        loaddata={
            'ctl00$ScriptManager1':'ctl00$ContentPlaceHolder1$updResult|ctl00$ContentPlaceHolder1$btnCalculate',
            'ScriptManager1_TSM':';;AjaxControlToolkit, Version=4.1.40412.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:acfc7575-cdee-46af-964f-5d85d9cdcf92:ea597d4b:b25378d2',
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'', '__VIEWSTATE':'/wEPDwULLTExNDA4NDI3OTgPZBYCZg9kFgRmD2QWBAICDxUBGGNzcy9zdHlsZS5jc3M/MTQzMDIyMDMxMGQCBg8VAiFqcy9qcXVlcnktMS43LjEubWluLmpzPzE0MzAyMjAzMTYbanMvanNyZXNvdXJjZS5qcz8xNDMwMjIwMzE4ZAIBD2QWBgIBDxYCHgRUZXh0BZcJPG9wdGlvbiB2YWx1ZT0iZW4iIHNlbGVjdGVkPSdzZWxlY3RlZCc+RW5nbGlzaDwvb3B0aW9uPjxvcHRpb24gdmFsdWU9ImFyIiA+QXJhYmljPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iYmUiID5CZW5nYWxpPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iY2hzIiA+Q2hpbmVzZSBTaW1wbGlmaWVkPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iY2h0IiA+Q2hpbmVzZSBUcmFkaXRpb25hbDwvb3B0aW9uPjxvcHRpb24gdmFsdWU9ImNyIiA+Q3JvYXRpYW48L29wdGlvbj48b3B0aW9uIHZhbHVlPSJjeiIgPkN6ZWNoPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iZGEiID5EYW5pc2g8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJkZSIgPkdlcm1hbjwvb3B0aW9uPjxvcHRpb24gdmFsdWU9ImR1IiA+RHV0Y2g8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJlcyIgPkVzdG9uaWFuPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iZmkiID5GaW5uaXNoPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iZnIiID5GcmVuY2g8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJnciIgPkdyZWVrPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0iaWMiID5JY2VsYW5kaWM8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJpbiIgPkluZG9uZXNpYW48L29wdGlvbj48b3B0aW9uIHZhbHVlPSJpdCIgPkl0YWxpYW48L29wdGlvbj48b3B0aW9uIHZhbHVlPSJqcCIgPkphcGFuZXNlPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0ia28iID5Lb3JlYW48L29wdGlvbj48b3B0aW9uIHZhbHVlPSJsaSIgPkxpdGh1YW5pYW48L29wdGlvbj48b3B0aW9uIHZhbHVlPSJubyIgPk5vcndlZ2lhbjwvb3B0aW9uPjxvcHRpb24gdmFsdWU9InBvIiA+UG9saXNoPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0icHIiID5Qb3J0dWd1ZXNlIChQb3J0dWdhbCk8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJwdCIgPlBvcnR1Z3Vlc2U8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJybyIgPlJvbWFuaWFuPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0icnMiID5SdXNzaWFuPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0ic2UiID5Td2VkaXNoPC9vcHRpb24+PG9wdGlvbiB2YWx1ZT0ic2wiID5TbG92YWs8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJzcCIgPlNwYW5pc2g8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJ0aCIgPlRoYWk8L29wdGlvbj48b3B0aW9uIHZhbHVlPSJ0dSIgPlR1cmtpc2g8L29wdGlvbj5kAgIPZBYKAg8PFgIeBXN0eWxlBQt3aWR0aDo0MHB4O2QCEQ8WAh8BBQt3aWR0aDo0MHB4O2QCEg8WAh8BBQt3aWR0aDozMHB4O2QCEw8WAh8BBQt3aWR0aDozMHB4O2QCKQ9kFgJmD2QWAmYPDxYCHwAFCUNhbGN1bGF0ZWRkAgMPFgIfAAXYCDxhIGhyZWY9Ij9sYW5nPWVuIiBjbGFzcz0nc2VsZWN0ZWRMYW5nJz5FbmdsaXNoPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPWFyIiA+QXJhYmljPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPWJlIiA+QmVuZ2FsaTwvYT4gfCA8YSBocmVmPSI/bGFuZz1jaHMiID5DaGluZXNlIFNpbXBsaWZpZWQ8L2E+IHwgPGEgaHJlZj0iP2xhbmc9Y2h0IiA+Q2hpbmVzZSBUcmFkaXRpb25hbDwvYT4gfCA8YSBocmVmPSI/bGFuZz1jciIgPkNyb2F0aWFuPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPWN6IiA+Q3plY2g8L2E+IHwgPGEgaHJlZj0iP2xhbmc9ZGEiID5EYW5pc2g8L2E+IHwgPGEgaHJlZj0iP2xhbmc9ZGUiID5HZXJtYW48L2E+IHwgPGEgaHJlZj0iP2xhbmc9ZHUiID5EdXRjaDwvYT4gfCA8YSBocmVmPSI/bGFuZz1lcyIgPkVzdG9uaWFuPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPWZpIiA+RmlubmlzaDwvYT4gfCA8YSBocmVmPSI/bGFuZz1mciIgPkZyZW5jaDwvYT4gfCA8YSBocmVmPSI/bGFuZz1nciIgPkdyZWVrPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPWljIiA+SWNlbGFuZGljPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPWluIiA+SW5kb25lc2lhbjwvYT4gfCA8YSBocmVmPSI/bGFuZz1pdCIgPkl0YWxpYW48L2E+IHwgPGEgaHJlZj0iP2xhbmc9anAiID5KYXBhbmVzZTwvYT4gfCA8YSBocmVmPSI/bGFuZz1rbyIgPktvcmVhbjwvYT4gfCA8YSBocmVmPSI/bGFuZz1saSIgPkxpdGh1YW5pYW48L2E+IHwgPGEgaHJlZj0iP2xhbmc9bm8iID5Ob3J3ZWdpYW48L2E+IHwgPGEgaHJlZj0iP2xhbmc9cG8iID5Qb2xpc2g8L2E+IHwgPGEgaHJlZj0iP2xhbmc9cHIiID5Qb3J0dWd1ZXNlIChQb3J0dWdhbCk8L2E+IHwgPGEgaHJlZj0iP2xhbmc9cHQiID5Qb3J0dWd1ZXNlPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPXJvIiA+Um9tYW5pYW48L2E+IHwgPGEgaHJlZj0iP2xhbmc9cnMiID5SdXNzaWFuPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPXNlIiA+U3dlZGlzaDwvYT4gfCA8YSBocmVmPSI/bGFuZz1zbCIgPlNsb3ZhazwvYT4gfCA8YSBocmVmPSI/bGFuZz1zcCIgPlNwYW5pc2g8L2E+IHwgPGEgaHJlZj0iP2xhbmc9dGgiID5UaGFpPC9hPiB8IDxhIGhyZWY9Ij9sYW5nPXR1IiA+VHVya2lzaDwvYT4gZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WEAUeY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRzZXgxBR5jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJHNleDIFK2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkcHJldmlvdXNmcmFjdHVyZTEFK2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkcHJldmlvdXNmcmFjdHVyZTIFJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkcGZyYWN0dXJlaGlwMQUnY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRwZnJhY3R1cmVoaXAyBShjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGN1cnJlbnRzbW9rZXIxBShjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGN1cnJlbnRzbW9rZXIyBSpjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGdsdWNvY29ydGljb2lkczEFKmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkZ2x1Y29jb3J0aWNvaWRzMgUkY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRhcnRocml0aXMxBSRjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGFydGhyaXRpczIFJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkb3N0ZW9wb3Jvc2lzMQUnY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRvc3Rlb3Bvcm9zaXMyBSJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGFsY29ob2wxBSJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGFsY29ob2wy77cdcJT908w4/kofFjNkgAOu7ySeQUVLd7ncyP0uaDI=',
            '__VIEWSTATEGENERATOR':'E5DF20DC',
            '__EVENTVALIDATION':'/wEWKwLPq8D9AwKgq9TjDQKKgcOADALw7MSZBAKo4dL0BALq59vuDALFt7DdCAKWw8jJBgKz7c+cDALUqN/IAgLcvLLvDwL83oSmDQLUqNunAQKJ9ZRqAuHS5MQPAv29tMELAu+Vi6cFAvf937ELAvTmt7kBAqCm5IkKAsG6nLgOAs3d0eAGAoq3i/kGArO65o8KAvDE6YIDApLkvuEFAuWKxaoGAqX49ekFAoSLk94HAsT5o50EAuDwqfAPAqCCmbMMAsvSxOYMAoug9KUPAs6Tn/8MAo7hr7wPAo+g0YsDAs/S4UgCzrHgxQ8CjsPQhgwCnrGivwICl7P5gQgC6u3H+woecsR6Gfsbo4DqGyQzQtoVlSyaPGVM4udbKdUOawnhjw==',
            'language':'en',
            'ctl00$ContentPlaceHolder1$hdnethnicity':'2',
            'ctl00$ContentPlaceHolder1$hdnpreviousfracture':previousfracture,
            'ctl00$ContentPlaceHolder1$hdnpfracturehip':pfracturehip,
            'ctl00$ContentPlaceHolder1$hdncurrentsmoker':currentsmoker,
            'ctl00$ContentPlaceHolder1$hdnglucocorticoids':glucocorticoids,
            'ctl00$ContentPlaceHolder1$hdnarthritis':arthritis,
            'ctl00$ContentPlaceHolder1$hdnosteoporosis':osteoporosis,
            'ctl00$ContentPlaceHolder1$hdnalcohol':alcohol,
            'ctl00$ContentPlaceHolder1$hdnbmd':dxa,
            'ctl00$ContentPlaceHolder1$hdnthescore':thescore,
            'ctl00$ContentPlaceHolder1$hdnsex':hdnsex,
            'ctl00$ContentPlaceHolder1$hdnbmi':'',
            'ctl00$ContentPlaceHolder1$hdnAuthCode':auth,
            'ctl00$ContentPlaceHolder1$nameid':'',
            'ctl00$ContentPlaceHolder1$toolage':age,
            'ctl00$ContentPlaceHolder1$toolagehidden':age,
            'ctl00$ContentPlaceHolder1$year':'',
            'ctl00$ContentPlaceHolder1$month':'',
            'ctl00$ContentPlaceHolder1$day':'',
            'ctl00$ContentPlaceHolder1$sex':sex,
            'ctl00$ContentPlaceHolder1$toolweight':weight,
            'ctl00$ContentPlaceHolder1$toolweighthidden':weight,
            'ctl00$ContentPlaceHolder1$ht':height,
            'ctl00$ContentPlaceHolder1$toolheighthidden':height,
            'ctl00$ContentPlaceHolder1$facture':fracture,
            'ctl00$ContentPlaceHolder1$facture_hip':fracture_hip,
            'ctl00$ContentPlaceHolder1$smoking':smoking,
            'ctl00$ContentPlaceHolder1$glu':glu,
            'ctl00$ContentPlaceHolder1$rhe_art':rhe_art,
            'ctl00$ContentPlaceHolder1$sec_ost':sec_ost,
            'ctl00$ContentPlaceHolder1$alcohol':alcohol2,
            'dxa':dxa,
            'ctl00$ContentPlaceHolder1$bmd_input':bmdinput,
            '__ASYNCPOST':'TRUE',
            'ctl00$ContentPlaceHolder1$btnCalculate':'Calculate',
        }

        name=outdir+'/'+idnum
        frax(name,loaddata)
        time.sleep(5)
        

if __name__ == "__main__":
    main()

