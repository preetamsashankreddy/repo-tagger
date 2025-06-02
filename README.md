# repo-tagger

This is a simnple python 3 utility that helps create a common tag across multiple git repositories.
It takes in a json file 'repo-list.json'; hard coded for now; and goes over it to acquire the tag to create as well as repositories to download.
Once it creates the tags, it will try to push them.

# repo-list.json format

`"apply_tag": <value>` -> Tag that will be applied across the repos.
`"repositories": ` -> A json list that will have the following elements:
    `"url"` -> The url for downaload
    `"object"` -> This can be any identifier such as branch name or an aexisting tag / hash. This is what will be cheked out.

# Future

In future, there will be more options and customizations allowing a more refined utility.