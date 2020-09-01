def predict_grade(text, custom_marks):
    import pandas as pd
    import nltk
    from nltk.corpus import stopwords
    import language_check
    from collections import Counter
    from nltk.corpus import wordnet as wn

    text = " ".join(filter(lambda x: x[0] != '@', text.split()))
    # To remove proper nouns tagged in the data-set which may result into
    # false positives during POS tagging.

    punctuation = ['.', '?', '!', ':', ';']
    # Comma count
    comma_count = text.count(',')

    # Punctuation count
    punctuation_count = 0
    for punct in punctuation:
        punctuation_count += text.count(punct)

    # Quotation marks count
    quotation_mark_count = text.count('"')
    quotation_mark_count += text.count("'")

    # Add the sentence count

    tokenized_essay = nltk.sent_tokenize(text)
    sent_count = len(tokenized_essay)

    # Add word count after removing the stop words.
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stop_words.update(
        ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])  # remove it if you need punctuation

    for word in words:
        if word in stop_words:
            words.remove(word)
    word_count = len(words)

    # Long word count
    long_word_count = 0
    total_word_length = 0
    for word in words:
        total_word_length += len(word)
        if len(word) > 6:
            long_word_count += 1

    # Average word length per essay
    avg_word_length_per_essay = round((total_word_length / float(len(words))), 2)

    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    spelling_mistakes = len(matches)

    # POS TAGS
    count = Counter([j for i, j in nltk.pos_tag(words)])

    noun_count = count['NN'] + count['NNS'] + count['NNPS'] + count['NNP']
    verb_count = count['VB'] + count['VBG'] + count['VBP'] + count['VBN'] + count['VBZ']
    adjective_count = count['JJ'] + count['JJR']
    adverb_count = count['RB'] + count['RBR'] + count['RBS']

    # No_of_domain_words and wrong words after removing the stop words and punctuations from the essay.
    cnt = 0
    wrong_word_count = 0
    for word in words:
        if wn.synsets(word):
            cnt += 1
        else:
            wrong_word_count += 1

    # Word to sentence ratio
    word_to_sent_ratio = round(float(word_count / float(sent_count)), 2)

    # Number of characters
    num_of_characters = nltk.FreqDist(text).N()

    to_predict = [word_count, long_word_count, avg_word_length_per_essay, wrong_word_count, cnt,
                  word_to_sent_ratio, num_of_characters, sent_count, noun_count, verb_count, comma_count,
                  punctuation_count,
                  adjective_count, adverb_count, quotation_mark_count, spelling_mistakes]

    # Load the model from the file
    import joblib
    lgb_from_joblib = joblib.load('./apigrade/CatBoost_Model.pkl')

    import numpy as np
    pred = np.array(to_predict).reshape(1, -1)

    # Use the loaded model to make predictions
    pred = lgb_from_joblib.predict(pred)

    pred_score = np.round(((pred / 12) * custom_marks), 2)

    print(pred)
    print(pred_score)

    return pred_score
