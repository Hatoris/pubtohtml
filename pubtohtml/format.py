from pymed import PubMed
from typing import *

query= "Roullin VG[Author]"

pubmed = PubMed(tool="UpdateArticles", email="florian.bernard@umontreal.ca")
results = pubmed.query(query, max_results=500)


class formatArticle:
    
    def __init__(self, article : Dict):
        self.article = article
     
    @property   
    def format_authors(self) -> str:
        results = ""
        for author in self.article.get("authors", []):
            results += f'{author.get("lastname", "")} '
            results += f'{author.get("initials", "")}, '
        return f'<a href="{self.url}" target="_blank"><b>{results[:-2]}</b></a>'

    @property
    def url(self)->str:
        return f"https://doi.org/{self.article.get('doi')}"

    @property        
    def title(self) -> str:
        return f'<i>{self.article.get("title", "")}</i>'
     
    @property   
    def journal(self):
        return self.article.get("journal", "")
   
    @property     
    def pub_date(self):
        return f'<b>{self.article.get("publication_date", ""):%Y}</b>'
      
    @property  
    def pmid(self):
        ID = self.article.get("pubmed_id").split("\n")[0]
        return f'PMID: {ID}'
        
    def __str__(self):
        return f'<li>{self.format_authors}. {self.title} {self.journal}. {self.pub_date}. {self.pmid} </li> '
 
with open("update_vg.html", "w") as f:
    f.write("<ul>")
    for r in results:
        article = r.toDict()
        fa = formatArticle(article)
        f.write(str(fa))
    f.write("</ul>")
    #print(format_article(article))
    #print(article.keys())
    #print(r.toDict()["authors"])
    #print(title(article))
    #print(format_authors(r.toDict()))
    #print(url(article))