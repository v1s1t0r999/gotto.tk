## What?
A simple and easy link shortner which completely "self-hosted" and is [open sourced](http://gotto.tk/source)!!

---

## How?
Send a `GET` request to `https://v1s1t0r999.herokuapp.com/make` with parameters:
  - `src` = Link to be Shortened.
  - `name` = The name you want for it.
  - **Example in Python:**
  ```py
  import requests
  site = "https://blog.somesite.com/imacool/how-to-be-cool"
  name = "my-cool-blog"
  resp = requests.get(f"http://v1s1t0r999.herokuapp.com/make?src={site}&name={name}")
  print(resp.json())
  >> {"code":200, "error":false, "redirect":"http://gotto.tk/great", "src":"https://blog.somesite.com/imacool/how-to-be-cool"}
  print(resp.json().get("redirect"))
  >> http://gotto.tk/great
  ```

---


## Check if a name is available
Send a `GET` request to `http://gotto.tk/all_links.json` and recieve the JSON response. And check whether the name you want is available. If it ain't available, nothing can be done, but if you really want it, [Create an Issue](https://github.com/v1s1t0r999/cheap-bitly/issues) and I'll look into it 😉


---

*Note:*
  1. Both src and name are required parameters.
  2. Please wait for some time after recieving the response.

---


# VERY SOOS
## HOW?!?!?!?!?
`GET` request to `http://v1s1t0r999.herokuapp.com/email?email_id=<RECEIVER@EMAIL.COM>` with `json` as:
```json
{'subject':'IMPORTANT!', 'body':'THIS THING WORKS FOR REAL!!!!!'}
```
# -AND SEND EMAIL TO ANYONE ANONYMOUSLY!!


#ceoforever!
