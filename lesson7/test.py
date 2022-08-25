import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

death_by_year = wiki_wiki.page('Lists_of_deaths_by_year')
# wiki_wiki.page('Deaths_in_February_2022')
# wiki_wiki.page('2022#Deaths')

months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#print(death_by_year.exists())

#print(death_by_year.sections)

#print(death_by_year.summary)

sections=death_by_year.sections

def print_year(sections, level=0):
    years=[section.title for section in sections]
    years=years[:-1]
    secs=[]
    for year in years:
        #if int(year) >= 1990 and int(year) != 2022:
        if int(year) == 1991:
            #url01=wiki_wiki.page(f'{year}#Deaths')
            #print(url01.sections)
            #print(f'{year}#Deaths')

            for month in months:
                url02=wiki_wiki.page(f'Deaths_in_{month}_{year}')
                #print(f'Deaths_in_{month}_{year}')
                #print(url02.sections)
                for s in url02.sections:
                    #print("%s: %s - %s" % ("*" * (level+1), s.title, s.text[0:40]))
                    secs.append(s)
                    print(secs)
                    for sub in secs:
                        print("%s: %s - %s" % ("*" * (level+1), sub.title, sub.text[0:40]))

                    
                



print_year(sections)

dictionary={"Sergio Corbucci":["1 December 1990", 63], "Sergio Corbucci":["1 December 1990", 63]}