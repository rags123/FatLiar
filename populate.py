import os

def populate():
	add_title(title="Some text about Burger",
		content=""" A hamburger (also called a beef burger, hamburger sandwich, burger or hamburg) is a sandwich consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bun. 
		Hamburgers are often served with lettuce, bacon, tomato, onion, pickles, cheese and condiments such as mustard, mayonnaise, ketchup, relish, and green chile.
        The term "burger" can also be applied to the meat patty on its own, especially in the UK where the term "patty" is rarely used. 
        The term may be prefixed with the type of meat used, as in "turkey burger". """)

	add_title(title="Some text about Pizza",
		content=""" Pizza is an oven-baked flat bread generally topped with tomato sauce and cheese. 
		It is commonly supplemented with a selection of meats, vegetables and condiments. 
		The term first appeared in 997 AD, "in a Latin text from the southern Italian town of Gaeta", in Lazio, Central Italy. 
		The modern pizza was invented in Naples, Italy, and the dish and its variants have since become popular in many areas of the world. """)

	add_title(title="Some text about Angelina",
		content=""" Angelina Jolie (born Angelina Jolie Voight; June 4, 1975) is an American actress, filmmaker, and humanitarian. She has won an Academy Award, two Screen Actors Guild Awards, and three Golden Globe Awards, and has been cited as Hollywood's highest-paid actress. 
		Jolie made her screen debut as a child alongside her father, Jon Voight, in Lookin' to Get Out (1982). 
		Her film career began in earnest a decade later with the low-budget production Cyborg 2 (1993), followed by her first leading role in a major film, Hackers (1995). 
		She starred in the critically acclaimed biographical television films George Wallace (1997) and Gia (1998), and won an Academy Award for Best Supporting Actress for her performance in the drama Girl, Interrupted (1999). """)

	add_title(title="Some text about Germany",
		content=""" Germany (German: Deutschland), officially the Federal Republic of Germany (German: Bundesrepublik Deutschland, pronounced, is a federal parliamentary republic in western-central Europe. 
		It consists of 16 constituent states, which retain limited sovereignty, and covers an area of 357,021 square kilometres (137,847 sq mi) with a largely temperate seasonal climate. 
		Its capital and largest city is Berlin. Germany is a major economic and political power and traditionally a leader in many cultural, theoretical and technical fields. """)

	add_title(title="Some text about Apple Inc.",
		content=""" Apple Inc. is an American multinational corporation headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, online services, and personal computers. 
		Its best-known hardware products are the Mac line of computers, the iPod media player, the iPhone smartphone, and the iPad tablet computer. Its online services include iCloud, iTunes Store, and App Store. 
		Apple's consumer software includes the OS X and iOS operating systems, the iTunes media browser, the Safari web browser, and the iLife and iWork creativity and productivity suites. """)

	for t in Blog.objects.all():
		print str(t)




def add_title(title, content):
	t = Blog.objects.get_or_create(title=title, content=content, views=0, likes=0)[0]
	return t

if __name__ == '__main__':
    print "Starting Rose population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'version_one.settings')
    from site_one.models import Blog
    populate()