import pydicom
import os
import shutil


#direcrory for base seria for majority of cases
ser1 =r'C:\Users\sa-comp\Documents\ser1-base\30062.000000-NA-97495'
#direcrorys for two appendix series. We use it for 3 series cases
ser2=r'C:\Users\sa-comp\Documents\ser2'
#directory for output
ser3=r'C:\Users\sa-comp\Documents\ser-3'

output='C:/Users/sa-comp/Documents/test_for/'


def changeThicknessAndWindow(dcm, outputDir,filename,newWidth,newCenter, newThickness,PatintId=None, studyUUID=None):
    """Change Slice Thickness and window parameters in source seria. Save new seria in output directory outputDir.
        Change studyUUID and PatintId if it nessary."""
    try:
        dataset=pydicom.dcmread(dcm, force=True)
        if studyUUID is not None:
            dataset[0x0020000D].value=studyUUID
            dataset[0x00100020].value=PatintId
        if newWidth=='delete':
            del dataset[0x00180050]
        else:
            dataset[0x00180050].VR = 'LO'
            dataset[0x00180050].value=newThickness
            dataset[0x00180050].VR = 'DS'
        if newCenter == 'delete':
            del dataset[0x00281050]
        else:
            dataset[0x00281050].VR = 'LO'
            dataset[0x00281050].value = newCenter
            dataset[0x00281050].VR = 'DS'
        if newThickness=='delete':
            del dataset[0x00281051]
        else:
            dataset[0x00281051].VR = 'LO'
            dataset[0x00281051].value=newWidth
            dataset[0x00281051].VR = 'DS'
        instanseUID=str(dataset[0x00080018].value)
        dataset.save_as(filename=str(os.path.join(outputDir, f"{instanseUID}.dcm")), write_like_original=False)
        return {"filename":filename, 'status': "ok"}
    except Exception as e:
        print(e)
        return {"filename":filename, 'status': "error"}


def changeMultyThicknessAndWindow(dcm, outputDir,filename,newWidth,newCenter, newThickness,PatintId=None, studyUUID=None):
    """Change Slice Thickness and window parameters in source seria. Save new seria in output directory outputDir.
        Change studyUUID and PatintId if it nessary."""
    try:
        dataset=pydicom.dcmread(dcm, force=True)
        if dataset[0x00200013].value %2 ==0:
            dataset[0x00180050].value=newThickness
        else:
            dataset[0x00180050].value = newThickness*2
        dataset[0x00281050].value = newCenter
        dataset[0x00281051].value = newWidth
        instanseUID = str(dataset[0x00080018].value)
        dataset.save_as(filename=str(os.path.join(outputDir, f"{instanseUID}.dcm")), write_like_original=False)
        return {"filename":filename, 'status': "ok"}
    except:
        return {"filename":filename, 'status': "error"}



