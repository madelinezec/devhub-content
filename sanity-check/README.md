# Sanity Check

## What is it?

This small python script scans the blog posts: 
- tags,
- products,
- languages,
- unused images from the `source/images/` folder,
- images used but not found in the `source/images/` folder,
- missing information in twitter directive:
  - creator (with the @),
  - title (max size 70 characters),
  - image (with a relative path and image in the /images/ folder),
  - image-alt,
  - description (max size 160 characters),
- missing in the og directive:
  - title (max size 95 characters),
  - image,
- type should not be provided in the OG directive (automatic)
- URL is populated correctly automatically in the OG directive. (Only set one if you want something different (with https!)),
- meta-description (max size 155 characters),
- type,
- level,
- "include" directives with non existing content,
- "atf-image" directive presence and check image size (squared and >= 299px),
- twitter image size 1024x512,
- og image size 1200x630,
- prevent useless meta fields,
- links with the correct number of underscores,
- check "home" and "learn" featured pages are in snooty.toml,
- check all the blog posts in snooty.toml exist.

## Install packages

```bash
pip3 install -r requirements.txt
```

## Use it

Place your shell in the `sanity-check` folder.
```bash
python3 sanity-check.py
```

## Errors

The scripts tells you something like this?

```
ERROR: invalid element in directive '.. tags::' in file: ../source/article/top-4-reasons-to-use-mongodb.txt => 'SQL'
```

That's probably because you forgot the star `*` to make a list under the appropriate directive in this file.

### Do

```
.. products::

   * Stitch
   * Atlas
```

### Don't

```
.. products::

   Stitch
   Atlas
```

## Example output

