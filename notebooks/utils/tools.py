import pandas as pd
import numpy as np

class PreprocessingData:
    
    def preprocessing_base(file):
        summary_plan = pd.read_excel(file, sheet_name = 0)
        ethnicity_plan = pd.read_excel(file, sheet_name = 2)
        gender_plan = pd.read_excel(file, sheet_name = 3)
        
        vars_out = [
            'T_ENV', 'RAZDEP', 'ANOSEST','T_ANALF15M', 'T_ANALF18M', 'T_ANALF25M', 
           'T_ATRASO_2_BASICO', 'T_ATRASO_2_FUND', 'T_FLBAS', 'T_FLFUND', 'T_FLMED',
           'T_FLSUPER', 'T_FREQ5A6', 'T_FREQ6A14', 'T_FREQ15A17', 'T_FREQ18A24',
           'T_FUND11A13', 'T_FUND15A17', 'T_FUND18M', 'T_FUND18A24', 'T_FUND25M',
           'T_MED18A20', 'T_MED25M', 'T_SUPER25M', 'R1040', 'R2040', 'RDPC1', 
           'RDPC2', 'RDPC3', 'RDPC4', 'RDPC5', 'RDPC10', 'RDPCT', 'RIND', 'RMPOB', 
           'RPOB', 'PRENTRAB', 'PIND', 'PMPOB', 'PPOB', 'GINI', 'THEIL',
           'I_ESCOLARIDADE', 'I_FREQ_PROP', 'IDHM_E', 'IDHM_L', 'IDHM_R','IDHM',
           ]
        
        vars_ethnicity_plan = ethnicity_plan.drop(vars_out, axis = 1)
        vars_gender_plan = gender_plan.drop(vars_out, axis = 1)
        vars_gender_plan = vars_gender_plan.drop(['IDHM_R_ajustado', 'IDHM_ajustado'], axis = 1)
        
        return summary_plan, vars_ethnicity_plan, vars_gender_plan