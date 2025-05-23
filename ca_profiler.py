U
    �='h�  �                   @   sv  e d � ddlZe�� Zejdddd� ejddd	d� ejd
ddd� e�� Zeej�ej	ej
  ZZ	Z
ddlZddlmZ ddlmZ ddlZddlZddlmZ ddlmZ dd� Ze�e	�Zdd� ed D �ed< e�ed �Zejddd� edk�re�d�Z n@edk�r"e�d�Z n*edk�r8e�d�Z nedk�rLe�d �Z e �!e�ed!< ej"e
d"d#� e d$e
� dS )%a�  
      
                                                                                        
,--.      ,-----.  ,---.      ,------.                ,---.,--.,--.               
|  ,---. '  .--./ /  O  \     |  .--. ',--.--. ,---. /  .-'`--'|  | ,---. ,--.--. 
|  .-.  ||  |    |  .-.  |    |  '--' ||  .--'| .-. ||  `-,,--.|  || .-. :|  .--' 
|  | |  |'  '--'\|  | |  |    |  | --' |  |   ' '-' '|  .-'|  ||  |\   --.|  |    
`--' `--' `-----'`--' `--'    `--'     `--'    `---' `--'  `--'`--' `----'`--'    
         
University of Pisa - Department of Pharmacy - MMVSL https://www.mmvsl.it/wp/                                                                         
      
      �    Nz--ca_isoformz-ciz+Isoform related model. Options: 1, 2, 9, 12)�helpz--in_csvz-inz%Input csv. Must contain SMILES columnz	--out_csvz-outzHOutput csv. Predicitions will be saved in a column named Out_predictions)�Chem)�AllChem)�RandomForestClassifier)�SVCc                 C   sj   t �| |j�}| |  �d�}|jd }|�|df�}|| �d�}|jd }|�d|f�}||| |  S )N�   r   )�np�dot�T�sum�shapeZreshape)�X�YZxyZxx�mZyy�n� r   �
predict.py�tanimoto_kernel#   s    

r   c                 C   s"   g | ]}t jt�|�d dd��qS )�   i   )ZnBits)r   ZGetMorganFingerprintAsBitVectr   ZMolFromSmiles)�.0Zsmir   r   r   �
<listcomp>.   s     r   ZSMILES�fpT)�columnsZinplacer   z%models/Model_1CPU_CA1_SVM-Morgan.dumpr   z%models/Model_1CPU_CA2_SVM-Morgan.dump�	   z%models/Model_16CPU_CA9_RF-Morgan.dump�   z&models/Model_16CPU_CA12_RF-Morgan.dumpZOut_predictionsF)�indexzResults saved as )#�print�argparse�ArgumentParser�parser�add_argument�
parse_args�args�intZ
ca_isoformZin_csvZout_csvZisoformZpandas�pdZrdkitr   Z
rdkit.Chemr   Znumpyr   ZjoblibZsklearn.ensembler   Zsklearn.svmr   r   Zread_csvZdf�stackr   Zdrop�loadr   ZpredictZto_csvr   r   r   r   �<module>   s<   






