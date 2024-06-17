from deep_translator import GoogleTranslator

def translate_and_copy_file_content(input_file, output_file, char_limit=4000):
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Take only the first 4000 characters
    content_to_translate = content[:char_limit]

    try:
        # Translate content to Hindi
        translated_text = GoogleTranslator(source='auto', target='hi').translate(content_to_translate)
        
        # Write translated content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
            
        print(f"Content copied from {input_file} and translated to Hindi in {output_file}")

    except Exception as e:
        print(f"An error occurred during translation: {e}")

if __name__ == "__main__":
    # Define file paths
    input_file = r'C:\Users\nikhilchahar\Desktop\NLP CLASS\assignment_4_data.txt'
    output_file = r'C:\Users\nikhilchahar\Desktop\NLP CLASS\assignment_4_hindi.txt'
    
    # Translate content from input file and write to output file
    translate_and_copy_file_content(input_file, output_file)
from deep_translator import GoogleTranslator

def translate_and_copy_file_content(input_file, output_file, char_limit=4000):
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Take only the first 4000 characters
    content_to_translate = content[:char_limit]

    try:
        # Translate content to Hindi
        translated_text = GoogleTranslator(source='auto', target='hi').translate(content_to_translate)
        
        # Write translated content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
            
        print(f"Content copied from {input_file} and translated to Hindi in {output_file}")

    except Exception as e:
        print(f"An error occurred during translation: {e}")

if __name__ == "__main__":
    # Define file paths
    input_file = r'C:\Users\nikhilchahar\Desktop\NLP CLASS\assignment_5_data.txt'
    output_file = r'C:\Users\nikhilchahar\Desktop\NLP CLASS\assignment_5_data_hindi.txt'
    
    # Translate content from input file and write to output file
    translate_and_copy_file_content(input_file, output_file)
