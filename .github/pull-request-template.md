# Author Checklist
The post author should complete this section. If your post is not ready for review, please add the `WIP - Do not review yet` label.
* [ ] [Jira ticket link](PUT JIRA LINK HERE)
* [ ] The name of this PR starts with the Jira ticket ID (e.g. "DA-123: Awesome blog post title").
* [ ] I created and linked a DEVSOCIAL Jira ticket to my DA ticket following the [Social Media Content request process](https://wiki.corp.mongodb.com/pages/viewpage.action?pageId=100263451).
* [ ] If I need new images, I created a DESIGN ticket and linked it to the DA ticket.
* [ ] For EVERY new commit, I have taken the actions below and updated the links: 
  * [ ] I ran the `sanity-check.py` script, and I fixed all the warnings about my blog post.
  * [ ] I built my branch and the builder log doesn't contain warnings or errors.
  * [ ] [Builder log link](PUT LOG LINK HERE)
  * [ ] [Staging blog post link](PUT BLOG POST LINK HERE)
* [ ] The post has received LGTM from a technical reviewer and an editorial reviewer. I am finished making updates based on the reviews, and the post is ready for publication. Please publish this post...
  * [ ] As soon as possible
  * [ ] On the following date: TBD

# Technical Reviewer Checklist
When you (the author) are ready for a technical review, add the `Technical Review Wanted` label. If you want a review from someone in particular, add them as a reviewer in the PR. If not, someone from the [Response Team](https://wiki.corp.mongodb.com/display/DEVREL/Response+Team) will review the post. If you want to get a technical review before creating a PR, copy this checklist to your DA ticket and request a review there.

Name of technical reviewer:
* [ ] LGTM!

## Correctness
* [ ] Concepts are presented accurately
* [ ] Code samples are syntactically correct
* [ ] Code for any sample apps is included in a GitHub repo in https://github.com/mongodb-developer with an Apache 2 license and a readme
* [ ] Necessary version numbers are included using the `.. prerequisites::` directive.
* [ ] Tutorial steps work top to bottom
* [ ] Links work as expected

## Style
* [ ] The concepts presented are easy to understand
* [ ] Relevant links are included
* [ ] Code samples follow best practices of their language and/or MongoDB

# Editorial Reviewer Checklist
Once you have a LGTM from a technical reviewer above, request a review from Megan Grant (GitHub id Meg528) and add the `Editorial Review Wanted` label. She will complete the fields below.

* [ ] LGTM!

## Correctness
* [ ] Sentences are grammatically correct
* [ ] Post is free of typos
* [ ] Post contains a Community Call to Action (either using `source/includes/callouts/community-cta.rst` or custom `blockquote`)

## Accessibility
* [ ] All images have alternate text
* [ ] Shell output and commands are inside of code blocks instead of images

## Style
The [MongoDB Style Guide](https://docs.mongodb.com/meta/style-guide) can be used as a reference.
* [ ] Items in headings and lists have consistent style and formatting
* [ ] Sentences are easy to follow and understand
* [ ] Paragraphs contain information about a single idea
* [ ] Post does not contain words that make readers feel dumb like "obviously" and "clearly"
* [ ] Post does not contain gendered language, like "guys", and does not automatically default to referring to people as "he/him," etc. 
* [ ] Non-common acronyms are defined
