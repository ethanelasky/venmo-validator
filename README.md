# venmo-validator

This webapp quickly validates Venmo handles to ensure that they are typo-free. A user can input a list of Venmo handles, and after a few seconds, the website will display a chart which handles exist and which handles do not. 

The website includes a time delay to avoid anti-bot measures. Each additional Venmo handle adds a delay of _Poisson_(1.5) seconds (basically, ≈1.5 seconds, with some unsymmetric noise added to it). 

I developed this website as part of my involvement in the Haas Business School's Business and Social Psychology Lab. This website allows us to check that a handle is valid before a payment is sent, reducing headaches when it comes time to compensate survey participants.
