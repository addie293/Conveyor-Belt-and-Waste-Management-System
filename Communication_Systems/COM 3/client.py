import time
import win32com.client

# Instantiate the client object
client = win32com.client.Dispatch('OpcLabs.EasyOpc.UA.EasyUAClient') 
client.PullDataChangeNotificationQueueCapacity = 1000
print('Subscribing...')
client.SubscribeDataChange('http://opcua.demo-this.com:51211/UA/SampleServer', 
   'nsu=http://test.org/UA/Data/;i=10853', 1000)

print('Processing data change events for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    eventArgs = client.PullDataChangeNotification(2*1000)
    if eventArgs is not None:
        # Handle the notification event
        print(eventArgs)
