def get_stats(text_lines: str, msg_type: str):
    msgs = [msg for msg in text_lines if msg_type in msg]

    if not msgs:
        return [],{}

    if msg_type == "INFO":
        all_messages = [msg.split('"')[1].replace('"',"") for msg in msgs]
    elif msg_type == "ERROR":
        all_messages = [msg.split('ERROR -')[1].strip() for msg in msgs]
    else:
        raise "Msg type not allowed"

    unique_msgs = set(all_messages)
    msgs_count = {msg:all_messages.count(msg) for msg in unique_msgs}
    sorted_msgs = sorted(msgs_count, reverse=True)

    return sorted_msgs, msgs_count

def get_num_messages(text_lines: str): 

    info = [msg for msg in text_lines if "INFO" in msg]
    error = [msg for msg in text_lines if "ERROR" in msg]
    warn = [msg for msg in text_lines if "WARNING" in msg]

    return len(info), len(error), len(warn)


def parse_file(file_path: str):

    lines = open(file_path,'r').readlines()

    info_num, error_num, warn_num = get_num_messages(lines)

    sorted_msgs, messages_count = get_stats(lines,"INFO")

    sorted_error, error_count = get_stats(lines, "ERROR")

    top_ai_messages = "Top 3 AI Responses:\n"
    if not sorted_msgs:
        top_ai_messages = "No AI Responses found"

    else:
        for i in range(len(sorted_msgs)):

            msg = sorted_msgs[i]
            count = messages_count[msg]
            
            
            top_ai_messages += f'{i+1}. "{msg}" ({count} times)\n'

            if i == 2:
                break
        
    top_err_messages = "Most Common Errors:\n"
    if not sorted_error:
        top_err_messages = "No Errors are found"
    
    else:

        for i in range(len(sorted_error)):

            msg = sorted_error[i]
            count = error_count[msg]
            
            
            top_err_messages += f'{i+1}. {msg} ({count} times)\n'

            if i == 2:
                break 


    log_summary = f"""
Log Summary:
- INFO messages: {info_num}
- ERROR messages: {error_num}
- WARNING messages: {warn_num}
"""

    final_report = log_summary + "\n" + top_ai_messages + "\n" + top_err_messages

    return final_report


if __name__ == "__main__":

    print(parse_file("logs.txt"))