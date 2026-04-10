
import json



def extract_topics(file_path):
    """
    Extract topics from topics_triggers.md file.
    Returns a dictionary with topic keys (marked by backticks) 
    and English values (following 'en:')
    """
    topics = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_topic = None
    
    for i, line in enumerate(lines):
        # Look for lines starting with * `topic_name`
        if line.strip().startswith('* `') and line.strip().endswith('`'):
            current_topic = line.strip()[3:-1]  # Extract text between * ` 
        
        # Look for English value following the topic
        elif current_topic:
            if line.strip().startswith('en:'):
               # Extract the English text after "en: "
               en_text = line.strip()[4:].strip()  # Remove "en: " prefix
               topics[current_topic] = en_text
               current_topic = None
            elif line.strip() and not line.strip().startswith('de:'):
               en_text = line.strip() 
               topics[current_topic] = en_text
               current_topic = None

    original_topics = json.dumps(topics, indent=4)
    with open("arg-microtexts/original_topics_2.json", "w", encoding="utf-8") as json_file:
        json_file.write(original_topics)

    
    

if __name__ == "__main__":
    extract_topics('arg-microtexts/topics_triggers_2.md')