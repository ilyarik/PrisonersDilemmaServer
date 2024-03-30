from socket import *
import re


HOST = ""
PORT = 58999

iteration = 0

def make_decision(msg: bytes) -> bytes:
    if iteration == 0:
        return b"C"
    match = re.search(br"Player \d+\s+(C|D|\.)*?(?P<decision>C|D) \d+", msg)
    if not match:
        raise ValueError("Can't find last decision")
    # print(f"Opp decision: {match.group('decision')}")
    match match.group("decision"):
        case b"C":
            return b"C"
        case b"D":
            return b"D"
        case _:
            raise ValueError


if __name__ == "__main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    text = s.recv(20_000)
    decision = b"C"
    while True:
        text = s.recv(20_000)
        print(text.decode())
        if text == b"":
            break
        if b"End of the round" in text:
            iteration = 0
        if b"Player " in text:
            decision = make_decision(text)
        if text.endswith(b"Your turn: "):
            s.send(decision+b"\n")
            iteration += 1
    s.close()
    print("END")
