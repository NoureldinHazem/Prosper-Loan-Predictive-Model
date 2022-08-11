# Loan-Completion-Prediction
## Predictive Modelling Using Social Profile in Online P2P Lending Market

## Introduction to the project :
> Online peer-to-peer (P2P) lending markets enable individual consumers to
borrow from, and lend money to, one another directly. We study the borrower-,
loan- and group- related determinants of performance predictability in an
online P2P lending market by conceptualizing financial and social strength to
predict borrower rate and whether the loan would be timely paid. The result of
our empirical study, conducted using a database of 9479 completed P2P
transactions in calendar year 2007, provide support for the proposed
conceptual model in this study. The results showed that combing financial files
with social indicators can enhance the performance predictability in P2P
lending market. Although social strength attributes do affect the borrower rate
and status, their effects are very small in comparison to financial strength
attributes. This paper concludes with specific suggestions to borrowers and
lenders to increase their chances of funding to refunding completely in P2P
lending market, and a discussion of future research opportunities.

## Understanding the Dataset :
**Dataset consists of 113,937 samples and 81 features.**

> Features are = { ListingKey, ListingNumber, ListingCreationDate, CreditGrade, Term, LoanStatus, ClosedDate, BorrowerAPR, BorrowerRate, LenderYield, EstimatedEffectiveYield, EstimatedLoss, EstimatedReturn, ProsperRating (numeric), ProsperRating (Alpha), ProsperScore, ListingCategory (numeric), BorrowerState, Occupation, EmploymentStatus, EmploymentStatusDuration, IsBorrowerHomeowner, CurrentlyInGroup, GroupKey, DateCreditPulled, CreditScoreRangeLower, CreditScoreRangeUpper, FirstRecordedCreditLine, CurrentCreditLines, OpenCreditLines, TotalCreditLinespast7years, OpenRevolvingAccounts, OpenRevolvingMonthlyPayment, InquiriesLast6Months, TotalInquiries, CurrentDelinquencies, AmountDelinquent, DelinquenciesLast7Years, PublicRecordsLast10Years, PublicRecordsLast12Months, RevolvingCreditBalance, BankcardUtilization, AvailableBankcardCredit, TotalTrades, TradesNeverDelinquent (percentage), TradesOpenedLast6Months, DebtToIncomeRatio, IncomeRange, IncomeVerifiable, StatedMonthlyIncome, LoanKey, TotalProsperLoans, TotalProsperPaymentsBilled, OnTimeProsperPayments, ProsperPaymentsLessThanOneMonthLate, ProsperPaymentsOneMonthPlusLate, ProsperPrincipalBorrowed, ProsperPrincipalOutstanding, ScorexChangeAtTimeOfListing, LoanCurrentDaysDelinquent, LoanFirstDefaultedCycleNumber, LoanMonthsSinceOrigination, LoanNumber, LoanOriginalAmount, LoanOriginationDate, LoanOriginationQuarter, MemberKey, MonthlyLoanPayment, LP_CustomerPayments, LP_CustomerPrincipalPayments, LP_InterestandFees, LP_ServiceFees, LP_CollectionFees, LP_GrossPrincipalLoss, LP_NetPrincipalLoss, LP_NonPrincipalRecoverypayments, PercentFunded, Recommendations, InvestmentFromFriendsCount, InvestmentFromFriendsAmount, Investors}.
## Data Cleaning :
1) Checking Null values and Printing their missing percentage amd count.
2) Reformatting any feature with datatime with format '%Y-%m-%d %H:%M:%S'
>features = { ListingCreationDate, DateCreditPulled, LoanOriginationDate, FirstRecordedCreditLine, ClosedDate}
3) Handling missing values in FirstRecordedCreditLine, ClosedDate by adding upcoming date.
4) Filling some features by adding the mean in the missing samples.
> Features = { BorrowerAPR, EstimatedEffectiveYield, EstimatedLoss, EstimatedReturn, EmploymentStatusDuration, CreditScoreRangeLower, CreditScoreRangeUpper, RevolvingCreditBalance, BankcardUtilization, AvailableBankcardCredit, TotalTrades, TradesNeverDelinquent (percentage),TradesOpenedLast6Months, DebtToIncomeRatio}.
5) Filling some features by adding 0 in the missing samples.
> Features = { TotalProsperLoans, TotalProsperPaymentsBilled,OnTimeProsperPayments, ProsperPaymentsLessThanOneMonthLate, ProsperPaymentsOneMonthPlusLate, ProsperPrincipalBorrowed, ProsperPrincipalOutstanding, ScorexChangeAtTimeOfListing, CurrentCreditLines, OpenCreditLines, TotalCreditLinespast7years, InquiriesLast6Months, TotalInquiries, CurrentDelinquencies, AmountDelinquent, DelinquenciesLast7Years, PublicRecordsLast10Years, PublicRecordsLast12Months}.
6) Filling null values in BorrowerState with 'CA'.
7) Filling null values in Occupation with 'Other'.
8) Filling null values in EmploymentStatus with 'Unknow'.
9) Filling CreditGrade according to CreditScore.
> CreditScore < 300 will be 'NC'. <br>
> 300 < CreditScore < 559 will be 'HR'. <br>
> 560 < CreditScore < 599 will be 'E'.<br>
> 600 < CreditScore < 639 will be 'D'.<br>
> 640 < CreditScore < 679 will be 'C'.<br>
> 680 < CreditScore < 719 will be 'B'.<br>
> 720 < CreditScore < 759 will be 'A'.<br>
> CreditScore > 759 will be 'AA'.
10) Filling null values in LoanFirstDefaultedCycleNumber by -1.
11) Dropping features that are keys or have alot of null values.
> Features = { GroupKey, LisitingKey, LisitingNumber, LoanKey, MemberKey, LoanNumber}.
13) Dropping samples that have null values in some features.
> Features = { ProsperRating (numeric), ProsperScore, ProsperRating (Alpha)}.

## Feature Engineering
