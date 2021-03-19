import env

from utilities import generate_db_url, generate_df

_zillow_query = """
SELECT bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, taxamount, regionidcounty
	FROM properties_2017
		JOIN predictions_2017 USING(parcelid)
	WHERE (transactiondate LIKE \'2017-05-%%\' 
		OR transactiondate LIKE \'2017-08-%%\')
		AND propertylandusetypeid = 261
		AND calculatedfinishedsquarefeet IS NOT NULL
		AND bathroomcnt IS NOT NULL
		AND bedroomcnt IS NOT NULL
		AND regionidcounty IS NOT NULL
		AND taxvaluedollarcnt IS NOT NULL
		AND taxamount IS NOT NULL;
"""

def acquire_zillow():
    return generate_df("zillow.csv", _zillow_query, generate_db_url(env.user, env.password, env.host, "zillow"))