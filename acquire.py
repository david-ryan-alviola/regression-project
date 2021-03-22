import env

from utilities import generate_db_url, generate_df

_zillow_query = """
SELECT bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, taxamount, fips
	FROM properties_2017
		JOIN predictions_2017 USING(parcelid)
	WHERE (transactiondate BETWEEN '2017-05-01' AND '2017-08-31')
		AND (unitcnt = 1 OR propertylandusetypeid IN (261, 279, 262, 263, 264, 266, 275))
		AND calculatedfinishedsquarefeet IS NOT NULL
		AND bathroomcnt IS NOT NULL
		AND bedroomcnt IS NOT NULL
		AND fips IS NOT NULL
		AND taxvaluedollarcnt IS NOT NULL
		AND taxamount IS NOT NULL;
"""

def acquire_zillow():
    return generate_df("zillow.csv", _zillow_query, generate_db_url(env.user, env.password, env.host, "zillow"))