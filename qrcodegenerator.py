import pyqrcode

def qrcode():
    q=pyqrcode.create(input())
    q.png('yashqr.png',scale=6)
    print('QR code generated...')

if __name__=='__main__':
     qrcode()
