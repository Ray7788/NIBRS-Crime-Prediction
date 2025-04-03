select *
from public.nibrs_incident inc --516549
left join  public.nibrs_arrestee arrest -- 516549
on inc.incident_id = arrest.incident_id 
and arrest.arrestee_seq_num = 1

left join public.nibrs_arrest_type arrest_type -- 516549
on arrest.arrest_type_id = arrest_type.arrest_type_id

left join public.nibrs_offense offense -- 572438
on inc.incident_id = offense.incident_id

left join public.nibrs_offense_type offense_type -- 572438
on offense.offense_code = offense_type.offense_code

left join public.nibrs_location_type loc_type -- 572438
on loc_type.location_id = offense.LOCATION_ID
