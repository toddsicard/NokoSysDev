import N002Collector
import N001StackIt

payload = N002Collector.PayloadCollector()
msg = '{"WhatNow": "Full manual rewrite"}'
payload.newmsg(msg)
msg = '{"WhatNow": "Full manual rewrite3"}'
payload.newmsg(msg)
msg = '{"WhatNow": "Full manual rewrite2"}'
payload.newmsg(msg)

N001StackIt.StackIt(payload.allmsgs())
