import json
import xmltodict
import os


original_data_dir = 'arg-microtexts/corpus/en'
original_data_json = 'arg-microtexts'


    
def convert_xml_to_json():   

    sample_texts = {}
    data_dict = []

    # First pass: collect all text files
    for file in os.listdir(original_data_dir):
        if file.endswith('.txt'):
            with open(os.path.join(original_data_dir, file), 'r', encoding='utf-8') as f:
                sample_texts[file[:-4]] = f.read()
                # print(sample_texts)
    # Second pass: process XML files and merge with text
    for file in os.listdir(original_data_dir):
        if file.endswith('.xml'):
            with open(os.path.join(original_data_dir, file), 'r', encoding='utf-8') as f:
                data_dict.append(xmltodict.parse(f.read()))
            
            # Add @text from sample_texts if @id matches
            file_id = file[:-4]
            if file_id in sample_texts:
                data_dict[-1]["@text"] = sample_texts[file_id]
                

    json_data = json.dumps(data_dict, indent=4)
    text_data = json.dumps(sample_texts, indent=4)
    with open(os.path.join(original_data_json, "original_data.json"), "w", encoding="utf-8") as json_file:
        json_file.write(json_data)

    
    with open(os.path.join(original_data_json, "text_data.json"), "w", encoding="utf-8") as text_file:
        text_file.write(text_data)


if __name__=="__main__":
    convert_xml_to_json(), 