
# This File is just for testing the model. You can run this file directly by calling "python TestBot.py"
# in your terminal.

from transformers import AutoTokenizer , AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# Let's initialize a conversation history
conversation_history = []


while True:
    history_string = "\n".join(conversation_history)
    input_text = input(">>>:- ")
    inputs = tokenizer.encode_plus(history_string , input_text , return_tensors = "pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0] , skip_special_tokens=True).strip()
    print(response)
    conversation_history.append(input_text)
    conversation_history.append(response)
