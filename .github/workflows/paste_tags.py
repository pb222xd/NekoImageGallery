#!/usr/bin/env python
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) == 2:
        metajson = json.loads(sys.argv[1])
        tagsList = metajson.get('tags', [])
        deviceTagsList = sys.argv[2].split('\n')
        combinedTags = []
        for tag in tagsList:
            for device in deviceTagsList:
                combinedTags.append(f"{tag}-{device}")
        for tag in combinedTags:
            print(tag, end=',')
