# datsci_testing
A repository for tinkering and learning, related to a class I took.


## Homework 2
- How do you fill in the missing dates from the grants data?

I'd fill them in as NaN, as there's no real way to know when they were supposed to be. You could estimate, but this is innacurate. They already are this way by default, so nothing needs to be done.

- PI_NAMEs contains multiple names. We can only connect individual people. Can you make it so that we can get "grantees"?

I'll make a new column in the data frame titled 'grantees' that contains each grantee in a list. 

- The dates for Articles are problematic. Can you fix them?

The program initially only reads line breaks for the dates. I can fix them by redefining how the data frame reads the date/time info should work.

## Homework 3
First I modified HAR to include step count. Presumably, if someone is asleep their step count should be low or zero. Then I took the asbolute value of the individual's movement, as if they're asleep they're likely also moving a lot less. They would also have a lower heart rate, so that can be used as well. 
Printing accuracy, we get a success rate of 0.8689556749496307.

## Homework 4
Running the classifier again, we get a success rate of 0.7238979118329466 for random forest and 0.7682134570765661 for xgboost.
Installing fasttext required a lot of extra work. The provided solution was not effective. In the end, the best solution I could find was using a downgraded python instance.