```
polux@hafx:~/Work/devhub-content/sanity-check$ python3 sanity-check.py 

List of the invalid tags:

=> Invalid tag: AW  =>  ../source/how-to/golang-alexa-skills.txt

List of the invalid products:

=> Invalid product: Atla  =>  ../source/how-to/golang-alexa-skills.txt

List of the invalid languages:

=> Invalid language: G  =>  ../source/how-to/golang-alexa-skills.txt

List of the Twitter warnings:

=> Missing ":image:" with relative path                                =>  /article/stitch-triggers.txt                                            
=> Missing ":image-alt:"                                               =>  /article/stitch-triggers.txt                                            
=> Missing ":image-alt:"                                               =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Description too long (160 max) - need to remove 44 characters       =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Twitter title is too long (70 max) - need to remove 3 characters    =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Missing ":image-alt:"                                               =>  /article/srv-connection-strings.txt                                     
=> Missing ":image-alt:"                                               =>  /article/map-terms-concepts-sql-mongodb.txt                             
=> Missing ":image-alt:"                                               =>  /article/active-active-application-architectures.txt                    
=> Missing ":image-alt:"                                               =>  /article/top-4-reasons-to-use-mongodb.txt                               
=> Missing ":image:" with relative path                                =>  /how-to/data-enrichment-stitch.txt                                      
=> Missing ":image-alt:"                                               =>  /how-to/data-enrichment-stitch.txt                                      
=> Missing ":image:" with relative path                                =>  /how-to/atlas-data-lake-setup.txt                                       
=> Missing ":image-alt:"                                               =>  /how-to/atlas-data-lake-setup.txt                                       
=> Missing ":image-alt:"                                               =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Description too long (160 max) - need to remove 94 characters       =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Missing ":image-alt:"                                               =>  /how-to/nextjs-building-modern-applications.txt                         
=> Missing ":image:" with relative path                                =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Missing ":image-alt:"                                               =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Twitter title is too long (70 max) - need to remove 5 characters    =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Missing ":image:" with relative path                                =>  /how-to/golang-alexa-skills.txt                                         
=> Missing ":image-alt:"                                               =>  /how-to/golang-alexa-skills.txt                                         
=> Missing ":image-alt:"                                               =>  /how-to/attribute-pattern.txt                                           
=> Missing ":image-alt:"                                               =>  /how-to/stitch-shell.txt                                                
=> Description too long (160 max) - need to remove 63 characters       =>  /how-to/stitch-shell.txt                                                
=> Twitter title is too long (70 max) - need to remove 14 characters   =>  /how-to/stitch-shell.txt                                                
=> Missing ":image-alt:"                                               =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Twitter title is too long (70 max) - need to remove 5 characters    =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Missing ":image-alt:"                                               =>  /how-to/stitch-hosting.txt                                              
=> Missing ":image-alt:"                                               =>  /how-to/transactions-c-dotnet.txt                                       
=> Description too long (160 max) - need to remove 6 characters        =>  /how-to/transactions-c-dotnet.txt                                       
=> Missing ":image-alt:"                                               =>  /how-to/python-starlette-stitch.txt                                     
=> Missing ":image:" with relative path                                =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Missing ":image-alt:"                                               =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Twitter title is too long (70 max) - need to remove 11 characters   =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Missing ":image-alt:"                                               =>  /how-to/stitch-authentication-triggers.txt                              
=> Description too long (160 max) - need to remove 51 characters       =>  /how-to/stitch-authentication-triggers.txt                              
=> Missing ":image-alt:"                                               =>  /how-to/gatsby-modern-blog.txt                                          
=> Missing ":image:" with relative path                                =>  /how-to/polymorphic-pattern.txt                                         
=> Missing ":image-alt:"                                               =>  /how-to/polymorphic-pattern.txt                                         
=> Missing ":image:" with relative path                                =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Missing ":image-alt:"                                               =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Missing ":image-alt:"                                               =>  /how-to/storing-large-objects-and-files.txt                             
=> Missing ":image:" with relative path                                =>  /how-to/capture-iot-data-stitch.txt                                     
=> Missing ":image-alt:"                                               =>  /how-to/capture-iot-data-stitch.txt                                     
=> Missing ":image:" with relative path                                =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Missing ":image-alt:"                                               =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Missing ":image:" with relative path                                =>  /quickstart/java-mapping-pojos.txt                                      
=> Missing ":image-alt:"                                               =>  /quickstart/java-mapping-pojos.txt                                      
=> Twitter title is too long (70 max) - need to remove 6 characters    =>  /quickstart/java-mapping-pojos.txt                                      
=> Missing ":image:" with relative path                                =>  /quickstart/golang-change-streams.txt                                   
=> Missing ":image-alt:"                                               =>  /quickstart/golang-change-streams.txt                                   
=> Missing ":image:" with relative path                                =>  /quickstart/free-atlas-cluster.txt                                      
=> Missing ":image-alt:"                                               =>  /quickstart/free-atlas-cluster.txt                                      
=> Missing ":image:" with relative path                                =>  /quickstart/java-change-streams.txt                                     
=> Missing ":image-alt:"                                               =>  /quickstart/java-change-streams.txt                                     
=> Missing ":image-alt:"                                               =>  /quickstart/nodejs-change-streams-triggers.txt                          
=> Missing ":image:" with relative path                                =>  /quickstart/java-aggregation-pipeline.txt                               
=> Missing ":image-alt:"                                               =>  /quickstart/java-aggregation-pipeline.txt                               
=> Twitter title is too long (70 max) - need to remove 3 characters    =>  /quickstart/java-aggregation-pipeline.txt                               
=> Missing ":image-alt:"                                               =>  /quickstart/bson-data-types-decimal128.txt                              
=> Missing ":image-alt:"                                               =>  /quickstart/node-crud-tutorial.txt                                      
=> Missing ":image:" with relative path                                =>  /quickstart/python-acid-transactions.txt                                
=> Missing ":image-alt:"                                               =>  /quickstart/python-acid-transactions.txt                                
=> Description too long (160 max) - need to remove 39 characters       =>  /quickstart/python-acid-transactions.txt                                
=> Missing ":image-alt:"                                               =>  /quickstart/bson-data-types-objectid.txt                                
=> Missing ":image:" with relative path                                =>  /quickstart/python-change-streams.txt                                   
=> Missing ":image-alt:"                                               =>  /quickstart/python-change-streams.txt                                   
=> Description too long (160 max) - need to remove 127 characters      =>  /quickstart/python-change-streams.txt                                   
=> Missing ":image:" with relative path                                =>  /quickstart/java-setup-crud-operations.txt                              
=> Missing ":image-alt:"                                               =>  /quickstart/java-setup-crud-operations.txt                              
=> Description too long (160 max) - need to remove 101 characters      =>  /quickstart/java-setup-crud-operations.txt                              
=> Twitter title is too long (70 max) - need to remove 192 characters  =>  /quickstart/java-setup-crud-operations.txt                              

List of the Meta Description warnings:

=> meta-description is too long (155 characters max) - need to remove 49 characters   =>  /article/enterprise-operator-kubernetes-openshift.txt
=> meta-description is too long (155 characters max) - need to remove 99 characters   =>  /how-to/cidr-subnet-selection-atlas.txt              
=> meta-description is too long (155 characters max) - need to remove 215 characters  =>  /how-to/attribute-pattern.txt                        
=> meta-description is too long (155 characters max) - need to remove 68 characters   =>  /how-to/stitch-shell.txt                             
=> meta-description is too long (155 characters max) - need to remove 11 characters   =>  /how-to/transactions-c-dotnet.txt                    
=> meta-description is too long (155 characters max) - need to remove 56 characters   =>  /how-to/stitch-authentication-triggers.txt           
=> meta-description is too long (155 characters max) - need to remove 215 characters  =>  /how-to/polymorphic-pattern.txt                      
=> meta-description is too long (155 characters max) - need to remove 44 characters   =>  /quickstart/python-acid-transactions.txt             
=> meta-description is too long (155 characters max) - need to remove 132 characters  =>  /quickstart/python-change-streams.txt                

List of the og warnings:

=> Missing ":type: article"              =>  /article/stitch-triggers.txt                                            
=> Missing ":url:"                       =>  /article/stitch-triggers.txt                                            
=> Missing ":title:"                     =>  /article/stitch-triggers.txt                                            
=> Missing ":image:" with relative path  =>  /article/stitch-triggers.txt                                            
=> Description is empty.                 =>  /article/stitch-triggers.txt                                            
=> Missing ":type: article"              =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Missing ":url:"                       =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Missing ":title:"                     =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Missing ":image:" with relative path  =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Description is empty.                 =>  /article/enterprise-operator-kubernetes-openshift.txt                   
=> Missing ":type: article"              =>  /article/srv-connection-strings.txt                                     
=> Missing ":url:"                       =>  /article/srv-connection-strings.txt                                     
=> Missing ":title:"                     =>  /article/srv-connection-strings.txt                                     
=> Missing ":image:" with relative path  =>  /article/srv-connection-strings.txt                                     
=> Description is empty.                 =>  /article/srv-connection-strings.txt                                     
=> Missing ":type: article"              =>  /article/map-terms-concepts-sql-mongodb.txt                             
=> Missing ":url:"                       =>  /article/map-terms-concepts-sql-mongodb.txt                             
=> Missing ":title:"                     =>  /article/map-terms-concepts-sql-mongodb.txt                             
=> Missing ":image:" with relative path  =>  /article/map-terms-concepts-sql-mongodb.txt                             
=> Description is empty.                 =>  /article/map-terms-concepts-sql-mongodb.txt                             
=> Missing ":type: article"              =>  /article/active-active-application-architectures.txt                    
=> Missing ":url:"                       =>  /article/active-active-application-architectures.txt                    
=> Missing ":title:"                     =>  /article/active-active-application-architectures.txt                    
=> Missing ":image:" with relative path  =>  /article/active-active-application-architectures.txt                    
=> Description is empty.                 =>  /article/active-active-application-architectures.txt                    
=> Missing ":type: article"              =>  /article/top-4-reasons-to-use-mongodb.txt                               
=> Missing ":url:"                       =>  /article/top-4-reasons-to-use-mongodb.txt                               
=> Missing ":title:"                     =>  /article/top-4-reasons-to-use-mongodb.txt                               
=> Missing ":image:" with relative path  =>  /article/top-4-reasons-to-use-mongodb.txt                               
=> Description is empty.                 =>  /article/top-4-reasons-to-use-mongodb.txt                               
=> Missing ":type: article"              =>  /how-to/data-enrichment-stitch.txt                                      
=> Missing ":url:"                       =>  /how-to/data-enrichment-stitch.txt                                      
=> Missing ":title:"                     =>  /how-to/data-enrichment-stitch.txt                                      
=> Missing ":image:" with relative path  =>  /how-to/data-enrichment-stitch.txt                                      
=> Description is empty.                 =>  /how-to/data-enrichment-stitch.txt                                      
=> Missing ":type: article"              =>  /how-to/atlas-data-lake-setup.txt                                       
=> Missing ":url:"                       =>  /how-to/atlas-data-lake-setup.txt                                       
=> Missing ":title:"                     =>  /how-to/atlas-data-lake-setup.txt                                       
=> Missing ":image:" with relative path  =>  /how-to/atlas-data-lake-setup.txt                                       
=> Description is empty.                 =>  /how-to/atlas-data-lake-setup.txt                                       
=> Missing ":type: article"              =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Missing ":url:"                       =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Missing ":title:"                     =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Missing ":image:" with relative path  =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Description is empty.                 =>  /how-to/cidr-subnet-selection-atlas.txt                                 
=> Missing ":type: article"              =>  /how-to/nextjs-building-modern-applications.txt                         
=> Missing ":url:"                       =>  /how-to/nextjs-building-modern-applications.txt                         
=> Missing ":title:"                     =>  /how-to/nextjs-building-modern-applications.txt                         
=> Missing ":image:" with relative path  =>  /how-to/nextjs-building-modern-applications.txt                         
=> Description is empty.                 =>  /how-to/nextjs-building-modern-applications.txt                         
=> Missing ":type: article"              =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Missing ":url:"                       =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Missing ":title:"                     =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Missing ":image:" with relative path  =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Description is empty.                 =>  /how-to/nodejs-python-ruby-atlas-api.txt                                
=> Missing ":type: article"              =>  /how-to/golang-alexa-skills.txt                                         
=> Missing ":url:"                       =>  /how-to/golang-alexa-skills.txt                                         
=> Missing ":title:"                     =>  /how-to/golang-alexa-skills.txt                                         
=> Missing ":image:" with relative path  =>  /how-to/golang-alexa-skills.txt                                         
=> Description is empty.                 =>  /how-to/golang-alexa-skills.txt                                         
=> Missing ":type: article"              =>  /how-to/attribute-pattern.txt                                           
=> Missing ":url:"                       =>  /how-to/attribute-pattern.txt                                           
=> Missing ":title:"                     =>  /how-to/attribute-pattern.txt                                           
=> Missing ":image:" with relative path  =>  /how-to/attribute-pattern.txt                                           
=> Description is empty.                 =>  /how-to/attribute-pattern.txt                                           
=> Missing ":type: article"              =>  /how-to/stitch-shell.txt                                                
=> Missing ":url:"                       =>  /how-to/stitch-shell.txt                                                
=> Missing ":title:"                     =>  /how-to/stitch-shell.txt                                                
=> Missing ":image:" with relative path  =>  /how-to/stitch-shell.txt                                                
=> Description is empty.                 =>  /how-to/stitch-shell.txt                                                
=> Missing ":type: article"              =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Missing ":url:"                       =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Missing ":title:"                     =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Missing ":image:" with relative path  =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Description is empty.                 =>  /how-to/static-website-deployments-mongodb-stitch-hugo-git-travis-ci.txt
=> Missing ":type: article"              =>  /how-to/stitch-hosting.txt                                              
=> Missing ":url:"                       =>  /how-to/stitch-hosting.txt                                              
=> Missing ":title:"                     =>  /how-to/stitch-hosting.txt                                              
=> Missing ":image:" with relative path  =>  /how-to/stitch-hosting.txt                                              
=> Description is empty.                 =>  /how-to/stitch-hosting.txt                                              
=> Missing ":type: article"              =>  /how-to/transactions-c-dotnet.txt                                       
=> Missing ":url:"                       =>  /how-to/transactions-c-dotnet.txt                                       
=> Missing ":title:"                     =>  /how-to/transactions-c-dotnet.txt                                       
=> Missing ":image:" with relative path  =>  /how-to/transactions-c-dotnet.txt                                       
=> Description is empty.                 =>  /how-to/transactions-c-dotnet.txt                                       
=> Missing ":type: article"              =>  /how-to/python-starlette-stitch.txt                                     
=> Missing ":url:"                       =>  /how-to/python-starlette-stitch.txt                                     
=> Missing ":title:"                     =>  /how-to/python-starlette-stitch.txt                                     
=> Missing ":image:" with relative path  =>  /how-to/python-starlette-stitch.txt                                     
=> Description is empty.                 =>  /how-to/python-starlette-stitch.txt                                     
=> Missing ":type: article"              =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Missing ":url:"                       =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Missing ":title:"                     =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Missing ":image:" with relative path  =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Description is empty.                 =>  /how-to/search-engine-using-atlas-full-text-search.txt                  
=> Missing ":type: article"              =>  /how-to/stitch-authentication-triggers.txt                              
=> Missing ":url:"                       =>  /how-to/stitch-authentication-triggers.txt                              
=> Missing ":title:"                     =>  /how-to/stitch-authentication-triggers.txt                              
=> Missing ":image:" with relative path  =>  /how-to/stitch-authentication-triggers.txt                              
=> Description is empty.                 =>  /how-to/stitch-authentication-triggers.txt                              
=> Missing ":type: article"              =>  /how-to/gatsby-modern-blog.txt                                          
=> Missing ":url:"                       =>  /how-to/gatsby-modern-blog.txt                                          
=> Missing ":title:"                     =>  /how-to/gatsby-modern-blog.txt                                          
=> Missing ":image:" with relative path  =>  /how-to/gatsby-modern-blog.txt                                          
=> Description is empty.                 =>  /how-to/gatsby-modern-blog.txt                                          
=> Missing ":type: article"              =>  /how-to/polymorphic-pattern.txt                                         
=> Missing ":url:"                       =>  /how-to/polymorphic-pattern.txt                                         
=> Missing ":title:"                     =>  /how-to/polymorphic-pattern.txt                                         
=> Missing ":image:" with relative path  =>  /how-to/polymorphic-pattern.txt                                         
=> Description is empty.                 =>  /how-to/polymorphic-pattern.txt                                         
=> Missing ":type: article"              =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Missing ":url:"                       =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Missing ":title:"                     =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Missing ":image:" with relative path  =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Description is empty.                 =>  /how-to/graphql-support-atlas-stitch.txt                                
=> Missing ":type: article"              =>  /how-to/storing-large-objects-and-files.txt                             
=> Missing ":url:"                       =>  /how-to/storing-large-objects-and-files.txt                             
=> Missing ":title:"                     =>  /how-to/storing-large-objects-and-files.txt                             
=> Missing ":image:" with relative path  =>  /how-to/storing-large-objects-and-files.txt                             
=> Description is empty.                 =>  /how-to/storing-large-objects-and-files.txt                             
=> Missing ":type: article"              =>  /how-to/capture-iot-data-stitch.txt                                     
=> Missing ":url:"                       =>  /how-to/capture-iot-data-stitch.txt                                     
=> Missing ":title:"                     =>  /how-to/capture-iot-data-stitch.txt                                     
=> Missing ":image:" with relative path  =>  /how-to/capture-iot-data-stitch.txt                                     
=> Description is empty.                 =>  /how-to/capture-iot-data-stitch.txt                                     
=> Missing ":type: article"              =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Missing ":url:"                       =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Missing ":title:"                     =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Missing ":image:" with relative path  =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Description is empty.                 =>  /how-to/stitch-aws-rekognition-images.txt                               
=> Missing ":type: article"              =>  /quickstart/java-mapping-pojos.txt                                      
=> Missing ":url:"                       =>  /quickstart/java-mapping-pojos.txt                                      
=> Missing ":title:"                     =>  /quickstart/java-mapping-pojos.txt                                      
=> Missing ":image:" with relative path  =>  /quickstart/java-mapping-pojos.txt                                      
=> Description is empty.                 =>  /quickstart/java-mapping-pojos.txt                                      
=> Missing ":type: article"              =>  /quickstart/golang-change-streams.txt                                   
=> Missing ":url:"                       =>  /quickstart/golang-change-streams.txt                                   
=> Missing ":title:"                     =>  /quickstart/golang-change-streams.txt                                   
=> Missing ":image:" with relative path  =>  /quickstart/golang-change-streams.txt                                   
=> Description is empty.                 =>  /quickstart/golang-change-streams.txt                                   
=> Missing ":type: article"              =>  /quickstart/free-atlas-cluster.txt                                      
=> Missing ":url:"                       =>  /quickstart/free-atlas-cluster.txt                                      
=> Missing ":title:"                     =>  /quickstart/free-atlas-cluster.txt                                      
=> Missing ":image:" with relative path  =>  /quickstart/free-atlas-cluster.txt                                      
=> Description is empty.                 =>  /quickstart/free-atlas-cluster.txt                                      
=> Missing ":type: article"              =>  /quickstart/java-change-streams.txt                                     
=> Missing ":url:"                       =>  /quickstart/java-change-streams.txt                                     
=> Missing ":title:"                     =>  /quickstart/java-change-streams.txt                                     
=> Missing ":image:" with relative path  =>  /quickstart/java-change-streams.txt                                     
=> Description is empty.                 =>  /quickstart/java-change-streams.txt                                     
=> Missing ":type: article"              =>  /quickstart/nodejs-change-streams-triggers.txt                          
=> Missing ":url:"                       =>  /quickstart/nodejs-change-streams-triggers.txt                          
=> Missing ":title:"                     =>  /quickstart/nodejs-change-streams-triggers.txt                          
=> Missing ":image:" with relative path  =>  /quickstart/nodejs-change-streams-triggers.txt                          
=> Description is empty.                 =>  /quickstart/nodejs-change-streams-triggers.txt                          
=> Missing ":type: article"              =>  /quickstart/java-aggregation-pipeline.txt                               
=> Missing ":url:"                       =>  /quickstart/java-aggregation-pipeline.txt                               
=> Missing ":title:"                     =>  /quickstart/java-aggregation-pipeline.txt                               
=> Missing ":image:" with relative path  =>  /quickstart/java-aggregation-pipeline.txt                               
=> Description is empty.                 =>  /quickstart/java-aggregation-pipeline.txt                               
=> Missing ":type: article"              =>  /quickstart/bson-data-types-decimal128.txt                              
=> Missing ":url:"                       =>  /quickstart/bson-data-types-decimal128.txt                              
=> Missing ":title:"                     =>  /quickstart/bson-data-types-decimal128.txt                              
=> Missing ":image:" with relative path  =>  /quickstart/bson-data-types-decimal128.txt                              
=> Description is empty.                 =>  /quickstart/bson-data-types-decimal128.txt                              
=> Missing ":type: article"              =>  /quickstart/node-crud-tutorial.txt                                      
=> Missing ":url:"                       =>  /quickstart/node-crud-tutorial.txt                                      
=> Missing ":title:"                     =>  /quickstart/node-crud-tutorial.txt                                      
=> Missing ":image:" with relative path  =>  /quickstart/node-crud-tutorial.txt                                      
=> Description is empty.                 =>  /quickstart/node-crud-tutorial.txt                                      
=> Missing ":type: article"              =>  /quickstart/python-acid-transactions.txt                                
=> Missing ":url:"                       =>  /quickstart/python-acid-transactions.txt                                
=> Missing ":title:"                     =>  /quickstart/python-acid-transactions.txt                                
=> Missing ":image:" with relative path  =>  /quickstart/python-acid-transactions.txt                                
=> Description is empty.                 =>  /quickstart/python-acid-transactions.txt                                
=> Missing ":type: article"              =>  /quickstart/bson-data-types-objectid.txt                                
=> Missing ":url:"                       =>  /quickstart/bson-data-types-objectid.txt                                
=> Missing ":title:"                     =>  /quickstart/bson-data-types-objectid.txt                                
=> Missing ":image:" with relative path  =>  /quickstart/bson-data-types-objectid.txt                                
=> Description is empty.                 =>  /quickstart/bson-data-types-objectid.txt                                
=> Missing ":type: article"              =>  /quickstart/python-change-streams.txt                                   
=> Missing ":url:"                       =>  /quickstart/python-change-streams.txt                                   
=> Missing ":title:"                     =>  /quickstart/python-change-streams.txt                                   
=> Missing ":image:" with relative path  =>  /quickstart/python-change-streams.txt                                   
=> Description is empty.                 =>  /quickstart/python-change-streams.txt                                   
=> Missing ":type: article"              =>  /quickstart/java-setup-crud-operations.txt                              
=> Missing ":url:"                       =>  /quickstart/java-setup-crud-operations.txt                              
=> Missing ":title:"                     =>  /quickstart/java-setup-crud-operations.txt                              
=> Missing ":image:" with relative path  =>  /quickstart/java-setup-crud-operations.txt                              
=> Description is empty.                 =>  /quickstart/java-setup-crud-operations.txt                              

List of files with a wrong type:

=> Type directive is wrong in this file.  =>  /how-to/golang-alexa-skills.txt

List of files with a wrong level:

=> Level directive is wrong in this file.  =>  /how-to/golang-alexa-skills.txt

List of images not used:

=> /images/qs-badges/qs-badge-ruby.png
=> /images/qs-badges/qs-badge-csharp.png
=> /images/social/twitter/twitter-nextjs.png
=> /images/social/twitter/twitter-starlette.png
=> /images/social/twitter/twitter-specs.rst
=> /images/social/twitter/twitter-graphql.png
=> /images/social/twitter/twitter-sql-to-mdb.png
=> /images/social/twitter/twitter-build.png
=> /images/social/open-graph/og-sql-to-mdb.png
=> /images/social/open-graph/og-mdb-developer.png
=> /images/social/open-graph/og-gatsbyjs-mdb.png
=> /images/social/open-graph/og-nextjs.png
=> /images/social/open-graph/og-build.png
=> /images/social/open-graph/og-starlette.png
=> /images/social/open-graph/og-security.png
=> /images/social/open-graph/open-graph-specs.rst
=> /images/social/open-graph/og-sql-mdb.png
=> /images/social/open-graph/og-graphql.png
=> /images/bios/bio-generic.jpg
=> /images/atf-images/illustrations/community-card.png
=> /images/atf-images/illustrations/docs.png
=> /images/atf-images/illustrations/productivity.png
=> /images/atf-images/illustrations/sql-to-mdb.png
=> /images/atf-images/illustrations/data-streaming.png
=> /images/atf-images/photos/meetup.png
=> /images/atf-images/photos/fun-events.png
=> /images/atf-images/photos/nodejs.png
=> /images/atf-images/photos/age-gap.png
=> /images/atf-images/generic/purple2.png
=> /images/atf-images/generic/green2.png
=> /images/atf-images/logos/golang2.png
=> /images/atf-images/logos/kafka.png
=> /images/atf-images/logos/stitch-triggers.png
=> /images/atf-images/logos/twillio.png
=> /images/atf-images/logos/alexa-skills-2.png
=> /images/atf-images/logos/Unity.png
=> /images/atf-images/quickstart/ruby.png

List of includes not used:

=> /includes/authors/horowitz-eliot.rst

List of includes not found:

=> /includes/authors/rabdoy-nic.rst
```