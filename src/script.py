import os
import sys
from datetime import datetime, timedelta

import pexpect
import pyotp
from dotenv import load_dotenv


def main():
    load_dotenv()

    user_prompt = os.getenv("USER_PROMPT")
    password_prompt = os.getenv("PASSWORD_PROMPT")
    vpn_command = os.getenv("VPN_COMMAND")
    user = os.getenv("VPN_USERNAME")
    password = os.getenv("VPN_PASSWORD")
    otp_prompt = os.getenv("OTP_PROMPT")
    otp_secret = os.getenv("OTP_SECRET")

    child = pexpect.spawn(vpn_command)
    child.expect(user_prompt)
    child.sendline(user)

    child.expect(password_prompt)
    child.sendline(password)

    if otp_prompt:
        otp = pyotp.TOTP(otp_secret).at(datetime.now() + timedelta(seconds=1))
        child.expect(otp_prompt)
        child.sendline(str(otp))

    child.logfile = sys.stdout.buffer
    child.expect(pexpect.EOF, timeout=None)


if __name__ == "__main__":
    main()
