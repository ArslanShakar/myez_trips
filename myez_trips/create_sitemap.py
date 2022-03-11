file = open("sitemaps.xml", "w")
file.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for i in range(1, 26266):
    file.write("<sitemap>\n")
    file.write("<loc>https://myeztrips.com/sitemaps/sitemap_{}.txt</loc>".format(i))
    file.write("\n</sitemap>\n")

file.write("</sitemapindex>")
file.close()
