# WhoBeSpeaking

See some cool statistics on who is the chattiest in your Telegram chat.

You can see who is sending the most messages, when are people most active, the breakdown on types of messages and more!

Dependencies required:
- Python 3.4+
- Matplotlib
- Numpy

Steps:
1. Open Telegram Desktop, and navigate to "Settings" and "Advanced" and "Export Telegram Data"
2. Select whichever group chats you want to view
3. Unmark all media options, sticker analysis is not yet an implemented feature
4. Select "Machine-readable JSON" under Location and format
5. Export
6. Move "result.json" into the directory with the code
7. run the command
```python
python json_parse.py
```
8. Profit!

