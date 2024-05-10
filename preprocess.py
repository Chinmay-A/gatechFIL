import os
import time

def get_data(path):

    import google.generativeai as genai

    bard_api_key='AIzaSyDA_f4kl8MADRVyOLA9BqRgkXVjR8vL5Tc'
    
    genai.configure(api_key=bard_api_key)
    model=genai.GenerativeModel('gemini-pro')
    
    # chat=model.start_chat(history=[])
    
    file_path='./sec-edgar-filings/AAPL/10-K/0000320193-17-000070/full-submission.txt'

    uploaded_file=genai.upload_file(path=file_path,display_name='file_a')
    file=genai.get_file(name=uploaded_file.name)

    print(uploaded_file.uri)

    response=model.generate_content(['get relevant financial numbers in a jso format strictly',uploaded_file])
    # with open(file_path,'r') as f:
    #     text=f.read()

    # chat.send_message('I am going to input a SEC 10K filling for a company as split over 10 messages, reply with OK to the next 10 messages including this one, but remeber all input, after i instruct you return relevant financial numbers in a json format')
    # time.sleep(2)
    # n_characters=int(len(text)/9)

    # print(n_characters)

    # for i in range(9):
    #     chat.send_message(text[n_characters*i:n_characters*(i+1)-1])
    #     print('message sent')                  

    # reply=chat.send_message('filling over now return the relevant financial numbers in a json format')

    print(response.text)

    return response.text

get_data('TSLA')