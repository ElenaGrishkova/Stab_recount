# -*- coding: utf-8 -*-
import pandas as pd
#GAME_5STEP_DIR_NAMES=set()
GAME_5STEP_DIR_NAMES={u'08',u'15',u'22',u'29'}
#GAME_10STEP_DIR_NAMES={u'11',u'18',u'25',u'01'}
GAME_10STEP_DIR_NAMES={'11',u'18',u'25',u'01'}
#GAME_10STEP_DIR_NAMES={'11',u'18'}
DIR_NAMES=GAME_5STEP_DIR_NAMES | GAME_10STEP_DIR_NAMES
BASE_DIR_PATH=ur'D:\!informatics\projects\python\Stab_recount'
#BASE_DIR_PATH=u'C:\\Users\\egrishkova\\ЭЭ\\Стабилограмма пересчет'
SRC_FNAME_BEF=u'Before_Soc_INFO.xlsx'
SRC_FNAME_AFT=u'After_Soc_INFO.xlsx'

def fpath_bef(dir_nam):
  return BASE_DIR_PATH+u'\\'+dir_nam+u'\\'+SRC_FNAME_BEF
def fpath_aft(dir_nam):
  return BASE_DIR_PATH+u'\\'+dir_nam+u'\\'+SRC_FNAME_AFT

for dir_nam in DIR_NAMES:
  for fpath in ( fpath_bef(dir_nam), fpath_aft(dir_nam) ):
    print u"current src fpath: "+fpath
    xl=pd.ExcelFile(fpath)
    for sheet_nam in [ unicode(i) for i in xl.sheet_names]:
      print u"current name: "+fpath[:-len(u'.xlsx')]+u' '+sheet_nam+u'.csv'
      if sheet_nam == u'Sheet':
        continue
      data = xl.parse(sheet_nam)
      data.to_csv(fpath[:-len(u'.xlsx')]+u' '+sheet_nam+u'.csv',encoding='cp1251')
