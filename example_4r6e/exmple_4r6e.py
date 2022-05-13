import os
from datetime import datetime

os.chdir('/home/fuli/my_project/reinforce-master/test_set/ign_data/PDB2020_ext')
cmdline = "export PATH=$PATH:/home/fuli/.local/UCSF-Chimera64-1.16/bin"
cmdline += "\n echo path"
cmdline += "\n cd ~ \n cd /home/fuli/my_project/reinforce-master/test_set/ign_data/PDB2020_ext"
cmdline += "\n source activate \n conda deactivate \n conda activate pychimera"
star = datetime.now()
cmdline += '\n chimera --nogui --script "dockprep.py pdb2020_ext_PDB/%s_protein.pdb' \
               ' pdb2020_prep/%s.pdb &&"' % (name, name)
err = os.system(cmdline)
end = datetime.now()
print('time:', (end - star).seconds)
print('ID:', a)
print('error code: ', err)


