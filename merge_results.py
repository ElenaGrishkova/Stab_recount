# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from openpyxl import Workbook


GAME_5STEP_DIR_NAMES={'08','15','22','01'}
GAME_10STEP_DIR_NAMES={'11','18','25','29'}
DIR_NAMES=GAME_5STEP_DIR_NAMES | GAME_10STEP_DIR_NAMES
SHEET_NAMS=[u'Energy',u'Entropy',u'Hurst']
BASE_DIR_PATH='D:\!informatics\projects\python\Stab_recount'
SRC_FNAME_BEF='Before_Soc_EEH2.xlsx'
SRC_FNAME_AFT='After_Soc_EEH2.xlsx'
COL_CT_MAX=20
GAME_10STEP_REF_COLNAMS=['1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10',
                         '1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10']
GAME_5STEP_REF_COLNAMS=['1','1','2','2','3','3','4','4','5','5','1','1','2','2','3','3','4','4','5','5',
                        '1','1','2','2','3','3','4','4','5','5','1','1','2','2','3','3','4','4','5','5']

def fpath_bef(dir_nam):
  return BASE_DIR_PATH+'\\'+dir_nam+'\\'+SRC_FNAME_BEF
def fpath_aft(dir_nam):
  return BASE_DIR_PATH+'\\'+dir_nam+'\\'+SRC_FNAME_AFT

wb_bef_aft_list=[]
for dir in DIR_NAMES:
  wb_bef_aft_list.append((load_workbook(fpath_bef(dir), read_only=True),
                          load_workbook(fpath_aft(dir), read_only=True),
                          dir in GAME_10STEP_DIR_NAMES))

wb_merged = Workbook()
for nam in SHEET_NAMS:
  wb_merged.create_sheet(nam)

for nam in SHEET_NAMS:
  sheet_merged = wb_merged.get_sheet_by_name(nam)
  for wb_bef,wb_aft,game_10step in wb_bef_aft_list:
    sheet_bef = wb_bef.get_sheet_by_name(nam)
    sheet_aft = wb_aft.get_sheet_by_name(nam)
    humans={row[0] for row in sheet_bef.iter_rows(min_row=2)} | \
           {row[0] for row in sheet_aft.iter_rows(min_row=2)}
    humans=sorted(humans)
    col_n=0
    cols=[sheet_bef.columns()[0]]
    for ref_nam in GAME_10STEP_REF_COLNAMS if game_10step else GAME_5STEP_REF_COLNAMS:
      if ref_nam==col_nams[col_n]:
        col_n+=1
        cols.append(sheet_bef.columns()[col_n+1])
      else:
        cols.append(empty_col)




