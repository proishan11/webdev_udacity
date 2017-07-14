import webapp2

form="""
<form method="post">
	What is your birthday?
	<label>
		Month
		<input type="text" name="month">
	</label>
	<label>
		Day
	<input type="text" name="day">
	</label>
	<label>
		Year
	<input type="text" name="year">
	</label>
	<br>
	<br>
	<input type="submit">
</form> 
"""

months = ["January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December",]

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

def valid_day(day):
	day = day.strip()
	if day and day.isdigit():
		day = int(day)
		if day>0 and day<=31:
			return day
def valid_year(year):
	year = year.strip()
	if year and year.isdigit():
		year = int(year)
		if year>1900 and year<2020:
			return year

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)                                 #get request contains parameters as the names in form e.g. 'month'

    def post(self):
    	user_month = valid_month(self.request.get('month'))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year'))
    	if not (user_month and user_day and user_year):
    		self.response.out.write(form)                              #if invalid month,day or year show form again
    	else:
    		self.response.out.write("Thanks! that's a totally valid day!")    

application = webapp2.WSGIApplication([('/', MainPage),],debug=True)
									    
									  
