#!/bin/bash

# category search
python search.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="seattle" --term="hipster"
python search.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="seattle" --term="family"
python search.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="seattle" --term="gay"

# hotel search
python search_hotels.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="seattle" --term="hotels"
python search_hotels.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="downtown, seattle" --term="hotels"
python search_hotels.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="fremont, seattle" --term="hotels"
python search_hotels.py --consumer_key="KthO8dNdeYTgBFnBlIIdHA" --consumer_secret="Tm8COLLLfk2U5_YQmBEpSZtN6p4" --token="wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" --token_secret="IXMeyVMwlKawX9yNJxCBXS-Zo4Y" --location="ballard, seattle" --term="hotels"

find api | grep "api/" | awk '{ print "<script src=\""$1"\" type=\"text/javascript\"></script>" }' > tmp.scripts
python replace_autogen_index.py

rm tmp.scripts
