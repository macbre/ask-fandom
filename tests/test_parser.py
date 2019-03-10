"""
Test cases for ask_fandom.oracle module
"""
from ask_fandom.parser import filter_parsed_question, NLPParser


def test_filter_parsed_question():
    """
    (S1 (SBARQ (WHADVP (WRB When)) (SQ (VBD was) (NP (NNP Jake) (NNP Simmonds)) (VP (VBN born))) (. ?))) Tree 1
    (SBARQ (WHADVP (WRB When)) (SQ (VBD was) (NP (NNP Jake) (NNP Simmonds)) (VP (VBN born))) (. ?)) Tree 3
    (WHADVP (WRB When)) Tree 1
    (WRB When) Tree 0
    (SQ (VBD was) (NP (NNP Jake) (NNP Simmonds)) (VP (VBN born))) Tree 3
    (VBD was) Tree 0
    (NP (NNP Jake) (NNP Simmonds)) Tree 2
    (NNP Jake) Tree 0
    (NNP Simmonds) Tree 0
    (VP (VBN born)) Tree 1
    (VBN born) Tree 0
    (. ?) Tree 0
    """
    assert list(filter_parsed_question(NLPParser.parse_question("Who played Jake Simmonds?"))) == [
        ('WP', 'Who'),
        ('VBD', 'played'),
        ('NP', 'Jake Simmonds'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("When was Jake Simmonds born?"))) == [
        ('WRB', 'When'),
        ('VBD', 'was'),
        ('NP', 'Jake Simmonds'),
        ('VBN', 'born'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Who directed The Big Bang episode?"))) == [
        ('WP', 'Who'),
        ('VBD', 'directed'),
        ('NP', 'The Big Bang episode'),
        ('NN', 'episode'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Who played in The End of Time episode?"))) == [
        ('WP', 'Who'),
        ('VBD', 'played'),
        ('IN', 'in'),
        ('NP', 'The End of Time episode'),
        ('NP', 'The End'),
        ('NN', 'End'),
        ('IN', 'of'),
        ('NP', 'Time episode'),
        ('NN', 'episode'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Which faction does the Alterac belong to?"))) == [
        ('WDT', 'Which'),
        ('NN', 'faction'),
        ('VBZ', 'does'),
        ('NP', 'the Alterac'),
        ('VB', 'belong'),
        ('TO', 'to'),
    ]


def test_filter_parsed_question_football():
    assert list(filter_parsed_question(NLPParser.parse_question("When was Manchester United founded?"))) == [
        ('WRB', 'When'),
        ('VBD', 'was'),
        ('NP', 'Manchester United'),
        ('VBN', 'founded'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Who is the coach of Manchester United?"))) == [
        ('WP', 'Who'),
        ('VBZ', 'is'),
        ('NP', 'the coach of Manchester United'),
        ('NP', 'the coach'),
        ('NN', 'coach'),
        ('IN', 'of'),
        ('NP', 'Manchester United'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Who plays as forward for Manchester United?"))) == [
        ('WP', 'Who'),
        ('VBZ', 'plays'),
        ('RB', 'as'),
        ('RB', 'forward'),
        ('IN', 'for'),
        ('NP', 'Manchester United')
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Who plays as midfielder for Manchester United?"))) == [
        ('WP', 'Who'),
        ('VBZ', 'plays'),
        ('RB', 'as'),
        ('JJ', 'midfielder'),
        ('IN', 'for'),
        ('NP', 'Manchester United')
    ]

    # different phrases of the same question
    assert list(filter_parsed_question(NLPParser.parse_question("Which club Cristiano Ronaldo plays for?"))) == [
        ('WDT', 'Which'),
        ('NN', 'club'),
        ('NP', 'Cristiano Ronaldo'),
        ('VBZ', 'plays'),
        ('IN', 'for'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Where is Cristiano Ronaldo playing now?"))) == [
        ('WRB', 'Where'),
        ('VBZ', 'is'),
        ('NP', 'Cristiano Ronaldo'),
        ('VBG', 'playing'),
        ('RB', 'now'),
    ]

    assert list(filter_parsed_question(NLPParser.parse_question("Where does Cristiano Ronaldo play?"))) == [
        ('WRB', 'Where'),
        ('VBZ', 'does'),
        ('NP', 'Cristiano Ronaldo'),
        ('VB', 'play'),
    ]