# Easy-Bitly+Sendgrid 💀

## [Easy Bitly](https://gotto.tk)
- **Tons of link shortners out there, but you gotta pay for a custom name!**
### How-To?
1. Send a `GET` request to `https://v1s1t0r999.herokuapp.com/make` with parameters `src` and `name`
2. Request: `curl https://v1s1t0r999.herokuapp.com/make?src=https://source.com/page/yea&name=custom_name`
3. Response:
   - Success [200]: Shortening was successful.
     - JSON: `{"code":200,"error":false,"redirect":"https://gotto.tk/custom_name","src":"https://source.com/page/yea"}` OR `{"code":200,"error":false,"redirect":"https://gotto.tk/random_name","src":"https://source.com/page/yea"}` (if name "custom_name" is already taken)
    - Not Found [401]: Source was not found (404 returned)
       - JSON: `{"code":401,"error":true,"msg":"https://source.com/page/yea could not be found."}`

    - Parameters Missing [403]: Some arguments are missing.
      - JSON: `{"code":403,"error":true,"msg":"'<param>' is a required param."}`
    
    - Backend Error [500]: Something in the code just ~~Cucked~~ Up ;(
      - JSON: `{'error':True,'raw':'raw traceback of the error'}`


---
## [Easy-Sendgrid](https://gotto.tk/email-api)
- Request: (GET)
   `curl https://v1s1t0r999.herokuapp.com/email?email_id=myemail@anyservice.com` with json as `{"subject":"That's a subject.", "body":"Heh...thats the body!"}`
- Response:
   ```json
   {
    "code": 200,
    "data": {
        "email_body": "This don't work: https://discord.gg/zFBfXDY7RY",
        "sent_to": "pritam42069@protonmail.com",
        "subject": "BRUH"
    },
    "error": false,
    "msg": "Success!",
    "raw": "\n\t\t\t\u001b[96mSender:\u001b[0m gotto.tk@gmail.com\n\t\t\t\u001b[96mRecipient(s):\u001b[0m pritam42069@protonmail.com\n\n\t\t\t------------------------------\n\n\t\t\t\u001b[96mSubject:\u001b[0m BRUH\n\t\t\t\u001b[96mMessage:\u001b[0m This don't work: https://discord.gg/zFBfXDY7RY\n\n\n---\nSent Anonymously using `https://gotto.tk` ;)\n---\n"
}
   ```


