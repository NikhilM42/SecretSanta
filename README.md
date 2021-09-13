# SecretSanta
Secret Santa Generator

This script takes a list of names and generates textfiles that have the name of the gifter as the filename. Each text file stores the giftee that has been assigned to the gifter.

This was another excuse to practice Python and I didnt feel like using the online Secret Santa generator.

## How to Use
 Simply fill the text file called *List.txt* with the names of the group that will be doing the Secret Santa. Each name should get its own line. If any person should not be paired with another simply add the name of the person to avoid inline with the other person seperated by a space.

**NOTE** Spaces are sensitive so if you need to use first name and last name simply combine without a space.

> FirstNameLastName

## Example

Consider the following list:

> PersonA\
PersonB PersonD\
PersonC\
PersonD PersonB

Space

## Limitations
This script only supports avoiding one combination per person and does not track history.