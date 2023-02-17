import json

def data():
    data_path = 'annotated_user_da_with_span_full.json'
    save_path = 'data.json'
    with open(data_path, 'r') as f :
        dialogs = json.load(f)
    for id in dialogs:
        print(id)
        logs = dialogs[id]['log']
        for log in logs:
            del log['dialog_act']
            del log['span_info']
    with open(save_path, 'w') as sf:
        json.dump(dialogs, sf, indent=2, separators=(",", ": "), sort_keys=False)

if __name__ == "__main__":
    data()


