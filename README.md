# Zizek Vs Peterson

Did you ever want Slavoj Zizek and Jordan Peterson to debate on your computer?

Well now they can!


Markov Chain Based Zizek v Peterson debate simulator

Slavoj Zizek Data Sources:
 - http://opentranscripts.org/transcript/disposable-life-slavoj-zizek/
 - https://zizek.uk/zizeks-lecture-transcripts/
 - https://zizek.uk/zizek-transcriptsubtitles/
 - http://www2.idehist.uu.se/distans/ilmh/pm/zizek01.htm


Jordan Peterson Data Sources:
 - https://www.jordanbpeterson.com/category/transcripts/
 - https://www.jordanbpeterson.com/philosophy/postmodernism-definition-and-critique-with-a-few-comments-on-its-relationship-with-marxism/


## Installation:

After cloning this repository:

```
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

## Running:

```
python debate.py
```

## Example Output

```
Zizek: I can give them, but then you don’t agree with him in this sense Anakin restores the balance.

				Peterson: Left-leaning people don’t know how to deal with them, so the sense of meaning is.

Zizek: The Serb and the same time, Neo addresses people still caught in this sense that I don’t know if you can translate Lacan into clear terms.

				Peterson: We don’t know what the sense of meaning and engagement. Left-leaning people don’t know what that is, is radical skepticism. We don’t know how to deal with them, so the sense of meaning and engagement.

Zizek: The first problem I have to seduce people with obscure statements, but I don’t know if you don’t need philosophy. You don’t know how much. You don’t know how much.

				Peterson: Left-leaning people don’t know what the avenue is. Left-leaning people don’t know how an individual might be dangerous.

Zizek: I don’t know what I mean.

				Peterson: I don’t know what transformations that might mean. So I don’t know what that means.

Zizek: I don’t know what I love.

				Peterson: So I don’t know how to do it slowly. We don’t know what that means. We don’t know how to deal with it.
```

If i had more time/motivation i'd probably swap out the intersection based similaroty algorithm with a Word2vec embedding/cosine similarity
based system. But alas, im lazy.
