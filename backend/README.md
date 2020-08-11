## Loan Calculator Backend

This project is a small server that uses parameters such as:
* the monthly rate one would have to pay
* the number of months to pay back the loan 
* the interest 

to compute the ones that are missing. The API has one one endpoint that can be accessed without authentication (at the time being). The information is sent via query parameters.


### How to run it

To be continued.

### Questions to ponder

The implementation of this loan calculator is as simple as it gets. However, as times goes by, it could have some improvements:

- do we need to authenticate the user?
- should we have these queries somewhere?
- would be benefit from using caching?
- numpy could prove to be not very memory efficient, should we implement those computations ourselves?

