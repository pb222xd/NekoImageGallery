#!/usr/bin/env python
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) == 3:
        metajson = json.loads(base64.b64decode(sys.argv[1]).decode('utf-8'))
        tagsList = metajson.get('tags', [])
        deviceTagsList = [tag for tag in base64.b64decode(sys.argv[2]).decode('utf-8').split('\n') if tag]
        combinedTags = []
        for tag in tagsList:
            for device in deviceTagsList:
                combinedTags.append(f"{tag}-{device}")
        output = ','.join(combinedTags)
        print(output)
