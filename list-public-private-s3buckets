## this script will collecect the public and private s3 buckstes on the status of get-public-block api call
# i am using  only one condition to filter but we can add others conditions also

for s3_buckets in `aws s3 ls | cut -f 3 -d ' '`
do
  result=`aws s3api get-public-access-block --bucket $s3_buckets  --output json | jq '.PublicAccessBlockConfiguration.RestrictPublicBuckets'`

    if [ "$result"  == "false" ]
      then
        `echo "${s3_buckets}" >> public_buckets.csv`


    elif [ "$result"  == "true" ]
      then
        `echo  "${s3_buckets}" >> private_buckets.csv`
    else
      echo "\n" 
    fi   
done      
     
