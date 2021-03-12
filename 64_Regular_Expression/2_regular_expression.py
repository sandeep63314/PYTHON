# (\AEDH_[A-Z]+_[A-Z][A-Z]_\d+_\d\d_\d\d_\d\d\d\d.txt\Z)|(\AEDH_[A-Z]+_[A-Z][A-Z]_\d\d_\d\d_\d\d\d\d.csv\Z)|(\AORCL_[A-Z]+_[A-Z][A-Z]_\d+_\d\d_\d\d_\d\d\d\d.txt\Z)|(\AORCL_[A-Z]+_[A-Z][A-Z]_\d\d_\d\d_\d\d\d\d.csv\Z)
# EDH_COREMAP_IN_08_12_2021.csv
# EDH_CORESITE_IN_21_08_12_2021.txt
# EDH_CORESITE_IN_37_10_12_2021.txt
# EDH_CORESITE_IN_19_08_12_2021.txt
# ORCL_TRANSACTIONMAP_IN_10_12_2021.csv
# ORCL_TRANSACTIONSITE_IN_21_08_12_2021.txt
# ORCL_TRANSACTIONSITE_IN_37_08_12_2021.txt
# ORCL_TRANSACTIONSITE_IN_19_08_12_2021.txt
# URL : https://www.zoho.com/in/books/kb/gst/valid-state-codes-list.html
import os,re,datetime

def getfiles(filename, ptrn):
    matchstring = None
    pattern = re.compile(ptrn)
    filestats = pattern.fullmatch(filename)
    if str(filestats) != 'None':
        matchstring = filestats.group()
    else:
        matchstring = 'None'
    return matchstring


def getdate(fileval):
    pattern = re.compile('\d\d_\d\d_\d\d\d\d')
    filestats = pattern.search(fileval)
    return filestats.group()


filemask = '(\AEDH_[A-Z]+_[A-Z][A-Z]_\d\d_\d\d_\d\d\d\d.csv\Z)|(\AORCL_[A-Z]+_[A-Z][A-Z]_\d\d_\d\d_\d\d\d\d.csv\Z)'
coremapfiles = [getfiles(f, filemask) for f in
                [file for file in os.listdir('C:\\Users\\lenovo\\Desktop\\PYTHON\\64_Regular_Expression\\localFiles')]
                if getfiles(f, filemask) != 'None']
coremaptype = {'EDH': 'edhcoremap', 'ORCL': 'orcltransactionmap'}

filemask = '(\AEDH_[A-Z]+_[A-Z][A-Z]_\d+_\d\d_\d\d_\d\d\d\d.txt\Z)|(\AORCL_[A-Z]+_[A-Z][A-Z]_\d+_\d\d_\d\d_\d\d\d\d.txt\Z)'
coresitefiles = [getfiles(f, filemask) for f in [file for file in os.listdir(
    'C:\\Users\\lenovo\\Desktop\\PYTHON\\64_Regular_Expression\\localFiles')] if getfiles(f, filemask) != 'None']
coresitetype = {'EDH': 'edhcoresite', 'ORCL': 'orcltransactionsite'}

filestatus = {'edhcoremap': False, 'edhcoresite': False, 'orcltransactionmap': False, 'orcltransactionsite': False}

currdate = datetime.date(2021, 12, 8).strftime('%d_%m_%Y')

try:
    with open('FILE_DETAIL_LOG.log', mode = 'w') as statuslog:
        statuslog.write('Validation for COREMAP files have started...\n')

    for coremapfile in coremapfiles:
        ptrn = re.compile('EDH|ORCL')
        fstatus = ptrn.match(coremapfile)
        filesource = fstatus.group()
        getfilename = coremaptype[filesource]
        if getdate(coremapfile) == currdate:
            filestatus[getfilename] = True
            with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
                statuslog.write(f'\n{coremapfile} is today\'s file.')
        else:
            with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
                statuslog.write(f'\n{coremapfile} is not today\'s file.\n\nFile {filesource}_COREMAP_IN_{currdate}.csv is not received\n')
except FileNotFoundError as er:
    with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
        statuslog.write(f'\n{er}')
finally:
    filestatuslog = open('FILE_STATUS_LOG.log', mode='w')
    for keys, values in filestatus.items():
        if keys in ('edhcoresite','orcltransactionsite'):
            status = 'All files are not verified for '
            with open('FILE_STATUS_LOG.log', mode='a') as statuslog:
                statuslog.write(f'{status}{keys}\n')
        else:
            status = 'All files are available for ' if values == True else 'All files are not available for '
            with open('FILE_STATUS_LOG.log', mode='a') as statuslog:
                statuslog.write(f'{status}{keys}\n')
    filestatuslog.close()
    with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
        statuslog.write('\n\nValidation for COREMAP file has ended...')

try:
    with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
        statuslog.write('\n\n-----xxx-----\n\nValidation for CORESITE files has started...\n')

    coresitestatus = {'EDH': {'19': False, '21': False, '37': False, '20': False},
                      'ORCL': {'19': False, '21': False, '37': False, '20': False}}

    for coresitefile in coresitefiles:
        ptrn = re.compile('EDH|ORCL')
        fstatus = ptrn.match(coresitefile)
        filesource = fstatus.group()
        getzonestatus = coresitestatus[filesource]
        if getdate(coresitefile) == currdate:
            with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
                statuslog.write(f'\n{coresitefile} is today\'s file.')
            ptrn = re.compile('\d\d')
            fstatus = ptrn.search(coresitefile)
            zonecode = fstatus.group()
            if zonecode in getzonestatus.keys():
                getzonestatus[zonecode] = True
                coresitestatus[filesource] = getzonestatus
            else:
                with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
                    statuslog.write(f'\nReceived CORESITE file:{coresitefile} with wrong zone code.')
        else:
            with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
                statuslog.write(f'\n{coresitefile} is not today\'s file.')

except FileNotFoundError as er:
    with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
        statuslog.write(f'\n{er}')

finally:
    notreceivedfiles = {}
    for filesource in ('EDH', 'ORCL'):
        filesnotpresent = {filesource: [keys for keys, values in coresitestatus[filesource].items() if
                                        coresitestatus[filesource][keys] == False]}
        if filesnotpresent[filesource] == []:
            getfilename = coresitetype[filesource]
            filestatus[getfilename] = True
        else:
            getfilename = coresitetype[filesource]
            filestatus[getfilename] = False
        notreceivedfiles.update(filesnotpresent)

    filesource = notreceivedfiles.keys()
    for source in filesource:
        codes = notreceivedfiles[source]
        for zonecode in codes:
            with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
                statuslog.write(f'\n\nFile {source}_CORESITE_IN_{zonecode}_{currdate}.txt is not received.')

    with open('FILE_DETAIL_LOG.log', mode='a') as statuslog:
        statuslog.write('\n\nValidation for CORESITE files has ended...')

    filestatuslog = open('FILE_STATUS_LOG.log', mode='w')
    for keys,values in filestatus.items():
        status = 'All files are available for ' if values == True else 'All files are not available for '
        with open('FILE_STATUS_LOG.log', mode='a') as statuslog:
            statuslog.write(f'{status}{keys}\n')