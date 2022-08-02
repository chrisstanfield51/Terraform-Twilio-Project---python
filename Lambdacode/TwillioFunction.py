#_/_/_/_/_/_/_/_/_/_/_/_/
#Twilio Handler Function
#_/_/_/_/_/_/_/_/_/_/_/_/
import boto3

ec2_client = boto3.client('ec2')

#define function to change the state of an instance to the desired state
def change_state(instance_id, desired_state):
    #if text message includes "Start", then set the filtered instances to start
    if desired_state == "Start":
        try:
            ec2_client.start_instances(InstanceIds=[instance_id])
            print("Instance {} Has Started".format(instance_id))
        except Exception as e:
            print(e)
    #if text message includes "Stop", then set the filtered instances to stop
    elif desired_state == "Stop":
        try:
            ec2_client.stop_instances(InstanceIds=[instance_id])
            print("Instance {} Has Stopped".format(instance_id))
        except Exception as e:
            print(e)
    #if text message includes neither, then return nothing
    else:
        print("Instance {} State Has Not Changed".format(instance_id))

#definition to get all the instances ids that match a specific filter
def get_instance_ids(instance_state):
    instance_ids = []
    #this filter finds all tags with "TestInstance" and the desired state
    custom_filter = [{
        'Name': 'tag:Name',
        'Values': ['TestInstance']},
        {
            'Name': 'instance-state-name',
            'Values': [instance_state]},
    ]
    
    try:
        #this line uses describe_instances to gather all attributes of every ec2 client and then
        #runs then through a loop to grab all the instance ID's that match
        instances = ec2_client.describe_instances(Filters=custom_filter)
        for r in instances['Reservations']:
            for i in r['Instances']:
                #adds all instance ID's to the instance_ids array
                instance_ids.append(i['InstanceId'])
        #returns the array
        return instance_ids
    except Exception as e:
        print(e)

#main handler definition for lambda
def lambda_handler(event, context):
    print("Received event: " + str(event))
    body = event['Body']
    #if a text message with stop is received, run through this 'if'
    if "Stop" in body:
        #grabs all instances that are running plus the custom filter
        instance_ids = get_instance_ids("running")
        if len(instance_ids) != 0:
            for instance_id in instance_ids:
                #calls on the change_state definition to stop instances
                change_state(instance_id, "Stop")
                #return acknowledgement to Twilio
                return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
                       "<Response><Message><Body>Stopping Instance!</Body></Message></Response>"
    #if a text message with start is received, run through this 'if'
    elif "Start" in body:
        instance_ids = get_instance_ids("stopped")
        if len(instance_ids) != 0:
            for instance_id in instance_ids:
                #calls on the change_state definition to start instances
                change_state(instance_id, "Start")
                #return acknowledgement to Twilio
                return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
                       "<Response><Message><Body>Starting Instance!</Body></Message></Response>"
    else:
        print("No Status In Body")
        #return issue to Twilio
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
               "<Response><Message><Body>Command not recognized.  Try again.</Body></Message></Response>"