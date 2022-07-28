Here's a regex for checking social security number that I got off a [website](https://digitalfortress.tech/tips/top-15-commonly-used-regex/):
`/^((?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4})|((?!219 09 9999|078 05 1120)(?!666|000|9\d{2})\d{3} (?!00)\d{2} (?!0{4})\d{4})|((?!219099999|078051120)(?!666|000|9\d{2})\d{3}(?!00)\d{2}(?!0{4})\d{4})$/`

It is useful because it can determine if the user entered the correct social identity format when the number is needed. It can reduce spam or incorrect formatted social security number being sent to government services for further verification. I find it interesting that it can detect both dashes and space.

What the regex is looking for:

- Not 078-05-1120, 219-09-9999
- Not begin with 666 or any value between 900-999
- Does not contain all zeros in a specific group.
- 3-2-4 group

Examples of strings that the regular expression matches:
293 38 0289
034 93 2834
636 98 8039
038-05-1120

Response:
Hi Kyle,

I think using a regular expression to check for password strength is a good idea as people tend to use weak passwords that are easily cracked. One improvement to your regex is adding the exclusion of common phrases, such as `(?!.*pass|.*word|.*1234|.*asdf)` or running the password through a dictionary of common passwords after the password passes the first regular expression test.
I like to use passphrases, so I would use regex that's something like this:
`^\S{6,}[-]+\S{6,}[-]+\S{6,}$`
It's looking for 3 groups of 6 characters or more separated by one or more `-`. One example is `Nugget-Watt3d-Grade5`
