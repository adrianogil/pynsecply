import sys
from pyPdf import PdfFileReader


helpmsg = "Simple PDF brute force script\n"
helpmsg += "Cracks pwds of the format <first 4 chars of email>0000-9999."
helpmsg += "Example: snow0653\n\n"
helpmsg += "Usage: pdfbrute.py <encrypted_pdf_file> <email_address>"
if len(sys.argv) < 2:
        print(helpmsg)
        sys.exit()
        
pdffile = PdfFileReader(file(sys.argv[1], "rb"))
if pdffile.isEncrypted == False:
        print("[!] The file is not protected with any password. Exiting.")
        exit

print("[+] Attempting to Brute force. This could take some time...")

def crack_only_numbers():
        z = ""
        for i in range(0,9999):
                z = str (i)
                while (len(z) < 4):
                        z = "0" + z
                
                a = str(sys.argv[2][:4] + str(z))
                print(a)
                if pdffile.decrypt(a) > 0:
                        print("[+] Password is: " + a)
                        print("[...] Exiting..")
                        sys.exit()

def crack_all_letters_and_numbers():
        import itertools

        max_size_attempt = 7

        stuff = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        for L in range(5, max_size_attempt):
            for subset in itertools.combinations_with_replacement(stuff, L):
                a = ""
                for s in subset:
                        a = a + s
                print(a)
                if pdffile.decrypt(a) > 0:
                        print("[+] Password is: " + a)
                        print("[...] Exiting..")
                        sys.exit()

        print("[...] Sorry, password couldn't be found!")
crack_all_letters_and_numbers()