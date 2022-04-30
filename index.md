# Easy-Bitly+Sendgrid 💀

## [Easy Bitly](https://gotto.tk)
- **Tons of link shortners out there, but you gotta pay for a custom name!**
### How-To?
1. Send a `GET` request to `https://do.gotto.tk/make` with parameters `src` and `name`
2. Request: `curl https://api.gotto.tk/make?src=<https://source.com/page/yea>&name=<custom_name>`
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
- On it 💀


