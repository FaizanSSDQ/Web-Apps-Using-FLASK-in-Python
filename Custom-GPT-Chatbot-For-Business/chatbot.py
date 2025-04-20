from transformers import AutoTokenizer , AutoModelForSeq2SeqLM

class Chatbot:
    def __init__ (self , model_name = "facebook/blenderbot-400M-distill" , ):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.conversation_history = []
    
    def get_response(self , user_input):
        history_string = '\n'.join(self.conversation_history)
        inputs = self.tokenizer.encode_plus(history_string , user_input , return_tensors='pt')
        outputs = self.model.generate(**inputs)
        response = self.tokenizer.decode(outputs[0] , skip_special_tokens = True).strip()
        self.conversation_history.append(user_input)
        self.conversation_history.append(response)
        return response
    
    def reset_conversation(self):
        conversation_history=[]




