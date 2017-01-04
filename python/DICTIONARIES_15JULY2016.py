IT_SALARY = { 'trainee' : 10000 , 'developer' : 20300 , 'designer' : 300000 }
EXPENDITURE = { 'trainee' : 9000 , 'developer' : 8000 , 'designer' : 10000}
for pos in EXPENDITURE:
	REM_SALARY = (IT_SALARY[pos] - EXPENDITURE[pos])
	print "Remaning salary is %d"%(REM_SALARY)
