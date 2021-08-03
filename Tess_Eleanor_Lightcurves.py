# -*- coding: utf-8 -*-
"""MyCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BII6AUmPKD4tgw7HH_i9yR_BYy2OkC2I
"""

# Instala o módulo "eleanor", somente se necessário.

try:
  import eleanor
except:
  !pip install eleanor
  import eleanor

from IPython.display import Image
from tqdm import tqdm_notebook
import warnings
warnings.filterwarnings('ignore')

#import do eleanor  
import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import pandas as pd

# Monta o Google Drive no sistema de arquivos e diretório do Colab:
# 1. Execute esta célula de código
# 2. Clique no link que vai aparecer
# 3. Dê autrorização para o Colab acessar seu Google Drive
# 4. Copie o código de autroização e cole no campo abaixo.

from google.colab import drive
dir_drive = '/content/drive'    # diretório de montagem
drive.mount(dir_drive)

setor_file = dir_drive + "/MyDrive/" + "setor1.csv"    # arquivo no Google Drive.

df = pd.read_csv(setor_file, usecols=[0]) 
#df['tic_id'] = df.tic_id.str.replace('TIC ', '') <- Um dos csv's que testei anteriormente tinha a palavra TIC na lista
df

#for index, row in df.itertuples():
#  star = eleanor.Source(tic=row, sector=1)
#
#  print('Found TIC {0} (Gaia {1}), with TESS magnitude {2}, RA {3}, and Dec {4}'
#     .format(star.tic, star.gaia, star.tess_mag, star.coords[0], star.coords[1]))

#for index, row in df.itertuples():
#  star = eleanor.Source(tic=row, sector=1)
#  data = eleanor.TargetData(star, height=15, width=15, bkg_size=31, do_psf=False, do_pca=False, regressors='corner')
#  lk = data.to_lightkurve()
#  lk.plot()

for index, row in df.itertuples():
  star = eleanor.Source(tic=row, sector=1)
  data = eleanor.TargetData(star, height=15, width=15, bkg_size=31, do_psf=True, do_pca=True, regressors='corner')
  q = data.quality == 0
  t = data.time[q]
  yraw  = data.raw_flux[q]/np.nanmedian(data.raw_flux[q])
  ycorr = data.corr_flux[q]/np.nanmedian(data.raw_flux[q])
  ypca  = data.pca_flux[q]/np.nanmedian(data.raw_flux[q])
  ypsf  = data.psf_flux[q]/np.nanmedian(data.raw_flux[q])
  ymin = np.min( np.concatenate( (yraw, ycorr, ypca, ypsf) ) )
  ymax = np.max( np.concatenate( (yraw, ycorr, ypca, ypsf) ) )
  wid = 20
  hei = 5
  same_ylim = False
  plt.figure(figsize=(wid,hei))
  plt.plot(t, yraw, 'k', linewidth = 0.5)
  if (same_ylim):
    plt.ylim(ymin, ymax)
  plt.title(row)
  plt.xlabel("Time [BJD - 2457000]")
  plt.ylabel("Normalized Flux")
  plt.grid(True)
  plt.savefig(str(row) + '.png')
  plt.show()
  plt.close()

"""# Nova seção"""

#from google.colab import files

!zip -r content.zip /content

"""# Nova seção"""

