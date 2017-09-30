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

#area = [cf, cn, a, k, lk]
area = "a"
#chl = [vis, ir1, ir2, swir, wv, com]
chl = "ir1"
#year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
yr = "2016"

#drbase = '/media/guitar79/8T/RS_data/COMS_MI/le1b/'
drbase = '/run/user/1000/gvfs/smb-share:server=parksrne.local,share=rs_data/COMS_mi/le1b/'

drin = '%s/%s/%s/' %(area, chl, yr)

dummy_im = Image.open(drbase+area+'/dummy.png');

for i in sorted(os.listdir(drbase+drin)):
	if i[-4:] == '.png':
		my_file = Path('%s%s/all/%s/coms_mi_le1b_all_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]))
		if my_file.is_file(): # image file already exists in my folder
			print ('File exists coms_mi_le1b_all_%s_%s%s' %(area, yr, i[-12:]))
		else:
			list_im = ['%s%s/vis/%s/coms_mi_le1b_vis_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]),\
				'%s%s/swir/%s/coms_mi_le1b_swir_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]),\
				'%s%s/com/%s/coms_mi_le1b_com_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]),\
				'%s%s/ir1/%s/coms_mi_le1b_ir1_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]),\
				'%s%s/ir2/%s/coms_mi_le1b_ir2_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]),\
				'%s%s/wv/%s/coms_mi_le1b_wv_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:])]

			new_im=Image.new('RGB', (4500,2600)) #creates a new empty image, RGB mode, and size 4500 by 2600
			print('starting %s%s' %(yr,i[-12:]))
			for k in range(0,3):
				for j in range(0,2):
					t=2*k+j;
					if(os.path.isfile(list_im[t])):
						im=Image.open(list_im[t])
						new_im.paste(im, (1500*k,1300*j))
					else:
						new_im.paste(dummy_im, (1500*k,1300*j));
			if not os.path.exists('%s%s/all/%s/' %(drbase, area, yr)):
				os.makedirs('%s%s/all/%s/' %(drbase, area,yr))
			new_im.save('%s%s/all/%s/coms_mi_le1b_all_%s_%s%s' %(drbase, area, yr, area, yr, i[-12:]))
			print('created coms_mi_le1b_all_%s_%s%s' %(area, yr, i[-12:]))
