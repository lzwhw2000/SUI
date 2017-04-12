# occur a fatal error 
Fatal Python error: Cannot recover from stack overflow.  

Thread 0x0000700005dab000 (most recent call first):
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/pymongo/periodic_executor.py", line 125 in _run
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/threading.py", line 864 in run
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/threading.py", line 916 in _bootstrap_inner
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/threading.py", line 884 in _bootstrap

Thread 0x00007000058a8000 (most recent call first):
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/pymongo/periodic_executor.py", line 125 in _run
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/threading.py", line 864 in run
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/threading.py", line 916 in _bootstrap_inner
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/threading.py", line 884 in _bootstrap

Current thread 0x00007fffe21033c0 (most recent call first):
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/_weakrefset.py", line 75 in __contains__
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/abc.py", line 182 in __instancecheck__
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/_collections_abc.py", line 839 in update
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/structures.py", line 46 in __init__
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/models.py", line 603 in __init__
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/adapters.py", line 250 in build_response
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/adapters.py", line 503 in send
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/sessions.py", line 609 in send
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/sessions.py", line 488 in request
  File "/Users/vance/.pyenv/versions/3.6.0/lib/python3.6/site-packages/requests/sessions.py", line 501 in get
  File "getUserInfo.py", line 46 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
  File "getUserInfo.py", line 63 in getInfo
