from deep_translator import GoogleTranslator
from nltk.translate.bleu_score import sentence_bleu
import nltk

# Ensure NLTK resources are downloaded
nltk.download('punkt')

def translate_content(content, char_limit=4000):
    # Take only the first 4000 characters
    content_to_translate = content[:char_limit]

    try:
        # Translate content to Hindi
        translated_text = GoogleTranslator(source='auto', target='hi').translate(content_to_translate)
        return translated_text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return None

def evaluate_translation(translated_text, reference_text):
    # Tokenize the sentences
    translated_sentences = nltk.sent_tokenize(translated_text)
    reference_sentences = nltk.sent_tokenize(reference_text)

    # Tokenize the words
    translated_tokens = [nltk.word_tokenize(sent) for sent in translated_sentences]
    reference_tokens = [[nltk.word_tokenize(sent)] for sent in reference_sentences]

    # Calculate BLEU score
    scores = []
    for trans, ref in zip(translated_tokens, reference_tokens):
        score = sentence_bleu(ref, trans)
        scores.append(score)

    average_bleu_score = sum(scores) / len(scores)
    return average_bleu_score

if __name__ == "__main__":
    # Define file paths
    input_file = r'C:\Users\nikhilchahar\Desktop\NLP CLASS\assignment_5_data.txt'
    reference_file = r"C:\Users\nikhilchahar\Desktop\NLP CLASS\assignment_5_data_hindi.txt"
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate content
    translated_text = translate_content(content)
    
    if translated_text:
        # Read reference file
        with open(reference_file, 'r', encoding='utf-8') as f:
            reference_text = f.read()
        
        # Evaluate translation
        bleu_score = evaluate_translation(translated_text, reference_text)
        print(f"Average BLEU score for the translated content: {bleu_score}")
    else:
        print("Translation failed, skipping evaluation.")
