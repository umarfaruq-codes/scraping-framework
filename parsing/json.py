def validate_record(record: dict, fields: dict):

    if isinstance(record, dict) and fields is not None:
        if fields.keys() <= record.keys():
            count=0
            for key in fields:  # noqa: PLC0206
                if isinstance(record[key], fields[key]):
                    count+=1
            if count==len(fields):
                return True        
        else:
            return False
    return False    