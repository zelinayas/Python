import win32com.client

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
qinfo.FormatName="direct=os:ulfah\\private$\\bootcamp"
queue=qinfo.Open(2,0) #open a ref to queue
msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
msg.Label='TestMsg'
msg.Body="The quick brown fox jumps over the lazy dog"
msg.Send(queue)

queue.Close()