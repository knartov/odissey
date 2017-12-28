# -*- coding: utf-8 -*-

import ftplib

import os

ftp = ftplib.FTP('ftp.zakupki.gov.ru')
ftp_user = 'free'
ftp_password = 'free'
print(ftp.login(ftp_user, ftp_password))

ftp.cwd('fcs_regions')
ftp.cwd('PG-PZ')

filenames = ftp.nlst()

print(filenames)

# fcs_regions = open('fcs_regions.txt', 'w+')
# for x in filenames:
#     fcs_regions.write(x+'\n')

print(os.getcwd())

# fcs_regions.close()


'''
ftp.cwd('fcs_regions')
ftp.cwd('Adygeja_Resp')
ftp.cwd('notifications')
'''

'''
filenames = ftp.nlst()

for filename in filenames:
    host_file = os.path.join(
        'C:\\Users\\nartok\\Box Sync\\Project One\\Zakupki', filename
    )

    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
    except ftplib.error_perm:
        pass

ftp.quit()
'''

# ftp.cwd('fcs_regions')

# data = ftp.retrlines('LIST')

# print(data)

# out = 'C:\\Users\\nartok\\Box Sync\\Project One\\Zakupki\\_readme.txt'
#
# with open(out, 'wb') as f:
#     ftp.retrbinary('RETR ' + '_readme.txt', f.write)

"""
ftp.cwd('Tulskaja_obl')
data = ftp.retrlines('LIST')
print(data)
"""

# ftp.cwd('notifications')
# filenames = ftp.nlst()
# print(filenames)

# out = 'C:\\Users\\nartok\\workspace\\_readme.txt'

# with open(out, 'wb') as f:
# ftp.retrbinary('RETR ' + '_readme.txt', f.write)
