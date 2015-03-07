state_abbreviation=['AK ','AL ','AR ','AZ ','CA ','CO ','CT ','DC ','DE ','FL ','GA ','HI ','IA ','ID ','IL ','IN ','KS ','KY ','LA ','MA ','MD ','ME ','MI ','MN ','MO ','MS ','MT ','NC ','ND ','NE ','NH ','NJ ','NM ','NV ','NY ','OH ','OK ','OR ','PA ','RI ','SC ','SD ','TN ','TX ','UT ','VA ','VT ','WA ','WI ','WV ','WY ']
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District Of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
both=zip(state_abbreviation,states)

print "<select>"
for abb, full in both:
	print '<option value="{0}">{1}</option>'.format(abb,full)
print "</select>"
