import env

from utilities import generate_db_url, generate_df

_zillow_query = """
SELECT *
	FROM unique_properties
		JOIN properties_2017 USING(parcelid)
		JOIN predictions_2017 USING(parcelid)
        JOIN propertylandusetype USING(propertylandusetypeid) # 21937 rows
--		JOIN airconditioningtype USING(airconditioningtypeid) # 7088 rows
-- 		JOIN architecturalstyletype USING(architecturalstyletypeid) # 49 rows
-- 		JOIN heatingorsystemtype USING(heatingorsystemtypeid) # 13888 rows
-- 		JOIN typeconstructiontype USING(typeconstructiontypeid) # 51 rows
-- 		JOIN storytype USING(storytypeid) # 12 rows
	WHERE transactiondate LIKE \'2017-05-%%\' 
		OR transactiondate LIKE \'2017-06-%%\';
"""

def acquire_zillow():
    return generate_df("zillow.csv", _zillow_query, generate_db_url(env.user, env.password, env.host, "zillow"))