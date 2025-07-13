openai.lib._old_api.APIRemovedInV1: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/ai-health-advisor/app.py", line 29, in <module>
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
File "/home/adminuser/venv/lib/python3.13/site-packages/openai/lib/_old_api.py", line 39, in __call__
    raise APIRemovedInV1(symbol=self._symbol
