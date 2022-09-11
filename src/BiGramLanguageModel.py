def convertTextToWords():
    input = [
        'The day was grey and bitter cold, and the dogs would not take the scent. '
        'The big black bitch had taken one sniff at the bear tracks, backed off, '
        'and skulked back to the pack with her tail between her legs.']
    # converting the given sentence to lower case words. This helps treat The same as the
    lower_input = list(map(lambda x: x.lower(), input))
    dat = []
    for i in range(len(lower_input)):
        for word in lower_input[i].split():
            dat.append(word)
    print(dat)
    return dat


def bigramFunction(data):
    bigram_list = []
    bigram_counts = {}
    unigram_counts = {}
    for i in range(len(data) - 1):
        if i < len(data) - 1 and data[i + 1].islower():

            bigram_list.append((data[i], data[i + 1]))

            if (data[i], data[i + 1]) in bigram_counts:
                bigram_counts[(data[i], data[i + 1])] += 1
            else:
                bigram_counts[(data[i], data[i + 1])] = 1

        if data[i] in unigram_counts:
            unigram_counts[data[i]] += 1
        else:
            unigram_counts[data[i]] = 1
    return bigram_list, unigram_counts, bigram_counts


def calculate_bigram_probability(list_of_bigrams, unigram_counts, bigram_counts):
    list_of_prob = {}
    for bigram in list_of_bigrams:
        word1 = bigram[0]
        list_of_prob[bigram] = (bigram_counts.get(bigram)) / (unigram_counts.get(word1))
    return list_of_prob


if __name__ == '__main__':
    words = convertTextToWords()
    bigrams, number_of_unigrams, number_of_bigrams = bigramFunction(words)
    print('Bigrams:', bigrams)
    print('Bigrams and counts:', number_of_bigrams)
    print('Unigrams and counts:', number_of_unigrams)

    bigram_probability = calculate_bigram_probability(bigrams, number_of_unigrams, number_of_bigrams)
    print('Bigrams and probability', bigram_probability)
