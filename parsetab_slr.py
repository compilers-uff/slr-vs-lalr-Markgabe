
# parsetab_slr.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'EQUALS ID TIMES\n    S : L EQUALS R\n    \n    S : R\n    \n    L : TIMES R\n    \n    L : ID\n    \n    R : L\n    '
    
_lr_action_items = {'TIMES':([0,4,6,],[4,4,4,]),'ID':([0,4,6,],[5,5,5,]),'$end':([1,2,3,5,7,8,9,],[0,-5,-2,-4,-3,-5,-1,]),'EQUALS':([2,5,7,8,],[6,-4,-3,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'L':([0,4,6,],[2,8,8,]),'R':([0,4,6,],[3,7,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> L EQUALS R','S',3,'p_stmt_L_EQ_R','slrvslalr.py',23),
  ('S -> R','S',1,'p_stmt_R','slrvslalr.py',29),
  ('L -> TIMES R','L',2,'p_L_TIMES_R','slrvslalr.py',35),
  ('L -> ID','L',1,'p_L_ID','slrvslalr.py',41),
  ('R -> L','R',1,'p_R_L','slrvslalr.py',47),
]