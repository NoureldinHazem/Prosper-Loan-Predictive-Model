from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import joblib
from tensorflow.keras.models import load_model

def home(request):
    return render(request, "home.html")


def result(request):
    
    model = load_model('neural_network.h5')
    min_max_scaler = joblib.load('scaling_nn.sav')

    arr = np.array([])
    arr = np.append(arr, request.POST.get('borrowerAPR', False))
    arr = np.append(arr, request.POST.get('borrowerRate', False))
    arr = np.append(arr, request.POST.get('lenderYield', False))
    arr = np.append(arr, request.POST.get('estimatedReturn',False))
    arr = np.append(arr, request.POST.get('prosperRating',False))
    arr = np.append(arr, request.POST.get('prosperScore',False))
    arr = np.append(arr, request.POST.get('creditScoreRangeLower',False))
    arr = np.append(arr, request.POST.get('creditScoreRangeUpper',False))
    arr = np.append(arr, request.POST.get('bankcardUtilization',False))
    arr = np.append(arr, request.POST.get('availableBankcardCredit',False))
    arr = np.append(arr, request.POST.get('statedMonthlyIncome',False))
    arr = np.append(arr, request.POST.get('prosperPaymentsOneMonthPlusLate',False))
    arr = np.append(arr, request.POST.get('loanMonthsSinceOrigination',False))
    arr = np.append(arr, request.POST.get('loanOriginalAmount',False))
    arr = np.append(arr, request.POST.get('monthlyLoanPayment', False))
    arr = np.append(arr, request.POST.get('lP_CustomerPrincipalPayments',False))
    arr = np.append(arr, request.POST.get('lP_ServiceFees', False))

    arr = np.reshape(arr, (1, -1))

    normalized_arr = min_max_scaler.fit_transform(arr)
    my_prediction = model.predict(normalized_arr)

    if my_prediction[0] < 0.5:
        answer = "Loan can't be offered"
    else:
        answer = "Loan can be offered"

    return render(request, "results.html", {'ans': answer})
