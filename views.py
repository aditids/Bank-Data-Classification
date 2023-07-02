from django.shortcuts import render
from subprocess import run
from subprocess import PIPE
import sys
import test
import loan
import retention
import acquisition

def redirect(request):
    return render(request,'index.html')

def buton(request):
    return render(request, 'home.html')


def form_view(request):
    return render(request, 'form.html')


def cretention(request):
    return render(request, 'retention.html')

def cacquisition(request):
    return render(request, 'acquisition.html')

def returnhome(request):
    return render(request, 'home.html')


def external(request):
    gender=request.POST.get('gender')
    status=request.POST.get('status')
    dependents=request.POST.get('dependents')
    education=request.POST.get('education')
    selfemp=request.POST.get('selfemp')
    income=request.POST.get('income')
    c_income=request.POST.get('c_income')
    loan_amount=request.POST.get('loan_amount')
    loan_amount_term=request.POST.get('loan_amount_term')
    credit_history= request.POST.get('credit_history')
    property_area=request.POST.get('property_area')
   # out=run([sys.executable,'//test.py',gender,status,dependents,education,selfemp,income,c_income,loan_amount,loan_amount_term,
    #         credit_history,property_area], shell=False, stdout=PIPE)
    output=loan.input(gender,status,dependents,education,selfemp,income,c_income,loan_amount,loan_amount_term,credit_history,property_area)
    if(output=="Y"):
        output="Loan Status: Yes"
    else:
        output="Loan Status: No"
    #print(out)
    return render(request, 'try.html',{'data1': output})



def retention_function(request):
    gender=request.POST.get('gender')
    credit_score=request.POST.get('creditScore')
    age=request.POST.get('Age')
    tenure=request.POST.get('Tenure')
    balance=request.POST.get('Balance')
    num_of_products=request.POST.get('products')
    has_card=request.POST.get('credit_card')
    active_member=request.POST.get('active')
    estimated_salary=request.POST.get('salary')
    output=retention.classify(credit_score, gender, age, tenure, balance, num_of_products, has_card, active_member, estimated_salary)
    if(output==1):
        output="It is probable that the customer may leave the bank"
    else:
        output="Customer will not leave the bank"
    #print(out)
    return render(request, 'retention_result.html',{'data1': output})


def acquisition_function(request):
    age = request.POST.get('age')
    job = request.POST.get('job')
    marital = request.POST.get('marital')
    education = request.POST.get('education')
    balance=request.POST.get('balance')
    default=request.POST.get('default')
    housing = request.POST.get('housing')
    loan = request.POST.get('loan')
    day = request.POST.get('day')
    month = request.POST.get('month')
    duration = request.POST.get('duration')
    campaign = request.POST.get('campaign')

    output=acquisition.classify(age, job,marital, education, default, balance, housing, loan, day,month, duration, campaign)
    if(output=="yes"):
        output="Customer Is Interested!"
    else:
        output="Customer Is Not Interested!"
    #print(out)
    return render(request, 'acquisition_result.html',{'data1': output})