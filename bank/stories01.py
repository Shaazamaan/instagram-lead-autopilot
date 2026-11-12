# Story bank 01. EXAMPLE ONLY: setup replaces it. kinds: tip, quiz (question + answer card), contact (reply-with-keyword card).
T = []
def tip(id, segment, title, body): T.append(dict(id=id, kind="tip", segment=segment, title=title, body=body))
def quiz(id, segment, q, a, why): T.append(dict(id=id, kind="quiz", segment=segment, q=q, a=a, why=why))
def contact(id, segment, line, kw): T.append(dict(id=id, kind="contact", segment=segment, line=line, kw=kw))

tip("t001", "solo", "Starting alone?", "You can still do it properly from day one.")
contact("t002", "freelancer", "Not sure where to start?", "START")
