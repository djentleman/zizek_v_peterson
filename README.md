# Zizek Vs Peterson

Did you ever want Slavoj Zizek and Jordan Peterson to debate on your computer?

Well now they can!


Markov Chain Based Zizek v Peterson debate simulator

Slavoj Zizek Data Sources:
http://opentranscripts.org/transcript/disposable-life-slavoj-zizek/
https://zizek.uk/zizeks-lecture-transcripts/
https://zizek.uk/zizek-transcriptsubtitles/
http://www2.idehist.uu.se/distans/ilmh/pm/zizek01.htm


Jordan Peterson Data Sources:
https://www.jordanbpeterson.com/category/transcripts/
https://www.jordanbpeterson.com/philosophy/postmodernism-definition-and-critique-with-a-few-comments-on-its-relationship-with-marxism/


Installation:

```
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

Running:

```
python debate.py
```



If i had more time/motivation i'd probably swap out the intersection based similaroty algorithm with a Word2vec embedding/cosine similarity
based system. But alas, im lazy.
