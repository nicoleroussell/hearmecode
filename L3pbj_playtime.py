Python 2.7.8 (default, Jun 30 2014, 16:08:48) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> bread = 10
>>> pb=10
>>> jelly=4
>>> sandwich=1
>>> while bread >= 2 and pb>=1 and jelly>=1:
	print "I'm making sandwich #{0}.".format(sandwich)
	bread = bread -2
	pb = pb-1
	jelly = jelly-1
	sandwich = sandwich+1

	
I'm making sandwich #1.
I'm making sandwich #2.
I'm making sandwich #3.
I'm making sandwich #4.
>>> bread=10
>>> pb=10
>>> jelly=4
>>> sandwich=1
>>> while bread >=2 and pb>=1 and jelly >=1:
	print "i'm making sandwich #{0}.format(sandwich)
	
SyntaxError: EOL while scanning string literal
>>> while bread >=2 and pb>=1 and jelly >=1:
	print "i'm making sandwich #{0}.".format(sandwich)
		sandwiches-worthofbread=bread/2
		
  File "<pyshell#18>", line 3
    sandwiches-worthofbread=bread/2
    ^
IndentationError: unexpected indent
>>> while bread >=2 and pb>=1 and jelly >=1:
	print "i'm making sandwich #{0}.".format(sandwich)
	sandwichesworthofbread=bread/2
	print "i have sandwiches-worthofbread=bread/2
	
SyntaxError: EOL while scanning string literal
>>> 
>>> bread=10
>>> pb=10
>>> jelly=4
>>> sandwich=1
>>> sammworthofbread = bread / 2
>>> while bread >=2 and pb>=1 and jelly >=1:
	print "i'm making sandwich #{0}.".format(sandwich)
	print "i have {0} sandwiches worth of bread left, {1} sandwiches worth of jelly left, and {2} sandwiches worth of pb left.".format(sammworthofbread, jelly, pb)
	bread=bread-2
	pb=pb-1
	jelly=jelly-1
	sandwich=sandwich+1
	sammworthofbread=bread / 2

	
i'm making sandwich #1.
i have 5 sandwiches worth of bread left, 4 sandwiches worth of jelly left, and 10 sandwiches worth of pb left.
i'm making sandwich #2.
i have 4 sandwiches worth of bread left, 3 sandwiches worth of jelly left, and 9 sandwiches worth of pb left.
i'm making sandwich #3.
i have 3 sandwiches worth of bread left, 2 sandwiches worth of jelly left, and 8 sandwiches worth of pb left.
i'm making sandwich #4.
i have 2 sandwiches worth of bread left, 1 sandwiches worth of jelly left, and 7 sandwiches worth of pb left.
>>> bread=10
>>> pb=10
>>> jelly=4
>>> sandwich=1
>>> sammworthofbread=bread/2
>>> 
