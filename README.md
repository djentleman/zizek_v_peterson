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
Zizek: The paradox to be happy there not a crucial misunderstanding here. What if secretly they know she would kill her child again. And is not the standard, but the true unconstrained consumption in all these creeps here?

				Peterson: Otherwise, the creative types would sit around and see them again. I guess I would say that things can turn to stone, and they know that there’s such a degree that it was mastered completely. It’s a low resolution representations of what happens when you know what's going on all dimensions—there’s just as we were coming here.

Zizek: I think we should always be aware of how things really stand; they know she would kill her child again. It’s incredible how you feel’ … if you take away from human life things which may appear is going on here.

				Peterson: It’s identity politics, she would have to become conscious of are precisely the things I know I’m going to be able to transcend the rule structure, right? I think that’s going to talk about things that Jaak Panksepp discovered, for example, would think about it as delivering a lecture to an end.

Zizek: There we still talk about politics, I feel a kind of false activity: you think it’s my duty, for this permission. What does he know or at least that’s what I admire nonetheless in his essay significantly titled, “Kosovo and the key to order is that once you are doing where Derrida is concerned, I think it’s about.

				Peterson: I think it’s up to me that that’s right. I think it’s up to me that that’s profoundly correct. But I think that’s a special circuitry, and it’s no wonder.

Zizek: I think they are right.

				Peterson: Think about it as a marker. Think about this in their choices.

Zizek: So I think for the subject?

				Peterson: Think about this in their own worldview. You can think of it for both of them. I think it is.
```

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
