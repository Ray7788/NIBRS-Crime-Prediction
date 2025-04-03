# Mapping dictionary
# -----------------------------------------------------------------------------------
# --------------- nibrs data to create new offense_category_name --------------- 
# -----------------------------------------------------------------------------------
mapping = {
    'All Other Offenses': 'Other Offenses',
    'Animal Cruelty': 'Other Offenses',
    'Bad Checks': 'Fraud Offenses',
    'Counterfeiting/Forgery': 'Fraud Offenses',
    'Embezzlement': 'Fraud Offenses',
    'Extortion/Blackmail': 'Fraud Offenses',
    'Motor Vehicle Theft': 'Larceny/Theft Offenses',
    'Peeping Tom': 'Sex Offenses',
    'Sex Offenses, Non-forcible': 'Sex Offenses',
    'Driving Under the Influence': 'Liquor Law Violations',
    'Drunkenness': 'Liquor Law Violations',
    'Family Offenses, Nonviolent': 'Assault Offenses'
}

# Apply mapping; if not in dictionary, keep original value
nibrs['New_offense_category_name'] = nibrs['offense_category_name'].map(mapping).fillna(nibrs['offense_category_name'])

# -----------------------------------------------------------------------------------
# --------------- Chicago data to crime_against,offense_category_name ---------------
# -----------------------------------------------------------------------------------
crime_mapping = {
    'THEFT': ('Property', 'Larceny/Theft Offenses'),
    'BATTERY': ('Person', 'Assault Offenses'),
    'CRIMINAL DAMAGE': ('Property', 'Destruction/Damage/Vandalism of Property'),
    'ASSAULT': ('Person', 'Assault Offenses'),
    'MOTOR VEHICLE THEFT': ('Property', 'Larceny/Theft Offenses'),
    'DECEPTIVE PRACTICE': ('Property', 'Fraud Offenses'),
    'OTHER OFFENSE': ('Society', 'Other Offenses'),
    'ROBBERY': ('Property', 'Robbery'),
    'WEAPONS VIOLATION': ('Society', 'Weapon Law Violations'),
    'BURGLARY': ('Property', 'Burglary/Breaking & Entering'),
    'NARCOTICS': ('Society', 'Drug/Narcotic Offenses'),
    'CRIMINAL TRESPASS': ('Society', 'Trespass of Real Property'),
    'OFFENSE INVOLVING CHILDREN': ('Person', 'Other Offenses'),
    'CRIMINAL SEXUAL ASSAULT': ('Person', 'Sex Offenses'),
    'SEX OFFENSE': ('Person', 'Sex Offenses'),
    'PUBLIC PEACE VIOLATION': ('Society', 'Curfew/Loitering/Vagrancy Violations'),
    'HOMICIDE': ('Person', 'Homicide Offenses'),
    'INTERFERENCE WITH PUBLIC OFFICER': ('Society', 'Bribery'),
    'ARSON': ('Property', 'Arson'),
    'STALKING': ('Person', 'Other Offenses'),
    'PROSTITUTION': ('Society', 'Prostitution Offenses'),
    'LIQUOR LAW VIOLATION': ('Society', 'Liquor Law Violations'),
    'CONCEALED CARRY LICENSE VIOLATION': ('Society', 'Weapon Law Violations'),
    'INTIMIDATION': ('Person', 'Assault Offenses'),
    'KIDNAPPING': ('Person', 'Kidnapping/Abduction'),
    'OBSCENITY': ('Society', 'Pornography/Obscene Material'),
    'GAMBLING': ('Society', 'Gambling Offenses'),
    'HUMAN TRAFFICKING': ('Person', 'Human Trafficking'),
    'PUBLIC INDECENCY': ('Society', 'Disorderly Conduct'),
    'OTHER NARCOTIC VIOLATION': ('Society', 'Drug/Narcotic Offenses'),
    'NON-CRIMINAL': ('Not a Crime', 'Other Offenses')
}

# Apply mapping
data_filter[['crime_against', 'offense_category_name']] = data_filter['primary_type'].map(crime_mapping).apply(pd.Series)
