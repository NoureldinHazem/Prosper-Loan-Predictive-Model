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

## Feature Engineering :
1) Checking Correlation for numerical variables.
> Printing values in tables and on heatmap.
2) Printing Descriptive Statistics.
> using .describe()
3) Printing info of the dataframe to know the type of each feature.
> using .info()
4) Dropping samples with ListingCreationDate before 2008.
>  There was financial crisis in 2008.
5) Dropping features with datatime type.
6) Changing features with datatype boolean to float.
7) Removing duplications.
8) Visulaization of features with datatype object and detrmine what to do with it dropping or mapping.
> CreditGrade will be dropped as CreditScoreRangeLower & CreditScoreRangeUpper is equivalent to it.<br>
> ProsperRating (Alpha) will be dropped as ProsperRating (numeric) is equivalent to it.<br>
> BorrowerState will be dropped.<br>
> Occupation will be dropped.<br>
> LoanOriginationQuarter will be dropped.<br>
> EmploymentStatus will be mapped as 'Employed', 'Full-time', 'Self-employed', 'Part-time' will be 1 and the rest will be 0.<br>
>  IncomeRange will be mapped as i will put in it the mean of each range of them.<br>
>  LoanStatus will drop samples with 'Current' as it is hard to detrimine if it will complete the loan or not, and will map the rest as 'Completed' will be 1 and the rest will be 0.<br>
9) Dropping some features after looking to the correlation heatmap.
> Features = { EmploymentStatus, Investors, InvestmentFromFriendsAmount, InvestmentFromFriendsCount, Term, ListingCategory (numeric), EmploymentStatusDuration, IsBorrowerHomeowner, CurrentlyInGroup, CurrentCreditLines, OpenCreditLines, TotalCreditLinespast7years, OpenRevolvingAccounts, OpenRevolvingMonthlyPayment, InquiriesLast6Months, TotalInquiries, CurrentDelinquencies, AmountDelinquent, DelinquenciesLast7Years, PublicRecordsLast12Months, PublicRecordsLast10Years, RevolvingCreditBalance, TotalProsperPaymentsBilled, TotalProsperLoans, LP_CustomerPayments, LP_NetPrincipalLoss, EstimatedEffectiveYield, EstimatedLoss, LoanCurrentDaysDelinquent, LP_InterestandFees, LoanFirstDefaultedCycleNumber, Recommendations, PercentFunded }.
10) Handling outliner of the remaining features.
> After removing outliners some features become the same value for all the samples. So, they will be dropped.
> Features = { LP_NonPrincipalRecoverypayments, LP_GrossPrincipalLoss, LP_CollectionFees, ScorexChangeAtTimeOfListing, ProsperPrincipalOutstanding, ProsperPaymentsLessThanOneMonthLate, ProsperPrincipalBorrowed, OnTimeProsperPayments, IncomeVerifiable, DebtToIncomeRatio, TradesOpenedLast6Months, TradesNeverDelinquent (percentage), TotalTrades }.

## Models :
> Making multiple copies of the dataframe.
1) Logistic Regression :<br>
Model is done with max_iter=1000
> 'LoanStatus' will be the Labels.<br>
> Splitting data with 20% test and 80% train.<br>
> Feature scaling will be done by preprocessing.MinMaxScaler() to let each feature have the same important as the other features.<br>
> Undersampling will be done by RandomUnderSampler(random_state=0) to let samples with label 0 equal to samples with label 1.<br>
2) Neural Network:<br>
Model consists of 2 fully connected layers first layer with 128 neurouns, second with 10 neurouns and the last with 1 neurouns (sigmoid), loss is calculated using 'binary_crossentropy'.<br>
Batch size = 1024 and epochs = 1000.
> 'LoanStatus' will be the Labels.<br>
> Splitting data with 20% test , 70% train and 10% validation.<br>
> Feature scaling will be done by preprocessing.MinMaxScaler() to let each feature have the same important as the other features.<br>
> Undersampling will be done by RandomUnderSampler(random_state=0) to let samples with label 0 equal to samples with label 1.<br>
3) Naive Bayes :<br>
Gaussian naive bayes is used.
> 'LoanStatus' will be the Labels.<br>
> Splitting data with 20% test and 80% train.<br>
> Feature scaling will be done by preprocessing.MinMaxScaler() to let each feature have the same important as the other features.<br>
> Undersampling will be done by RandomUnderSampler(random_state=0) to let samples with label 0 equal to samples with label 1.<br>
4) Decision Trees :<br>
tree.DecisionTreeClassifier() is used.
> 'LoanStatus' will be the Labels.<br>
> Splitting data with 20% test and 80% train.<br>
> Feature scaling will be done by preprocessing.MinMaxScaler() to let each feature have the same important as the other features.<br>
> Undersampling will be done by RandomUnderSampler(random_state=0) to let samples with label 0 equal to samples with label 1.<br>

## Model Accuracy:
1) Logistic Regression :
> Accuracy = 92 % <br>
> Recall = 90 % at class 0 and 94 % at class 1. [ avg = 92 %] <br>
> Precision = 94 % at class 0 and 90 % class 1.  [ avg = 92 %]<br>
> f1-score = 92 % at class 0 and 92 % at class 1. [ avg = 92 %]
2) Neural Network :
> Accuracy = 98 % [ Validation accuracy = 98.37 % and train accuracy = 98.6 %. So, no overfit happen ]<br>
> Recall = 97 % at class 0 and 99 % at class 1. [ avg = 98 %]<br>
> Precision = 99 % at class 0 and 97 % class 1. [ avg = 98 %]<br>
> f1-score = 98 % at class 0 and 98 % at class 1. [ avg = 98 %]
3) Naive Bayes : 
> Accuracy = 71 % <br>
> Recall = 80 % at class 0 and 62 % at class 1. [ avg = 71 %] <br>
> Precision = 68 % at class 0 and 76 % class 1.  [ avg = 72 %] <br>
> f1-score = 73 % at class 0 and 68 % at class 1. [ avg = 71 %]
4) Decision Trees:
> Accuracy = 95 % <br>
> Recall = 92 % at class 0 and 97 % at class 1. [ avg = 95 %] <br>
> Precision = 97 % at class 0 and 93 % class 1.  [ avg = 95 %] <br>
> f1-score = 94 % at class 0 and 95 % at class 1. [ avg = 95 %]

## Saving Models :
we saved each model and scaler we used to be used later in deployment or at local host.
> All models are saved using pickle.dump except Neural Network was saved using save_model.

# Deployment :
## Flask : 
We created our app by using flask, then deployed it to heroku.<br>
We prepared the needed files to deploy our app sucessfully:<br>
> 1) Procfile: contains run statements for main file.
> 2) requirements.txt: contains the libraries must be downloaded by Heroku to run app file (main.py)  successfully.
> 3) runtime.txt: contains the required python version to let the app work successfully.

The files of this part is in Flask App folder.
> Decision_trees is the model used for prediction.<br>
> scaling_tree is the min_max_scaler used.<br>

You can acess to the app by using the following link :<br>
https://loan-completion-pred-flask.herokuapp.com/

## Django :
