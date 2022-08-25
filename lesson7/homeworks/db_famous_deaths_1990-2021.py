# Scrape famous people deaths between 1990 to 2021 from Wikipedia in a json
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

# Get wiki page by year
death_by_year = wiki_wiki.page('Lists_of_deaths_by_year')

months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Take years from wiki sections
sections=death_by_year.sections

# Foo for scraping deaths with years and months
def scrape_deaths(sections):
    years=[section.title for section in sections]
    years=years[:-1]

    for year in years:
        if int(year) >= 1990 and int(year) != 2022:
            url01=wiki_wiki.page(f'{year}#Deaths')
            print(url01.sections)
            #print(f'{year}#Deaths')

            for month in months:
                #url02=wiki_wiki.page(f'Deaths_in_{month}_{year}')
                print(f'Deaths_in_{month}_{year}')


scrape_deaths(sections)

## TODO ##
# Put in a json??
# Adding Death Ages