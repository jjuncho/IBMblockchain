import json

#Script to parse out necessary data from exported slack json data

def get_threads_and_replies():
	with open('slack-2019.json') as json_file:
	    data = json.load(json_file)
	    output_dict = [{"text": x['text'], "thread_ts": x['thread_ts']}for x in data if x.get('thread_ts') ] #currently has all messages with
	    #output = "["
	    # for x in output_dict:
	    # 	output =output + "{" + "'thread_ts':" + x['thread_ts'] + ",'text': " + x['text']
	    # 	output +="},"
	    # output=output[:-1]
	    # output+="]"

	    output_json = json.dumps(output_dict)
	    print(output_json)

def get_questions():
	with open('slack-2019.json') as json_file:
	    data = json.load(json_file)
	    output_dict = [ x['text'] for x in data if "?" in x["text"]]
	    print(output_dict)

if __name__ == "__main__":

	get_questions()

        