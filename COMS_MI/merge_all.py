#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 03:03:20 2017

@author: guitar79
"""

import sys
import os
from pathlib import Path
from PIL import Image

#drbase = '/media/guitar79/8T/RS_data/COMS_MI/le1b/'
drbase = '/run/user/1000/gvfs/smb-share:server=parksrne.local,share=rs_data/COMS_mi/le1b/'
drin = 'a/ir1/2016/'
dummy_im = Image.open(drbase+'a/dummy.png');

for i in sorted(os.listdir(drbase+drin)):
	if i[-4:] == '.png':
		my_file = Path(drbase+'a/all/2016/coms_mi_le1b_all_a_2016'+i[-12:])
		if my_file.is_file(): # image file already exists in my folder
			print ('File exists coms_mi_le1b_all_a_2016'+i[-12:])
		else:
			list_im = [drbase+'a/vis/2016/coms_mi_le1b_vis_a_2016'+i[-12:],\
				drbase+'a/swir/2016/coms_mi_le1b_swir_a_2016'+i[-12:],\
				drbase+'a/com/2016/coms_mi_le1b_com_a_2016'+i[-12:],\
				drbase+'a/ir1/2016/coms_mi_le1b_ir1_a_2016'+i[-12:],\
				drbase+'a/ir2/2016/coms_mi_le1b_ir2_a_2016'+i[-12:],\
				drbase+'a/wv/2016/coms_mi_le1b_wv_a_2016'+i[-12:]]
			new_im=Image.new('RGB', (4500,2600)) #creates a new empty image, RGB mode, and size 4500 by 2600
			print('starting 2016'+i[-12:])
			for k in range(0,3):
				for j in range(0,2):
					t=2*k+j;
					if(os.path.isfile(list_im[t])):
						im=Image.open(list_im[t])
						new_im.paste(im, (1500*k,1300*j))
					else:
						new_im.paste(dummy_im, (1500*k,1300*j));
			if not os.path.exists(drbase+'a/all/2016/'):
				os.makedirs('%sa/all/2016/' %(drbase))
			new_im.save(drbase+'a/all/2016/coms_mi_le1b_all_a_2016'+i[-12:])
			print('created coms_mi_le1b_all_a_2016'+i[-12:])
