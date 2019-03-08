# ask-fandom
Your semantic data-based assistant aka _Tell me FANDOM, ..._

# Supported questions

* _When was `someone` born?_
* _Who directed the `episode`?_
* _Who played in `episode`?_
* _Did `foo` played in `bar` episode?_

# Examples

* _Which is the first episode with Jana Carpenter?_
* _Which species is Jana Carpenter?_
* _Who is the main actor in 456 ambassador?_
* _Was Jake Simmonds in the Doctor Who cast?_
* _Was 456 ambassador engaged in drug dealing?_
* _List me the Doctor Who guest actors_

# Supported "commands"
* _Tell me something about `foo`_
* _List me the `Season 2` stories_

```
>>> rrp.simple_parse("Was Jake Simmonds in the Doctor Who cast?")
'(S1 (SQ (VBD Was) (NP (NP (NNP Jake) (NNPS Simmonds)) (PP (IN in) (NP (DT the) (NN Doctor)))) (NP (WP Who) (NN cast)) (. ?)))'
>>> rrp.simple_parse("Tell me something about foo")
'(S1 (S (VP (VB Tell) (NP (PRP me)) (NP (NP (NN something)) (PP (IN about) (NP (NN foo)))))))'
```

# Command-line tool

```
$ python ask.py  "Who played Lionel Carson?"
Model directory: /home/macbre/.local/share/bllipparser/WSJ-PTB3
Model directory already exists, not reinstalling
INFO:get_oracle:Parsing question: Who played Lionel Carson?
INFO:get_oracle:Parsed question: [('WP', 'Who'), ('VBD', 'played'), ('NP', 'Lionel Carson')]
INFO:PersonFactOracle:You've asked: 'Who played Lionel Carson?' ({'name': 'Lionel Carson', 'property': 'played'})
INFO:PersonFactOracle:Asking SMW for 'Lionel Carson' page Actor property
INFO:PersonFactOracle:Got the value for Actor: ['Peter Bowles']
---
Who played Lionel Carson?
Lionel Carson is played by Peter Bowles.
```

# Data sources

## SemanticMediaWiki API

* Tell me something about `person name` - https://poznan.fandom.com/api.php?action=browsebysubject&subject=Karol_Libelt
* Give me a list of people born in `year` - https://poznan.fandom.com/api.php?action=ask&query=[[Born::1800]]|%3FBorn_in|sort%3DModification%20date|order%3Ddesc
* "Doctor Who" episodes - https://tardis.fandom.com/wiki/Property:Editor

# Tools

## Questions parsing libraries

* http://www.nltk.org/_modules/nltk/parse/bllip.html
* https://pypi.org/project/bllipparser/

## Text to speech and speech to text

* http://espeak.sourceforge.net/
* https://www.linuxlinks.com/speechtools/

# Inspirations

* [START, the world's first Web-based question answering system](http://start.csail.mit.edu/answer.php?query=What+South-American+country+has+the+largest+population%3F)

# Install

```
virtualenv env -ppython3
. env/bin/activate
pip install -r requirements.txt
```
