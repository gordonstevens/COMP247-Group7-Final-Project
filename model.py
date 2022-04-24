import joblib
import pandas as pd
import numpy as np

def predictor(X_test):
    loaded_model = joblib.load('model__group7.pkl')
    result = loaded_model.predict(X_test)
    print(result)
    return result

'''
predictor(pd.DataFrame(np.array([[250.000000,"MEN'S MONTEREY",'NO','THEFT UNDER','OTH',240,235,
    'Single Home, House (Attach Garage, Cottage, Mobile)',8,'South Riverdale']]),
    columns=['Cost_of_Bike', 'Bike_Model', 'Bike_Make', 'Primary_Offence', 'Bike_Colour', 'Report_DayOfYear', 
    'Occurrence_DayOfYear', 'Location_Type', 'Bike_Speed', 'NeighbourhoodName'])
)

predictor(pd.DataFrame(np.array([[1324.000000,'DEW PLUS','KO','THEFT UNDER','BLK',190,189,'Streets, Roads, Highways (Bicycle Path, Private Road)',24,
'Bay Street Corridor']]),
    columns=['Cost_of_Bike', 'Bike_Model', 'Bike_Make', 'Primary_Offence', 'Bike_Colour', 'Report_DayOfYear', 
    'Occurrence_DayOfYear', 'Location_Type', 'Bike_Speed', 'NeighbourhoodName'])
)
# 3452 	650.000000 	UNKNOWN 	AUSTIN 	THEFT OF EBIKE UNDER $5000 	BLUWHI 	65 	64 	Apartment (Rooming House, Condo) 	1 	Glenfield-Jane Heights
'''