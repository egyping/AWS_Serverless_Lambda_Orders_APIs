# AWS_Serverless_Lambda_Orders_APIs

** Tools setup **
python3.8 installation 
- AWS new account 
- AWS CLI install v2 
    Google AWS install and continue
    to upgrade >> brew upgrade awscli
- AWS new user has AdministratorAccess policy
    Create AWS user to run the project from DON'T use the ROOT account
    >> aws configure
    to access the config file 
    >> nano ~/.aws/credentials
    to run commands using specific account 
    >> aws s3 ls -profile ProfileName
- AWS SAM install 
    Google AWS install and continue
    >> brew install aws-sam-cli
    to upgrade 
    >> brew upgrade aws-sam-cli
        serverless app deployment WITHOUT SAM 
            ZIP - uload to s3 - create IAM Roles, Resources, Functions and permissions 
        SAM framework it deploy template file, the file has all the resources and instructions
        SAM from AWS and there are many others 
        SAM build and SAM deploy will deploy all the steps mentioned at WITHOUT section
- Install POSTMAN

** YAML in Short **
YAML widely used as instructor for other tools like docker and sam 
YAMl has the followings 
simpleKey: stringValue
simpleIntKey: 123
valueKey: True 
list:
    - list item one 
    - list item two 
anotherWayofList: [item1: value1, item2: value2]
dictionary:
    dictionaryValue1
    dictionaryValue2
and you can validate it with any online validator 
*****************

** Hello wrold **
mkdir helloworld
sam init 
choice 1
runtime python
project name > HelloWorld
Hello world example 

above steps will deploy some files locally you can go through it 

build >> sam build --guided 
fllow along with the questions 
this command will pull the local files to S3 and all deployments go through cloudformation 
all the deployment moves on the template.yaml instructor 
after deployment happens you can review it from AWS CF-Stack 


************


** Orders Project **

Two API gateway 
First API >> lambda to create orders and save it to >> DynamoDB
Second API >> lambda to read the orders from >> DynamoDB
mkdir orders_lambda
cd orders_lambda
sam init
quick start templates > Hello world examples > name: orders-api 
rename the hellow world folder to orders_api
open the template.yaml and remove the Outputs and Global sections 
change the CodeUri value to the renamed folder name
(1) simple functiona and api return empty message read and create 
    Create Order Lambda function 
        create new python file file orders_api/create.py
        create.py >> (1)
    add API gateway to trigger lambda 
        add events section at template.yaml
        change the Function to CreateOrderFunction
    deploy and test 
        cd to the directory has the template file 
        sam build 
        sam deploy --guided
        review CF and test API via postman 
            POST > Body > Raw > Json > 
            https://aos6j1aw7g.execute-api.us-east-1.amazonaws.com/Stage/orders/
    Read Order Lambda function 
        create new python file file orders_api/read.py
        rest same like Create
        sam build sam deploy 
(2) using the global properties 
    common repeated otions we can add it under global
    such as runtime, architecture and timeout
    sam local start-api   >> to test local
(3) Create dynamoDB table and create and read final 
    template.yaml >> add the OrdersTable >> and add Env Variable at the global to access 
    the table name then you can refer to it from the create and read.py handlers
    policies to access dynamodb
        at Policies: for both read and create 
    add boto3 and simplejson to requirements
    add the output section
    sam build 
    sam deploy