#The array for base cases. No need change UUIDs, language and other
data=[
    {'case':1,'other':[{'files':ser1, 'newThickness':'3.1', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':2,'other':[{'files':ser1, 'newThickness':'3.0001', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':3,'other':[{'files':ser1, 'newThickness':'4.0', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':4,'other':[{'files':ser1, 'newThickness':'31e-1', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':5,'other':[{'files':ser1, 'newThickness':'delete', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':6,'other':[{'files':ser1, 'newThickness':None, 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':7,'other':[{'files':ser1, 'newThickness':'3', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':8,'other':[{'files':ser1, 'newThickness':'3.0', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':9,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':10,'other':[{"newThickness":"0.0001", "newCenter":"-600", "newWidth":"1600"}]},
    {'case':11,'other':[{'files':ser1, 'newThickness':'2.9999', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':12,'other':[{'files':ser1, 'newThickness':'3E0', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':13,'other':[{'files':ser1, 'newThickness':'25E-1', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':14,'other':[{'files':ser1, 'newThickness':'0', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':15,'other':[{'files':ser1, 'newThickness':'-3', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':17,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':18,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'1200'}]},
    {'case':19,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'1600'}]},
    {'case':20,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'800'}]},
    {'case':21,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'1200'}]},
    {'case':22,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'1600'}]},
    {'case':23,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-700', 'newWidth':'800'}]},
    {'case':24,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-700', 'newWidth':'1200'}]},
    {'case':25,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-700', 'newWidth':'1600'}]},
    {'case':26,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-6E2', 'newWidth':'1.2E3'}]},
    {'case':27,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'0', 'newWidth':'300'}]},
    {'case':28,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'0', 'newWidth':'450'}]},
    {'case':29,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'0', 'newWidth':'600'}]},
    {'case':30,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'30', 'newWidth':'300'}]},
    {'case':31,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'30', 'newWidth':'450'}]},
    {'case':32,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'30', 'newWidth':'600'}]},
    {'case':33,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'60', 'newWidth':'300'}]},
    {'case':34,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'60', 'newWidth':'450'}]},
    {'case':35,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'60', 'newWidth':'600'}]},
    {'case':36,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'3E1', 'newWidth':'4.5E2'}]},
    {'case':37,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'80', 'newWidth':'-10'}]},
    {'case':38,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'1800', 'newWidth':'-800'}]},
    {'case':39,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'59.9999', 'newWidth':'300'}]},
    {'case':40,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'59.9999', 'newWidth':'450'}]},
    {'case':41,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'59.9999', 'newWidth':'600'}]},
    {'case':42,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-400', 'newWidth':'700'}]},
    {'case':43,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'1600.0001'}]},
    {'case':44,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'1600.0001'}]},
    {'case':45,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-700', 'newWidth':'1600.0001'}]},
    {'case':46,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'500', 'newWidth':'2500'}]},
    {'case':52,'other':[{'files':ser1, 'newThickness':'@2.0', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':53,'other':[{'files':ser1, 'newThickness':'2.0%', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':54,'other':[{'files':ser1, 'newThickness':'*2.0', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':55,'other':[{'files':ser1, 'newThickness':'2&.0', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':56,'other':[{'files':ser1, 'newThickness':'(2.0)', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':57,'other':[{'files':ser1, 'newThickness':'2.0)', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':58,'other':[{'files':ser1, 'newThickness':'^2.0', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':59,'other':[{'files':ser1, 'newThickness':'2.0?', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':60,'other':[{'files':ser1, 'newThickness':'/2.0', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':61,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'@-500', 'newWidth':'800'}]},
    {'case':62,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500%', 'newWidth':'800'}]},
    {'case':63,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'*-500', 'newWidth':'800'}]},
    {'case':64,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-50&0', 'newWidth':'800'}]},
    {'case':65,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'(-500)', 'newWidth':'800'}]},
    {'case':66,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500)', 'newWidth':'800'}]},
    {'case':67,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'^-500', 'newWidth':'800'}]},
    {'case':68,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500?', 'newWidth':'800'}]},
    {'case':69,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'/-500', 'newWidth':'800'}]},
    {'case':70,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500,0', 'newWidth':'800'}]},
    {'case':71,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'@800'}]},
    {'case':72,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'800%'}]},
    {'case':73,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'*800'}]},
    {'case':74,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'80&0'}]},
    {'case':75,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'(800)'}]},
    {'case':76,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'800)'}]},
    {'case':77,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'^800'}]},
    {'case':78,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'800?'}]},
    {'case':79,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'/800'}]},
    {'case':80,'other':[{'files':ser1, 'newThickness':'2.0', 'newCenter':'-500', 'newWidth':'800,0'}]},
    {'case':83,'other':[{'files':ser1, 'newThickness':'aslkklsjdjlao', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':84,'other':[{'files':ser1, 'newThickness':'LKJGJLO', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':87,'other':[{'files':ser1, 'newThickness':'1.0', 'newCenter':'qwrpoutew', 'newWidth':'800'}]},
    {'case':88,'other':[{'files':ser1, 'newThickness':'1.0', 'newCenter':'POIIIYU', 'newWidth':'800'}]},
    {'case':91,'other':[{'files':ser1, 'newThickness':'1.0', 'newCenter':'-500', 'newWidth':'vbcvbnc'}]},
    {'case':92,'other':[{'files':ser1, 'newThickness':'1.0', 'newCenter':'-500', 'newWidth':'MNBKJH'}]},
    {'case':93,'other':[{'files':ser1, 'newThickness':'0.797699800122221', 'newCenter':'-500', 'newWidth':'800'}]},
    {'case':94,'other':[{'files':ser1, 'newThickness':'1.0', 'newCenter':'-500.8775454323228349823120078338499344322112345454', 'newWidth':'800'}]},
    {'case':95,'other':[{'files':ser1, 'newThickness':'1', 'newCenter':'-500.0', 'newWidth':'800.0993348039840293849082330984384928903842983908290384982903849087782384829392834728378987665656388302023949384394897549475399839843347758383758358383833998822838477457577564333398889823223234455456757689686797678077878666553322223455556667889999777877347637463657637657483453453453553353535223453453656565447676767788899'}]},
    {'case': 96, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': 'delete', 'newWidth': '800'}]},
    {'case': 97, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': None, 'newWidth': '800'}]},
    {'case': 98, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': '-500', 'newWidth': 'delete'}]},
    {'case': 99, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': '-500', 'newWidth': None}]},
    {'case': 100, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': r'400\-500', 'newWidth': r' 2000\800'}]},
    {'case': 101, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': r'400\-500', 'newWidth': r'800\2000'}]},
    {'case': 102, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': r'0\400', 'newWidth': r'300\2000'}]},
    {'case': 103, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': r'400\500\600\-500', 'newWidth': r'2000\250\3000\800'}]},
    {'case': 104, 'other':[{'files':ser1,'newThickness': '1.0', 'newCenter': r'0\400\-500', 'newWidth': r'300\2000\800'}]},
    {'case':'47', 'other':[
        {'files':ser1, 'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'1600'},
        {'files': ser2, 'newThickness': '1.0', 'newCenter': '45', 'newWidth': '450'},
        {'files': ser3, 'newThickness': '3.1', 'newCenter': '45', 'newWidth': '450'}
    ]
     },
    {'case': '48', 'other': [
        {'files': ser1, 'newThickness': '2.0', 'newCenter': '-600', 'newWidth': '1200'},
        {'files': ser2, 'newThickness': '1.0', 'newCenter': '-500', 'newWidth': '800'},
        {'files': ser3, 'newThickness': '3.1', 'newCenter': '45', 'newWidth': '450'}
    ]
     },
    {'case': '49', 'other': [
        {'files': ser1, 'newThickness': '2.0', 'newCenter': '0', 'newWidth': '300'},
        {'files': ser2, 'newThickness': '1.5', 'newCenter': '60', 'newWidth': '600'},
        {'files': ser3, 'newThickness': '1.0', 'newCenter': '45', 'newWidth': '450'}
    ]
     },
    {'case': '50', 'other': [
        {'files': ser1, 'newThickness': '2.0', 'newCenter': '400', 'newWidth': '2000'},
        {'files': ser2, 'newThickness': '159', 'newCenter': '60', 'newWidth': '600'},
        {'files': ser3, 'newThickness': '1.0', 'newCenter': '0', 'newWidth': '700'}
    ]
     },
    {'case': '51', 'other': [
        {'files': ser1, 'newThickness': 'delete', 'newCenter': '-600', 'newWidth': '1200'},
        {'files': ser2, 'newThickness': None, 'newCenter': '-500', 'newWidth': '800'}
    ]
     }
      ]


data1=[{'case':16,'newThickness':'2.0', 'newCenter':'-600', 'newWidth':'1600'}]


#create base data for base cases
for x in data:
    case = x['case']
    outputDir = f"{output}/{case}/"
    isExist = os.path.exists(outputDir)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(outputDir)
        print("The new directory is created!")
    for o in x['other']:
        workdir=o['files']
        path=os.listdir(workdir)
        for index, file in enumerate(path):
            if len(x['other']) > 1:
                print(changeThicknessAndWindow(os.path.join(workdir, file),
                                                    outputDir,
                                                    filename=file,
                                                    newThickness=o['newThickness'],
                                                    newCenter=o['newCenter'],
                                                    newWidth=o['newWidth'],
                                                    PatintId='LIDC-IDRI-0467',
                                                    studyUUID='1.3.6.1.4.1.14519.5.2.1.6279.6001.182190805623310236601030915541'))
            else:
                print(changeThicknessAndWindow(os.path.join(workdir, file),
                                               outputDir,
                                               filename=file,
                                               newThickness=o['newThickness'],
                                               newCenter=o['newCenter'],
                                               newWidth=o['newWidth']))

    shutil.make_archive(outputDir, 'zip', outputDir)

#Create appendix seria. Set different Slice Thickness for even and odd slice number
for x in data1:
    case=x['case']
    outputDir=f"{output}/{case}/"
    isExist = os.path.exists(outputDir)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(outputDir)
        print("The new directory is created!")
    files=os.listdir(ser1)
    for index, file in enumerate(files):
        print(changeThicknessAndWindow(os.path.join(ser1, file),
                                       outputDir,
                                       filename=file,
                                       newThickness=x['newThickness'],
                                       newCenter=x['newCenter'],
                                       newWidth=x['newWidth']))
    shutil.make_archive(outputDir, 'zip', outputDir)
#
